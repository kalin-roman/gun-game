from pygame import Rect
from random import randint
from pygame.draw import rect

from Vector import *
from units import *
from constants import DAMAGE

class Rectangl(Unit):
    rect: Rect
    width: int
    score:int

    def __init__(self, screen):
        super().__init__(screen)
        self.score = 5
        self.hp = 30
        self.width = randint(60, 100)
        radx = self.width//2
        x = randint(radx, self.size.x- radx)
        y = randint(radx, self.size.y - radx)
        self.point = Vector(x,y)
        self.rect = Rect(0,0, self.width, self.width)

    def draw(self):
        self.rect.center = self.point.get()
        rect(self.screen,self.color,self.rect)

    def move(self):
        radx = self.width//2
        self.point.add(self.speed)
        if not radx < self.point.x < self.size.x - radx:
             self.speed.x = -self.speed.x
        if not radx < self.point.y < self.size.y - radx:
             self.speed.y = -self.speed.y
    
    def check(self,x,y):
        top, right = self.rect.topright
        bottom, left = self.rect.bottomleft 
        form1 = top > x > bottom and left > y > right
        if form1:
            self.hp -= DAMAGE
        return self.score if form1 and self.is_dead() else 0