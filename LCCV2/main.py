# Imports
import os
import pygame
from LCCV2.chars import Player
from LCCV2.platforms import BackDrop, FloatingPlatform, MovingTile, BasePlatform
from LCCV2.enemies import Virus1

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
man.load_anim(IMAGES_PATH+"Characters/Player/")
man.init_guns()

# Setting up the clock
clock = pygame.time.Clock()

# Setting up the platform
platforms = [BasePlatform(0), MovingTile(400, 400), FloatingPlatform(900, 400),
             BasePlatform(1601), FloatingPlatform(1300, 400),
             MovingTile(1650, 400)]

# Loading the images for platform
platforms[0].load_anim(IMAGES_PATH + "Tilesets/level_5/platform_base.png")
platforms[1].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
platforms[2].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
platforms[3].load_anim(IMAGES_PATH + "Tilesets/level_5/platform_base.png")
platforms[4].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
platforms[5].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")

# Making the backdrop
bottom = BackDrop()
top = BackDrop()

# Loading the images for the backdrop
bottom.load_anim(IMAGES_PATH + "Background/level_1/bg_bottom.png")
top.load_anim(IMAGES_PATH + "Background/level_1/bg_top.png")
bg_layers = [top, bottom]

# Setting up Enemy
enemy = [Virus1(x=400, y=500)]
enemy[0].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/Idle/virus_1.png")
enemy[0].set_max_distance(200)

# Running the game
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        man.move(keys, platforms, enemy, bg_layers)
        platforms[1].move_x(1)
        platforms[5].move_y(1)
        enemy[0].move(3, man)
        man.change_weapon(keys)
        man.on_ground(platforms)
        clock.tick(30)
        redraw(win)


# draw function
def redraw(win):
    win.fill((104, 98, 112))
    bottom.draw(win)
    top.draw(win)
    man.draw(win)
    enemy[0].draw(win)

    for platform in platforms:
        platform.draw(win)

    pygame.display.update()


if __name__ == "__main__":
    main()
