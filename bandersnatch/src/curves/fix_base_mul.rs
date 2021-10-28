use crate::{BandersnatchParameters, EdwardsProjective, Fr, GLVParameters};
use ark_ec::{
    twisted_edwards_extended::GroupProjective, AffineCurve, ProjectiveCurve,
    TEModelParameters,
};
use ark_ff::{BigInteger, PrimeField};
use ark_std::{
    ops::{AddAssign, SubAssign},
    vec::Vec,
    Zero,
};

pub trait FixedBaseMul: TEModelParameters + Sized {
    fn preprocessing(base: GroupProjective<Self>)
        -> Vec<GroupProjective<Self>>;
    fn fixed_base_mul(
        base_pp: &[GroupProjective<Self>],
        scalar: Self::ScalarField,
    ) -> GroupProjective<Self>;
}

impl FixedBaseMul for BandersnatchParameters {
    fn preprocessing(base: EdwardsProjective) -> Vec<EdwardsProjective> {
        let mut res = Vec::new();
        let mut cur = base;
        for _ in 0..Fr::size_in_bits() {
            res.push(cur);
            cur.double_in_place();
        }
        res.push(cur);
        res
    }
    fn fixed_base_mul(
        base_pp: &[EdwardsProjective],
        scalar: Fr,
    ) -> EdwardsProjective {
        let mut res = EdwardsProjective::zero();
        for (i, bit) in scalar.into_repr().to_bits_le().iter().enumerate() {
            if *bit {
                res.add_assign(base_pp[i])
            }
        }
        res
    }
}

pub trait FixedBaseGLV: GLVParameters + FixedBaseMul {
    fn preprocessing(
        base: Self::CurveProjective,
    ) -> Vec<[EdwardsProjective; 4]>;
    fn fixed_base_mul(
        base_pp: &[[EdwardsProjective; 4]],
        scalar: Self::ScalarField,
    ) -> Self::CurveProjective;
}

impl FixedBaseGLV for BandersnatchParameters {
    fn preprocessing(base: EdwardsProjective) -> Vec<[EdwardsProjective; 4]> {
        let mut g = base;
        let mut h = Self::endomorphism(&g.into_affine()).into_projective();
        let mut g_plus_h = g + h;
        let mut g_minus_h = g - h;
        let mut res = Vec::new();
        for _ in 0..=128 {
            res.push([g, h, g_plus_h, g_minus_h]);
            g.double_in_place();
            h.double_in_place();
            g_plus_h.double_in_place();
            g_minus_h.double_in_place();
        }
        res
    }
    fn fixed_base_mul(
        base_pp: &[[EdwardsProjective; 4]],
        scalar: Fr,
    ) -> EdwardsProjective {
        let (s1, s2, s2_sign) = Self::scalar_decomposition(&scalar);

        let s1_bits = s1.into_repr().to_bits_le();
        let s2_bits = s2.into_repr().to_bits_le();

        let mut res = EdwardsProjective::zero();
        for i in 0..128 {
            // first 1 second 0: +g
            if s1_bits[i] && !s2_bits[i] {
                res.add_assign(base_pp[i][0]);
            }
            // first 0 second 1: +h
            if !s1_bits[i] && s2_bits[i] {
                if !s2_sign {
                    res.add_assign(base_pp[i][1]);
                } else {
                    res.sub_assign(base_pp[i][1])
                }
            }
            // both are 1
            if s1_bits[i] && s2_bits[i] {
                if !s2_sign {
                    // both positive: +(g+h)
                    res.add_assign(base_pp[i][2]);
                } else {
                    // first positive, second negative: +(g-h)
                    res.add_assign(base_pp[i][3])
                }
            }
        }

        res
    }
}
