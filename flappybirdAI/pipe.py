import pygame


class Pipe:
    def __init__(self,x,y,w,h) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen):
        self.r = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, (255,0,0), self.r)
        #print(self.x,self.y)
    
    def move(self):
        self.x -= 1.5
    
    def end(self):
        if((self.x + self.w) < 0):
            return True