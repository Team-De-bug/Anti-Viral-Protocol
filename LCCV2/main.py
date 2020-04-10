# Imports
import os
import pygame
from LCCV2.chars import Player
from LCCV2.platforms import BackDrop, FloatingPlatform, MovingTile, BasePlatform, Boost, TallPlatform, Endgate
from LCCV2.enemies import Virus1, Virus2

# Setting up the mixer for audio
pygame.mixer.init()

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


# Setting up the clock
clock = pygame.time.Clock()

# Setting up the player
man = Player(x=200, y=100)
man.load_anim(IMAGES_PATH+"Characters/Player/")
man.init_guns()

# Loading damage splash
WARN = pygame.image.load(IMAGES_PATH + "HUD/damage.png")


# Setting up the platform
def level_1():
    platforms = [BasePlatform(0), MovingTile(3150, 300), FloatingPlatform(300, 400),
                 FloatingPlatform(650, 250),MovingTile(1650, 236),  Boost(2250, 209), 
                 TallPlatform(1850,236), FloatingPlatform(1000, 350),FloatingPlatform(1110, 350),
                 FloatingPlatform(2500,236), FloatingPlatform(2800,300), 
                 FloatingPlatform(2910,300), BasePlatform(3650), FloatingPlatform(3350,450),
                 FloatingPlatform(3950,400), FloatingPlatform(4200,250), FloatingPlatform(4450,350),
                 FloatingPlatform(4700,350)]
    
    # Setting movement of moving platform
    platforms[4].move_style = "y"
    platforms[4].dist_y_max = 354
    platforms[4].dist_y = 354
    platforms[4].speed = 3

    platforms[1].move_style = "y"
    platforms[1].dist_y_max = 150
    platforms[1].dist_y = 150
    platforms[1].speed = 2

    # Loading the images for platform
    platforms[0].load_anim(IMAGES_PATH + "Tilesets/level_1/platform_base.png")
    platforms[1].load_anim(IMAGES_PATH + "Tilesets/level_1/moving_tile.png")
    platforms[2].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[3].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[4].load_anim(IMAGES_PATH + "Tilesets/level_1/moving_tile.png")
    platforms[5].load_anim(IMAGES_PATH + "Tilesets/heal.png")
    platforms[6].load_anim(IMAGES_PATH + "Tilesets/level_1/tall_platform.png")
    platforms[7].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[8].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[9].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[10].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[11].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[12].load_anim(IMAGES_PATH + "Tilesets/level_1/platform_base.png")
    platforms[13].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[14].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[15].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[16].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")
    platforms[17].load_anim(IMAGES_PATH + "Tilesets/level_1/platform.png")


    #loading The end portal
    portal = Endgate(5050, 473)
    portal.load_anim(IMAGES_PATH + "Tilesets/endgate.png")

    # Making the backdrop
    background = [BackDrop(), BackDrop()]

    # Loading the images for the backdrop
    background[0].load_anim(IMAGES_PATH + "Background/level_1/bg_bottom.png")
    background[1].load_anim(IMAGES_PATH + "Background/level_1/bg_top.png")

    # Setting up Enemy
    enemies = [Virus1(x=400, y=500), Virus1(x=1000, y=275), Virus1(x=1110, y=500), Virus1(x=2000, y=130),
               Virus1(x=2900, y=200), Virus1(x=3950, y=500), Virus1(x=4300, y=500)]
   
    enemies[0].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[0].set_max_distance(200)

    enemies[1].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[1].set_max_distance(100)

    enemies[2].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[2].set_max_distance(200)

    enemies[3].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[3].set_max_distance(50)

    enemies[4].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[4].set_max_distance(10)

    enemies[5].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[5].set_max_distance(100)

    enemies[6].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[6].set_max_distance(100)

    return platforms, enemies, background, portal


def level_2():
    man.x, man.y = 50, 300
    platforms = [BasePlatform(200), MovingTile(3150, 300), FloatingPlatform(0, 500),
                 FloatingPlatform(450, 400), MovingTile(1800, 350), Boost(400, 350),
                 TallPlatform(2500, 236), FloatingPlatform(810, 250), FloatingPlatform(920, 250),
                 FloatingPlatform(1030, 250), FloatingPlatform(1200, 425),
                 FloatingPlatform(1400, 200), BasePlatform(3650), FloatingPlatform(1600, 350),
                 FloatingPlatform(2300, 350), TallPlatform(3040, 236),FloatingPlatform(3580, 375)]

    # Setting movement of moving platform
    platforms[4].move_style = "x"
    platforms[4].dist_x_max = 300
    platforms[4].dist_x = 300
    platforms[4].speed = 3

    platforms[1].move_style = "y"
    platforms[1].dist_y_max = 340
    platforms[1].dist_y = 340

    # Loading the images for platform
    platforms[0].load_anim(IMAGES_PATH + "Tilesets/level_2/platform_base.png")
    platforms[1].load_anim(IMAGES_PATH + "Tilesets/level_2/moving_tile.png")
    platforms[2].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[3].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[4].load_anim(IMAGES_PATH + "Tilesets/level_2/moving_tile.png")
    platforms[5].load_anim(IMAGES_PATH + "Tilesets/heal.png")
    platforms[6].load_anim(IMAGES_PATH + "Tilesets/level_2/tall_platform.png")
    platforms[7].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[8].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[9].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[10].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[11].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[12].load_anim(IMAGES_PATH + "Tilesets/level_2/platform_base.png")
    platforms[13].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[14].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[15].load_anim(IMAGES_PATH + "Tilesets/level_2/tall_platform.png")
    platforms[16].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")


    # loading The end portal
    portal = Endgate(5050, 473)
    portal.load_anim(IMAGES_PATH + "Tilesets/endgate.png")

    # Making the backdrop
    background = [BackDrop(), BackDrop()]

    # Loading the images for the backdrop
    background[0].load_anim(IMAGES_PATH + "Background/level_2/bg_bottom.png")
    background[1].load_anim(IMAGES_PATH + "Background/level_2/bg_top.png")

    # Setting up Enemy
    enemies = [Virus1(x=400, y=500), Virus1(x=1000, y=150), Virus2(x=1250, y=475), Virus1(x=2375, y=250),
               Virus1(x=2700, y=125), Virus2(x=3250, y=110)]

    enemies[0].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[0].set_max_distance(200)

    enemies[1].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[1].set_max_distance(100)

    enemies[2].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[2].set_max_distance(200)

    enemies[3].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[3].set_max_distance(0)

    enemies[4].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[4].set_max_distance(25)

    enemies[5].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[5].set_max_distance(200)

    return platforms, enemies, background, portal


# Loading images for hud
weapons_list = [pygame.image.load(IMAGES_PATH + "Weapons/gun_pistol.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_shotgun.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_ar.png"),
                pygame.image.load(IMAGES_PATH + "Weapons/gun_rpg.png")]

infection_img = [pygame.image.load(IMAGES_PATH + "HUD/infection_0.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_1.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_2.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_3.png"),
                 pygame.image.load(IMAGES_PATH + "HUD/infection_4.png")]

# Loading image for game over screen
game_over_img = pygame.image.load(IMAGES_PATH + "HUD/game-over.png")

PLATFORMS = None
ENEMIES = None
BACKGROUND = None
PORTAL = None

LOAD_LEVEL = True
PAUSED = False

LEVELS = [level_1, level_2]
LEVEL_NUM = 0

DAMAGED = False


# Running the game
def main():
    running = True

    global LOAD_LEVEL
    global PLATFORMS
    global ENEMIES
    global BACKGROUND
    global PORTAL
    global LEVELS
    global LEVEL_NUM

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if LOAD_LEVEL:
            if LEVEL_NUM < 2:
                PLATFORMS, ENEMIES, BACKGROUND, PORTAL = LEVELS[LEVEL_NUM]()
                LOAD_LEVEL = False
            else:
                game_over(win)
                clock.tick(5)

        else:

            if PAUSED:
                keys = pygame.key.get_pressed()
                paused(win, keys)

            else:

                if man.hp <= 0:
                    game_over(win)
                    clock.tick(5)

                else:
                    check_portal(PORTAL, man)
                    keys = pygame.key.get_pressed()
                    paused(win, keys)

                    for platform in PLATFORMS:
                        if platform.is_moving:
                            platform.move()

                    for enemy in ENEMIES:
                        enemy.move(3, man)
                        enemy.hurt_player(man)

                    man.change_weapon(keys)
                    man.on_ground(PLATFORMS)
                    man.move(keys, PLATFORMS, ENEMIES, BACKGROUND, PORTAL)
                    hit_player(man, ENEMIES)
                    man.infection_damage()
                    clock.tick(30)
                    redraw(win, BACKGROUND, ENEMIES, PLATFORMS)


        pygame.display.update()


damage_delay = 20


# draw function
def redraw(win, background, enemies, platforms):


    global DAMAGED
    global WARN
    global damage_delay
    win.fill((104, 98, 112))

    for layer in background:
        layer.draw(win)

    man.draw(win)
    for enemy in enemies:
        enemy.draw(win)

    enemy_health_bar(win, enemies, man)

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

    PORTAL.draw(win)
    for enemy in enemies:
        enemy.update_bullets(win)

    if DAMAGED:
        win.blit(WARN, (0, 0))
        if damage_delay > 0:
            damage_delay -= 1
        else:
            DAMAGED = False
            damage_delay = 20


# player damage by projectiles from enemies
def hit_player(man, enemies):
    for enemy in enemies:
        for ammo in enemy.ammo_list:
            if man.x + man.width > ammo.x > man.x and man.y + man.height > ammo.y > man.y:
                man.hp -= enemy.ammo.damage
                global DAMAGED
                DAMAGED = True
                if man.infection < 4:
                    man.infection += 1
                enemy.ammo_list.pop(enemy.ammo_list.index(ammo))


def update_infection(man, win):
    win.blit(infection_img[man.infection],  (1064, 8))


def paused(win, keys):
    global PAUSED
    if keys[pygame.K_ESCAPE] and not PAUSED:
        PAUSED = True

    if PAUSED:
        pygame.draw.rect(win, (255, 255, 255), (500, 250, 200, 100))
        text = font_20.render("Game Paused ", 1, (0, 0, 0))
        text2 = font.render("Press C to continue", 1, (0, 0, 0))
        win.blit(text, (545, 270))
        win.blit(text2, (540, 300))

    if keys[pygame.K_c] and PAUSED:
        PAUSED = False


img_limit = 14
img = 0


def game_over(win):

    global img
    if img < img_limit:
        img += 1
        win.blit(game_over_img, (0, 0), (img * 1200, 0, 1200, 640))


def enemy_health_bar(win, enemies, man):
    for enemy in enemies:
        pygame.draw.rect(win, (50, 50, 50), (enemy.x - 10, enemy.y - 17, 104, 14))
        if enemy.hp > 0:
            pygame.draw.rect(win, (100 - enemy.hp + 50, enemy.hp + 50, 0), (enemy.x - 8, enemy.y - 15, enemy.hp, 10))
        else:
            man.score += enemy.points
            enemies.pop(enemies.index(enemy))


# next level
def check_portal(portal, man):
    global LOAD_LEVEL
    global LEVEL_NUM
    if portal.x + portal.width > man.x + man.hit_x[man.width_num] > portal.x and portal.y + portal.height > man.y > portal.y:
        LOAD_LEVEL = True
        LEVEL_NUM += 1


if __name__ == "__main__":
    main()
