from random import randint
from pygame.draw import circle

from Vector import *
from units import *
from constants import DAMAGE

class Ball(Unit):
    rad: int
    score: int

    def __init__(self,screen) -> None:
        super().__init__(screen)
        self.hp = 10
        self.score = 10
        self.rad = randint(30,50)
        x = randint(self.rad, self.size.x- self.rad)
        y = randint(self.rad, self.size.y - self.rad)
        self.point = Vector(x ,y)

    def draw(self):
        circle(self.screen, self.color, self.point.get(), self.rad)


    def move(self):
        self.point.add(self.speed)
        if not self.rad < self.point.x < self.size.x - self.rad:
            self.speed.x = -self.speed.x
        if not self.rad < self.point.y < self.size.y - self.rad:
            self.speed.y = -self.speed.y


    def check(self,x,y):
        formule1 = ((self.point.x - x) ** 2 + (self.point.y - y) ** 2) ** 0.5
        if formule1 <= self.rad:
            self.hp -= DAMAGE
        return self.score if self.is_dead() and formule1 <= self.rad else 0
    