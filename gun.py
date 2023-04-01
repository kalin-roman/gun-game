from pygame import Rect,Surface
from pygame.draw import circle
from pygame.draw import line
from math import *

from units import *
from Vector import *
from colors import RED,GRAY

RADIUS = 40
WIDTH = 20
HIGHT = RADIUS * 2

class Gun(Unit):
    angle: float

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.point = Vector(self.size.x // 2, self.size.y)
        self.angle = 0.0
        # self.rect = Surface(( WIDTH, HIGHT))  
    
    def setMouse(self,x,y):
        a = Vector( x - self.point.x, y - self.point.y)
        b = Vector(self.size.x, 0)
        print(self.point.get() , b.get(),'x =' ,x ,'y = ', y)
        self.angle = a.angle(b)
        # print(a.get(),b.get(),a.mul(b))
    
    def draw(self):
        end_x = HIGHT * cos(self.angle) + self.point.x
        end_y = HIGHT * sin(self.angle) + self.point.y
        line(self.screen, GRAY,self.point.get(), (end_x, end_y), WIDTH)
        circle(self.screen, RED, self.point.get(), RADIUS)

    def move(self):
        pass

    def check(self,x,y):
        return 0
    