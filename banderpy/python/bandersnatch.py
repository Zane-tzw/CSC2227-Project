from libbanderpy import *

class Point():

    def __init__(self, generator = False):
        if generator==False:
            self.p = random_point_rust()
        else: 
            self.p = get_generator_rust()
        
    def __str__(self):
        return point_to_string_rust(self.p)

    def __eq__(self, other):
        return self.p == other.p
    
    def add(self, other):
        self.p = add_rust(self.p, other.p)

    def double(self):
        self.p = double_rust(self.p)

    def mul(self, scalar):
        self.p = mul_rust(self.p, scalar.s)

    def glv(self, scalar):
        self.p = glv_rust(self.p, scalar.s)

    def msm(self, points, scalars):
        self.p = msm_rust(points, scalars)


class Scalar():
    def __init__(self):
        self.s = random_scalar_rust()

    def __str__(self):
        return scalar_to_string_rust(self.s)
