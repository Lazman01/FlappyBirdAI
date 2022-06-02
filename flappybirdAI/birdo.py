from mimetypes import init
from re import X
from tkinter import Y
#from turtle import circle
import pygame
import math
from pygame import *


class Birdo:
    def __init__(self,x,y,r) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.r = r
        self.time = 0
        self.h = self.y
        self.die = False
    
    def move(self,h):
        if(((self.y + self.r) <= h)):
            self.y = 32*(self.time**2) - 96*self.time + self.h
            self.time += 0.05
            
    
    def jump(self,h):
        if(((self.y + self.r) <= h) and not self.die and self.time > 0.05):
            self.time = 0
            self.h = self.y
            
    
    def draw(self,surface):
        num = -self.r
        pygame.draw.circle(surface, (255, 255, 74), [self.x,self.y], self.r)
        self.c1 = Rect(self.x-(self.r), self.y-(self.r/2), self.r*2,self.r)
        self.c2 = Rect(self.x-(self.r/2), self.y-(self.r), self.r, self.r*2)
        pygame.draw.rect(surface, (255,0,0), self.c1)
        pygame.draw.rect(surface,(255,0,0),self.c2)

    
    def dies(self, h, c):
        if(((self.y + self.r) >= h) or c or ((self.y + self.r) <= 0)):
            self.die = True
        
        return self.die

    




















