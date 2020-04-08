# Imports
import os
import pygame
from LCCV2.chars import Player
from LCCV2.platforms import BackDrop, FloatingPlatform, MovingTile, BasePlatform
from LCCV2.enemies import Virus1

# Setting up the font
pygame.font.init()
font = pygame.font.Font("resources/fonts/DJB Get Digital.ttf", 14)
font_20 = pygame.font.Font("resources/fonts/DJB Get Digital.ttf", 20)

# Working file paths
IMAGES_PATH = 'resources/Images/'

# Starting pygame
pygame.init()

# Loading the image for hud
hud = pygame.image.load(IMAGES_PATH + "HUD/hud.png")

# Setting the screen up
win = pygame.display.set_mode((1200, 640))
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
enemies = [Virus1(x=800, y=500), Virus1(x=1000, y=500)]
enemies[0].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
enemies[0].set_max_distance(200)

enemies[1].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
enemies[1].set_max_distance(200)


# Loading images for hud
weapons_list = [pygame.image.load(IMAGES_PATH + "Weapons/gun_pistol.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_shotgun.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_rpg.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_ar.png")]

infection_img = [pygame.image.load(IMAGES_PATH + "HUD/infection_0.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_1.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_2.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_3.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_4.png")]


# Running the game
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if man.hp <= 0:
            win.fill((255, 255, 255))
            over = font_20.render("game over", 1, (0, 0, 0))
            win.blit(over, (400,400))

        else:
            keys = pygame.key.get_pressed()
            platforms[1].move_x(1)
            platforms[5].move_y(1)
            for enemy in enemies:
                enemy.move(3, man)
                enemy.hurt_player(man)
            man.change_weapon(keys)
            man.on_ground(platforms)
            man.move(keys, platforms, enemies, bg_layers)
            hit_player(man, enemies)
            man.infection_damage()
            clock.tick(30)
            redraw(win)

        pygame.display.update()


# draw function
def redraw(win):
    win.fill((104, 98, 112))
    bottom.draw(win)
    top.draw(win)
    man.draw(win)
    for enemy in enemies:
        enemy.draw(win)

    for platform in platforms:
        platform.draw(win)

    # Stats part
    win.blit(hud, (0, 0))
    score = font.render(f"Score: {man.score}", 1, (132, 0, 255))
    life_left = font.render(f"Health: {man.hp}", 1, (255, 32, 32))
    infection = font_20.render(f"Infection", 1, (250, 0, 0))
    update_infection(man, win)
    win.blit(life_left, (18, 12))
    win.blit(score, (18, 35))
    win.blit(infection, (1075, 105))
    if man.current_weapon != 0:
        weapon_name = font.render(man.weapon_list[man.current_weapon], 1, (255, 168, 0))
        ammo_left = font.render(
            f" - Ammo: {man.weapons[man.weapon_list[man.current_weapon]].ammo_count}/{man.weapons[man.weapon_list[man.current_weapon]].ammo_limit}",
            1, (255, 168, 0))
        ammo_on_load = font.render(
            f"Loaded: {man.weapons[man.weapon_list[man.current_weapon]].on_load}/{man.weapons[man.weapon_list[man.current_weapon]].hold_limit}",
            1, (255, 168, 0))
        win.blit(weapon_name, (25, 66))
        win.blit(ammo_left, (70, 66))
        win.blit(weapons_list[man.current_weapon - 1], (23, 84))
        win.blit(ammo_on_load, (70, 105))

    for enemy in enemies:
        enemy.update_bullets(win)


# player damage by projectiles from enemies
def hit_player(man, enemies):
    for enemy in enemies:
        for ammo in enemy.ammo_list:
            if man.x + man.width > ammo.x > man.x:
                man.hp -= enemy.ammo.damage
                if man.infection < 4:
                    man.infection += 1
                enemy.ammo_list.pop(enemy.ammo_list.index(ammo))


def update_infection(man, win):
    win.blit(infection_img[man.infection],  (1064, 8))


def game_over(win):
    win.fill((255,255,255))


if __name__ == "__main__":
    main()
