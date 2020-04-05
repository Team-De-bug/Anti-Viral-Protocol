# Imports
import os
import pygame
from LCCV2.chars import Player
from LCCV2.platforms import MockPlatform

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
man = Player(x=300, y=100)
man.load_anim(IMAGES_PATH+"Characters/Player/idle.png")

# Setting up the clock
clock = pygame.time.Clock()

# Setting up the platform
platforms = [MockPlatform(800, 50, x=0, y=600), MockPlatform(128, 25, x=400, y=400),
             MockPlatform(800, 50, x=800, y=600), MockPlatform(128, 25, x=900, y=400),
             MockPlatform(800, 50, x=1600, y=600), MockPlatform(128, 25, x=1300, y=400)]


# Running the game
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        man.move(platforms)
        man.on_ground(platforms)
        clock.tick(30)
        redraw(win)


# draw function
def redraw(win):
    win.fill((105, 26, 26))
    man.draw(win)
    for platform in platforms:
        platform.draw(win)
    pygame.display.update()


if __name__ == "__main__":
    main()
