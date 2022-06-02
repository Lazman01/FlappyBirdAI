from operator import truediv
import pygame
from pygame import *
from pipes import Pipes
from birdos import Birdos
import neat
import os

#set framerate
clock = pygame.time.Clock()
FPS = 60

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = int(SCREEN_WIDTH * 1.5)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird :)')

sc = True

def main(genomes, config):
    nets = []
    ge = []

    birdos = Birdos(SCREEN_HEIGHT,10)

    pipes = Pipes()

    score = 0

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birdos.addBirdo(SCREEN_HEIGHT)
        g.fitness = 0
        ge.append(g)


    def collisions(c1,c2):
        for pip in pipes.list:
            for p in pip:
                if(p.r.colliderect(c1) or p.r.colliderect(c2)):
                    return True


    run = True
    while run:

        for event in pygame.event.get():
            #Quits Game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        pipes.start(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        pipe_ind = 0
        if len(birdos.list) > 0:
            if len(pipes.list) > 1 and birdos.get(0).x > pipes.get(0,0).x + pipes.get(0,0).w:
                pipe_ind = 1
                if(sc):
                    score+=1
                    sc = False
                    print(score)
            else:
                score = int(score)
                sc = True
        else:
            run = False
            score = int(score)
            break
        
        
        for x, birdo in enumerate(birdos.list):
            ge[x].fitness += 0.1

            output = nets[x].activate((birdo.y, abs(birdo.y - pipes.get(pipe_ind,0).y), abs(birdo.y - pipes.get(pipe_ind,1).y)))

            if output[0] > 0.5:
                birdo.jump(SCREEN_HEIGHT)

        screen.fill(255)

        

        clock.tick(FPS)

        
        #Pipes
        pipes.move()
        pipes.draw(screen)
        pipes.addPipe(SCREEN_WIDTH, SCREEN_HEIGHT,ge)

        #Birdo
        birdos.move(SCREEN_HEIGHT)
        birdos.draw(screen)
        for x,p in enumerate(birdos.list):
            coll = collisions(p.c1,p.c2)
            
            b = p.dies(SCREEN_HEIGHT, coll)
            if b:
                ge[x].fitness -= 5
                birdos.list.pop(x)
                nets.pop(x)
                ge.pop(x)
        
        
        pygame.display.update()

    


def runs(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    runs(config_path)