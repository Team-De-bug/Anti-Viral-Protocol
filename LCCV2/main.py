#imports
import os
import pygame

#working filepaths
WRKFOLDER = os.path.dirname(__file__)
FINALPATH = os.path.join(WRKFOLDER, 'resources/final')

#initialise
pygame.init()

#setup
SCREEN = pygame.display.set_mode((800, 640))
pygame.display.set_caption("LCC GAME")
ICON = pygame.image.load(os.path.join(FINALPATH, 'GameIcon_64.png'))
pygame.display.set_icon(ICON)

#keeping screen open
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False   
    SCREEN.fill((133, 37, 20))
