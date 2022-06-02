import random
from pipe import Pipe
import pygame

class Pipes:
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.list = []
        self.width = 80
        self.gap = 150

        self.x = 2

        self.score = 0
    
    def move(self):
        for pip in self.list:
            for p in pip:
                p.move()
    
    def draw(self, screen):
        for pip in self.list:
            for p in pip:
                p.draw(screen)
        
        #print("Score: " + str(self.score))
    
    def addPipe(self,start,num,ge):
        if(self.list[0][0].end() and self.x >= 5):
            self.list.pop(0)

            y = random.randint(num*0.3,num*0.7)
            pipe1 = Pipe((start/2)*2.6, y, self.width, num)
            pipe2 = Pipe((start/2)*2.6, 0, self.width, y-self.gap)

            temp = [pipe1,pipe2]

            self.list.append(temp)

            for g in ge:
                g.fitness += 5
            
            self.score+=1
            
    
    def start(self,start,num):
        while(self.x < 5):
            y = random.randint(num*0.3,num*0.7)
            pipe1 = Pipe((start/2)*self.x, y, self.width, num)
            pipe2 = Pipe((start/2)*self.x, 0, self.width, y-self.gap)

            temp = [pipe1,pipe2]

            self.list.append(temp)
            self.x+=1
        
    def get(self,x,y):
        for pip in self.list:
            if self.list.index(pip) == x:
                for p in pip:
                    if pip.index(p) == y:
                        return p
        return -1
        
        #print(len(self.list))


        