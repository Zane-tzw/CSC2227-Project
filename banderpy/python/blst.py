# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _blst
else:
    import _blst

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _blst.SWIG_PyInstanceMethod_New
_swig_new_static_method = _blst.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


BLST_SUCCESS = _blst.BLST_SUCCESS
BLST_BAD_ENCODING = _blst.BLST_BAD_ENCODING
BLST_POINT_NOT_ON_CURVE = _blst.BLST_POINT_NOT_ON_CURVE
BLST_POINT_NOT_IN_GROUP = _blst.BLST_POINT_NOT_IN_GROUP
BLST_AGGR_TYPE_MISMATCH = _blst.BLST_AGGR_TYPE_MISMATCH
BLST_VERIFY_FAIL = _blst.BLST_VERIFY_FAIL
BLST_PK_IS_INFINITY = _blst.BLST_PK_IS_INFINITY
class SecretKey(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    keygen = _swig_new_instance_method(_blst.SecretKey_keygen)
    from_bendian = _swig_new_instance_method(_blst.SecretKey_from_bendian)
    from_lendian = _swig_new_instance_method(_blst.SecretKey_from_lendian)
    to_bendian = _swig_new_instance_method(_blst.SecretKey_to_bendian)
    to_lendian = _swig_new_instance_method(_blst.SecretKey_to_lendian)

    def __init__(self):
        _blst.SecretKey_swiginit(self, _blst.new_SecretKey())
    __swig_destroy__ = _blst.delete_SecretKey

# Register SecretKey in _blst:
_blst.SecretKey_swigregister(SecretKey)

class P1_Affine(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.P1_Affine_swiginit(self, _blst.new_P1_Affine(*args))
    dup = _swig_new_instance_method(_blst.P1_Affine_dup)
    to_jacobian = _swig_new_instance_method(_blst.P1_Affine_to_jacobian)
    serialize = _swig_new_instance_method(_blst.P1_Affine_serialize)
    compress = _swig_new_instance_method(_blst.P1_Affine_compress)
    on_curve = _swig_new_instance_method(_blst.P1_Affine_on_curve)
    in_group = _swig_new_instance_method(_blst.P1_Affine_in_group)
    is_inf = _swig_new_instance_method(_blst.P1_Affine_is_inf)
    is_equal = _swig_new_instance_method(_blst.P1_Affine_is_equal)
    core_verify = _swig_new_instance_method(_blst.P1_Affine_core_verify)
    generator = _swig_new_static_method(_blst.P1_Affine_generator)
    __swig_destroy__ = _blst.delete_P1_Affine

# Register P1_Affine in _blst:
_blst.P1_Affine_swigregister(P1_Affine)
P1_Affine_generator = _blst.P1_Affine_generator

class P1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.P1_swiginit(self, _blst.new_P1(*args))
    dup = _swig_new_instance_method(_blst.P1_dup)
    to_affine = _swig_new_instance_method(_blst.P1_to_affine)
    serialize = _swig_new_instance_method(_blst.P1_serialize)
    compress = _swig_new_instance_method(_blst.P1_compress)
    on_curve = _swig_new_instance_method(_blst.P1_on_curve)
    in_group = _swig_new_instance_method(_blst.P1_in_group)
    is_inf = _swig_new_instance_method(_blst.P1_is_inf)
    is_equal = _swig_new_instance_method(_blst.P1_is_equal)
    aggregate = _swig_new_instance_method(_blst.P1_aggregate)
    sign_with = _swig_new_instance_method(_blst.P1_sign_with)
    hash_to = _swig_new_instance_method(_blst.P1_hash_to)
    encode_to = _swig_new_instance_method(_blst.P1_encode_to)
    mult = _swig_new_instance_method(_blst.P1_mult)
    cneg = _swig_new_instance_method(_blst.P1_cneg)
    neg = _swig_new_instance_method(_blst.P1_neg)
    add = _swig_new_instance_method(_blst.P1_add)
    dbl = _swig_new_instance_method(_blst.P1_dbl)
    generator = _swig_new_static_method(_blst.P1_generator)
    __swig_destroy__ = _blst.delete_P1

# Register P1 in _blst:
_blst.P1_swigregister(P1)
P1_generator = _blst.P1_generator

class P2_Affine(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.P2_Affine_swiginit(self, _blst.new_P2_Affine(*args))
    dup = _swig_new_instance_method(_blst.P2_Affine_dup)
    to_jacobian = _swig_new_instance_method(_blst.P2_Affine_to_jacobian)
    serialize = _swig_new_instance_method(_blst.P2_Affine_serialize)
    compress = _swig_new_instance_method(_blst.P2_Affine_compress)
    on_curve = _swig_new_instance_method(_blst.P2_Affine_on_curve)
    in_group = _swig_new_instance_method(_blst.P2_Affine_in_group)
    is_inf = _swig_new_instance_method(_blst.P2_Affine_is_inf)
    is_equal = _swig_new_instance_method(_blst.P2_Affine_is_equal)
    core_verify = _swig_new_instance_method(_blst.P2_Affine_core_verify)
    generator = _swig_new_static_method(_blst.P2_Affine_generator)
    __swig_destroy__ = _blst.delete_P2_Affine

# Register P2_Affine in _blst:
_blst.P2_Affine_swigregister(P2_Affine)
P2_Affine_generator = _blst.P2_Affine_generator

class P2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.P2_swiginit(self, _blst.new_P2(*args))
    dup = _swig_new_instance_method(_blst.P2_dup)
    to_affine = _swig_new_instance_method(_blst.P2_to_affine)
    serialize = _swig_new_instance_method(_blst.P2_serialize)
    compress = _swig_new_instance_method(_blst.P2_compress)
    on_curve = _swig_new_instance_method(_blst.P2_on_curve)
    in_group = _swig_new_instance_method(_blst.P2_in_group)
    is_inf = _swig_new_instance_method(_blst.P2_is_inf)
    is_equal = _swig_new_instance_method(_blst.P2_is_equal)
    aggregate = _swig_new_instance_method(_blst.P2_aggregate)
    sign_with = _swig_new_instance_method(_blst.P2_sign_with)
    hash_to = _swig_new_instance_method(_blst.P2_hash_to)
    encode_to = _swig_new_instance_method(_blst.P2_encode_to)
    mult = _swig_new_instance_method(_blst.P2_mult)
    cneg = _swig_new_instance_method(_blst.P2_cneg)
    neg = _swig_new_instance_method(_blst.P2_neg)
    add = _swig_new_instance_method(_blst.P2_add)
    dbl = _swig_new_instance_method(_blst.P2_dbl)
    generator = _swig_new_static_method(_blst.P2_generator)
    __swig_destroy__ = _blst.delete_P2

# Register P2 in _blst:
_blst.P2_swigregister(P2)
P2_generator = _blst.P2_generator

G1 = _blst.G1
G2 = _blst.G2
class PT(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.PT_swiginit(self, _blst.new_PT(*args))
    dup = _swig_new_instance_method(_blst.PT_dup)
    is_one = _swig_new_instance_method(_blst.PT_is_one)
    is_equal = _swig_new_instance_method(_blst.PT_is_equal)
    sqr = _swig_new_instance_method(_blst.PT_sqr)
    mul = _swig_new_instance_method(_blst.PT_mul)
    final_exp = _swig_new_instance_method(_blst.PT_final_exp)
    __swig_destroy__ = _blst.delete_PT

# Register PT in _blst:
_blst.PT_swigregister(PT)

class Pairing(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _blst.Pairing_swiginit(self, _blst.new_Pairing(*args))
    __swig_destroy__ = _blst.delete_Pairing
    aggregate = _swig_new_instance_method(_blst.Pairing_aggregate)
    mul_n_aggregate = _swig_new_instance_method(_blst.Pairing_mul_n_aggregate)
    commit = _swig_new_instance_method(_blst.Pairing_commit)
    merge = _swig_new_instance_method(_blst.Pairing_merge)
    finalverify = _swig_new_instance_method(_blst.Pairing_finalverify)

# Register Pairing in _blst:
_blst.Pairing_swigregister(Pairing)

cdata = _blst.cdata
memmove = _blst.memmove

cvar = _blst.cvar
BLS12_381_G1 = cvar.BLS12_381_G1
BLS12_381_NEG_G1 = cvar.BLS12_381_NEG_G1
BLS12_381_G2 = cvar.BLS12_381_G2
BLS12_381_NEG_G2 = cvar.BLS12_381_NEG_G2

