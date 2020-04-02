# Imports
import os
import pygame

# Working file paths
WORK_FOLDER = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(WORK_FOLDER, 'resources/Images/Icon')

# Starting pygame
pygame.init()

# Setting the screen up
SCREEN = pygame.display.set_mode((800, 640))
pygame.display.set_caption("LCC GAME")
ICON = pygame.image.load(os.path.join(IMAGES_PATH, 'GameIcon_64.png'))
pygame.display.set_icon(ICON)

# Running the game
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    SCREEN.fill((105, 26, 26))
    pygame.display.update()
