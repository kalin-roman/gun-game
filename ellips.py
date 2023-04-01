from pygame import Rect
from random import randint
from pygame.draw import ellipse

from Vector import *
from units import *
from constants import DAMAGE

class Ellipse(Unit):    
    rect: Rect
    score: int
    r1: int
    r2: int

    def __init__(self, screen):
        super().__init__(screen)
        self.score = 15
        self.hp = 20
        width = randint(20,120)
        height = randint(20,120)
        self.r1 = height // 2
        self.r2 = width // 2
        self.rect = Rect(0,0,width,height)
        x = randint(self.r1, self.size.x- self.r1)
        y = randint(self.r2, self.size.y - self.r2)
        self.point = Vector(x,y)

    def draw(self):
        self.rect.center = self.point.get()
        ellipse(self.screen, self.color, self.rect)

    def move(self):
        self.point.add(self.speed)
        if not self.r1 < self.point.y < self.size.y - self.r1:
            self.speed.y = -self.speed.y
        if not self.r2 < self.point.x < self.size.x - self.r2:
            self.speed.x = -self.speed.x

    def check(self,x,y):
        form = (x - self.point.x)**2//self.r2**2 + (y - self.point.y)**2//self.r1**2 <= 1
        if form:
            self.hp -= DAMAGE
        return self.score if self.is_dead() and form  else 0