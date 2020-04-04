# Imports
import os
import pygame
from LCCV2.chars import Player

# Working file paths
IMAGES_PATH = 'resources/Images/'

# Starting pygame
pygame.init()

# Setting the screen up
win = pygame.display.set_mode((800, 640))
pygame.display.set_caption("LCC GAME")
ICON = pygame.image.load(os.path.join(IMAGES_PATH+"Icon/", 'GameIcon_64.png'))
pygame.display.set_icon(ICON)

# Setting up the player
man = Player(x=10, y=100)
man.load_anim(IMAGES_PATH+"Characters/Player/idle.png")


# Running the game
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        man.move()
        redraw(win)


# draw function
def redraw(win):
    win.fill((105, 26, 26))
    man.draw(win)
    pygame.display.update()


if __name__ == "__main__":
    main()
