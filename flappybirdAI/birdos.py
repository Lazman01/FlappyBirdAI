from mimetypes import init
from birdo import Birdo
import pygame

class Birdos:
    def __init__(self,h,pop) -> None:
        self.list = []

    
    def move(self,h):
        for p in self.list:
            p.move(h)
    
    def draw(self,screen):
        for p in self.list:
            p.draw(screen)
        
    def addBirdo(self,h):
        birdo = Birdo(120, h/2, 10)
        self.list.append(birdo)
    
    def get(self,x):
        return self.list[x]
    
    