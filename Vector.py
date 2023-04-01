from math import pi
import numpy as np

class Vector:
    x : int
    y : int
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def get(self):
        return (self.x,self.y)
    
    def add(self, v):
        self.x += v.x
        self.y += v.y
    
    def mul(self, v):
        return self.x * v.x + self.y * v.y
    
    def mod(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def angle(self,v):
        mul_mod = self.mod() * v.mod()
        rad = 0 if mul_mod == 0 else self.mul(v)/ mul_mod
        return rad
        # return (self.mod(), v.mod())
    
    # def angle_2(self,b,c):
    #     CA = Vector(self.x - c.x, self.y - c.y)
    #     CB = Vector(b.x - c.x, b.y - c.y)
    #     mul_mod = CA.mod() * CB.mod()
    #     rad = 0 if mul_mod == 0 else CA.mul(CB)/ mul_mod
    #     return rad 