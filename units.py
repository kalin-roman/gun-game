from pygame.surface import Surface
from random import randint

from Vector import *
from colors import get_color

class Unit:
    screen: Surface
    size: Vector
    color: tuple
    speed: Vector
    point: Vector
    hp: int

    def __init__(self, screen) -> None:
        self.hp = 0
        self.screen = screen
        self.size = Vector(*self.screen.get_size())
        self.color = get_color()
        speedx = randint(1,5)
        speedy = randint(1,5) 
        self.speed = Vector(speedx,speedy)
        self.point = None

    def draw(self) -> None:
        '''
         Interaface,  need to implement
        '''
        raise NotImplementedError()
    
    def move(self) -> None:
        '''
         Interaface,  need to implement
        '''
        raise NotImplementedError()
    
    def check(self,x,y) -> int:
        '''
         Interaface,  need to implement
        '''
        raise NotImplementedError()
    
    def is_dead(self) -> bool:
        return self.hp <= 0 