import pygame
import sys, os
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

GAME_ROOT_FOLDER=os.path.dirname(__file__)
IMAGE_FOLDER=os.path.join(GAME_ROOT_FOLDER,"Images")

pygame.init()

clock = pygame.time.Clock()
clock.tick(60)

pygame.display.set_caption("Crazy Driver")
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER,"Road.png"))
screen=pygame.display.set_mode((500,800))

# screen.fill(WHITE)

while True:
    screen.blit(IMG_ROAD,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()