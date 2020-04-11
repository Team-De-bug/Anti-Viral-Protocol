# Imports
import os
import pygame
from LCCV2.chars import Player
from LCCV2.platforms import BackDrop, FloatingPlatform, MovingTile, BasePlatform, Boost, TallPlatform, Endgate
from LCCV2.enemies import Virus1, Virus2, Virus3, Virus4
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
man = Player(x=100, y=100)
man.load_anim(IMAGES_PATH+"Characters/Player/")
man.init_guns()

# Loading damage splash
WARN = pygame.image.load(IMAGES_PATH + "HUD/damage.png")

# Loading the mission log images
mission_log = pygame.image.load(IMAGES_PATH + "Menus/mission.png")

# loading the pause screen
pause_screen = pygame.image.load(IMAGES_PATH + "Menus/pause.png")

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
    enemies = [Virus1(x=400, y=500), Virus1(x=1000, y=260), Virus1(x=1110, y=500), Virus1(x=2000, y=130),
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
    platforms = [BasePlatform(200), MovingTile(3938, 125), FloatingPlatform(0, 500),
                 FloatingPlatform(450, 400), MovingTile(1800, 350), Boost(3600, 350),
                 TallPlatform(2500, 236), FloatingPlatform(810, 250), FloatingPlatform(920, 250),
                 FloatingPlatform(1030, 250), FloatingPlatform(1200, 425),
                 FloatingPlatform(1400, 200), BasePlatform(4175), FloatingPlatform(1600, 350),
                 FloatingPlatform(2300, 350), TallPlatform(3040, 236),FloatingPlatform(3580, 375),
                 FloatingPlatform(3700, 125), FloatingPlatform(4350, 400), FloatingPlatform(4600, 200),
                 FloatingPlatform(4850, 300), FloatingPlatform(4960, 300), FloatingPlatform(5500, 325),
                 FloatingPlatform(5610, 325), MovingTile(5750, 325), TallPlatform(6500,236),
                 FloatingPlatform(5215, 415), Boost(6800,209)]

    # Setting movement of moving platform
    platforms[4].move_style = "x"
    platforms[4].dist_x_max = 300
    platforms[4].dist_x = 300
    platforms[4].speed = 3

    platforms[1].move_style = "y"
    platforms[1].dist_y_max = 495
    platforms[1].dist_y = 495
    platforms[1].speed = 3

    platforms[24].move_style = "x"
    platforms[24].dist_x_max = 470
    platforms[24].dist_x = 470
    platforms[24].speed = 3


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
    platforms[17].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[18].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[19].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[20].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[21].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[22].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[23].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[24].load_anim(IMAGES_PATH + "Tilesets/level_2/moving_tile.png")
    platforms[25].load_anim(IMAGES_PATH + "Tilesets/level_2/tall_platform.png")
    platforms[26].load_anim(IMAGES_PATH + "Tilesets/level_2/platform.png")
    platforms[27].load_anim(IMAGES_PATH + "Tilesets/heal.png")


    # loading The end portal
    portal = Endgate(6900, 106)
    portal.load_anim(IMAGES_PATH + "Tilesets/endgate.png")

    # Making the backdrop
    background = [BackDrop(), BackDrop()]

    # Loading the images for the backdrop
    background[0].load_anim(IMAGES_PATH + "Background/level_2/bg_bottom.png")
    background[1].load_anim(IMAGES_PATH + "Background/level_2/bg_top.png")

    # Setting up Enemy
    enemies = [Virus1(x=400, y=500), Virus1(x=1000, y=150), Virus2(x=1450, y=475), Virus1(x=2725, y=125),
               Virus2(x=3250, y=110), Virus1(x=4275, y=500), Virus2(x=4900, y=475), Virus1(x=5610, y= 500),
               Virus2(x=6400, y=110)]

    enemies[0].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[0].set_max_distance(200)

    enemies[1].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[1].set_max_distance(100)

    enemies[2].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[2].set_max_distance(200)

    enemies[3].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[3].set_max_distance(100)

    enemies[4].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[4].set_max_distance(200)

    enemies[5].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[5].set_max_distance(100)

    enemies[6].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[6].set_max_distance(200)

    enemies[7].load_anim(IMAGES_PATH + "Characters/Virus/Virus_1/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[7].set_max_distance(100)

    enemies[8].load_anim(IMAGES_PATH + "Characters/Virus/Virus_2/idle.png", IMAGES_PATH + "Projectiles/virus_1_")
    enemies[8].set_max_distance(100)

    return platforms, enemies, background, portal


def level_3():
    man.x, man.y = 50, 50
    platforms = [BasePlatform(1500), MovingTile(3150, 250), FloatingPlatform(1550, 400),
                 FloatingPlatform(650, 250), MovingTile(1300, 350),  Boost(4100, 209),
                 TallPlatform(0, 236), FloatingPlatform(1000, 350),FloatingPlatform(1110, 350),
                 FloatingPlatform(890, 350), FloatingPlatform(1910, 250),
                 FloatingPlatform(2020, 250), BasePlatform(6200), FloatingPlatform(2275, 400),
                 FloatingPlatform(2550, 209), FloatingPlatform(2825, 250), FloatingPlatform(2936, 250),
                 FloatingPlatform(4700, 350), TallPlatform(3750, 236), MovingTile(4350,236),
                 FloatingPlatform(4600, 511), FloatingPlatform(4710, 511), FloatingPlatform(4820, 511),
                 MovingTile(5075, 236), TallPlatform(5250, 236), MovingTile(5825, 236), FloatingPlatform(6325, 236),
                 FloatingPlatform(6550, 350), FloatingPlatform(6850, 400), FloatingPlatform(7000, 250),
                 FloatingPlatform(7110, 250), FloatingPlatform(7220, 250),FloatingPlatform(7330,250),
                 FloatingPlatform(8250, 600), MovingTile(7825,600), MovingTile(8475, 236),
                 TallPlatform(8700, 236), TallPlatform(9240, 236)]

    # Setting movement of moving platform
    platforms[4].move_style = "y"
    platforms[4].dist_y_max = 240
    platforms[4].dist_y = 240
    platforms[4].speed = 3

    platforms[1].move_style = "x"
    platforms[1].dist_x_max = 375
    platforms[1].dist_x = 375
    platforms[1].speed = 3

    platforms[19].move_style = "y"
    platforms[19].dist_y_max = 275
    platforms[19].dist_y = 275
    platforms[19].speed = 3

    platforms[23].move_style = "y"
    platforms[23].dist_y_max = 250
    platforms[23].dist_y = 250
    platforms[23].speed = 3

    platforms[25].move_style = "x"
    platforms[25].dist_x_max = 275
    platforms[25].dist_x = 275
    platforms[25].speed = 3

    platforms[34].move_style = "x"
    platforms[34].dist_x_max = 200
    platforms[34].dist_x = 200
    platforms[34].speed = 3

    platforms[35].move_style = "y"
    platforms[35].dist_y_max = 354
    platforms[35].dist_y = 354
    platforms[35].speed = 3


    # Loading the images for platform
    platforms[0].load_anim(IMAGES_PATH + "Tilesets/level_3/platform_base.png")
    platforms[1].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[2].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[3].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[4].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[5].load_anim(IMAGES_PATH + "Tilesets/heal.png")
    platforms[6].load_anim(IMAGES_PATH + "Tilesets/level_3/tall_platform.png")
    platforms[7].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[8].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[9].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[10].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[11].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[12].load_anim(IMAGES_PATH + "Tilesets/level_3/platform_base.png")
    platforms[13].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[14].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[15].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[16].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[17].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[18].load_anim(IMAGES_PATH + "Tilesets/level_3/tall_platform.png")
    platforms[19].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[20].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[21].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[22].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[23].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[24].load_anim(IMAGES_PATH + "Tilesets/level_3/tall_platform.png")
    platforms[25].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[26].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[27].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[28].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[29].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[30].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[31].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[32].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[33].load_anim(IMAGES_PATH + "Tilesets/level_3/platform.png")
    platforms[34].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[35].load_anim(IMAGES_PATH + "Tilesets/level_3/moving_tile.png")
    platforms[36].load_anim(IMAGES_PATH + "Tilesets/level_3/tall_platform.png")
    platforms[37].load_anim(IMAGES_PATH + "Tilesets/level_3/tall_platform.png")

    #loading The end portal
    portal = Endgate(9700, 105)
    portal.load_anim(IMAGES_PATH + "Tilesets/endgate.png")

    # Making the backdrop
    background = [BackDrop(), BackDrop()]

    # Loading the images for the backdrop
    background[0].load_anim(IMAGES_PATH + "Background/level_1/bg_bottom.png")
    background[1].load_anim(IMAGES_PATH + "Background/level_1/bg_top.png")

    # Setting up Enemy
    enemies = [Virus1(x=1000, y=260), Virus1(x=1600, y=500), Virus2(x=2150, y=500), Virus1(x=2000, y=150),
               Virus1(x=2900, y=150), Virus3(x=3825, y=75), Virus1(x=4700, y=420), Virus3(x=5600, y=75),
               Virus2(x=2850, y=500), Virus3(x=6650, y= 425), Virus1(x=7175, y=150), Virus2(x=8900, y=110)]

    enemies[0].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[0].set_max_distance(200)

    enemies[1].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[1].set_max_distance(100)

    enemies[2].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[2].set_max_distance(250)

    enemies[3].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[3].set_max_distance(100)

    enemies[4].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[4].set_max_distance(100)

    enemies[5].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[5].set_max_distance(200)

    enemies[6].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[6].set_max_distance(100)

    enemies[7].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[7].set_max_distance(150)

    enemies[8].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[8].set_max_distance(200)

    enemies[9].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[9].set_max_distance(200)

    enemies[10].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[10].set_max_distance(100)

    enemies[11].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[11].set_max_distance(200)

    return platforms, enemies, background, portal


def level_4():
    man.x, man.y = 20, 50
    platforms = [BasePlatform(4000), MovingTile(2075, 275), FloatingPlatform(0, 250),
                 FloatingPlatform(6000, 250), MovingTile(225, 250),  Boost(3375, 209), 
                 TallPlatform(850,236), FloatingPlatform(1450, 125),FloatingPlatform(1700, 275),
                 FloatingPlatform(1810, 275), FloatingPlatform(1920, 275), 
                 FloatingPlatform(2625, 275), BasePlatform(8200), FloatingPlatform(2735, 275),
                 FloatingPlatform(3950, 400), FloatingPlatform(3700, 386), FloatingPlatform(4450, 400),
                 FloatingPlatform(4800, 350), TallPlatform(2950, 236), MovingTile(3525, 236),
                 FloatingPlatform(5050, 350), FloatingPlatform(5160, 350), FloatingPlatform(5300,400),
                 FloatingPlatform(5550, 250), FloatingPlatform(5660, 250),
                 TallPlatform(6325, 236), FloatingPlatform(6925, 175), MovingTile(7100, 175),
                 FloatingPlatform(7500, 175), FloatingPlatform(7610, 175), MovingTile(7860, 175),
                 FloatingPlatform(8110, 400),
                 FloatingPlatform(8110, 400), FloatingPlatform(8650, 400), FloatingPlatform(8950, 250),
                 FloatingPlatform(9060, 250), FloatingPlatform(9350, 300), MovingTile(9600, 300),
                 TallPlatform(9950, 236), TallPlatform(10490, 236), Boost(10050, 209),
                 FloatingPlatform(11100, 275), FloatingPlatform(11210, 275), FloatingPlatform(11320, 275)]

    # Setting movement of moving platform
    platforms[4].move_style = "x"
    platforms[4].dist_x_max = 394
    platforms[4].dist_x = 394
    platforms[4].speed = 3

    platforms[1].move_style = "x"
    platforms[1].dist_x_max = 400
    platforms[1].dist_x = 400
    platforms[1].speed = 3

    platforms[19].move_style = "y"
    platforms[19].dist_y_max = 150
    platforms[19].dist_y = 150
    platforms[19].speed = 3

    platforms[27].move_style = "x"
    platforms[27].dist_x_max = 250
    platforms[27].dist_x = 250
    platforms[27].speed = 3

    platforms[30].move_style = "y"
    platforms[30].dist_y_max = 225
    platforms[30].dist_y = 225
    platforms[30].speed = 3

    platforms[36].move_style = "x"
    platforms[36].dist_x_max = 250
    platforms[36].dist_x = 250
    platforms[36].speed = 3


    # Loading the images for platform
    platforms[0].load_anim(IMAGES_PATH + "Tilesets/level_5/platform_base.png")
    platforms[1].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[2].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[3].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[4].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[5].load_anim(IMAGES_PATH + "Tilesets/heal.png")
    platforms[6].load_anim(IMAGES_PATH + "Tilesets/level_5/tall_platform.png")
    platforms[7].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[8].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[9].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[10].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[11].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[12].load_anim(IMAGES_PATH + "Tilesets/level_5/platform_base.png")
    platforms[13].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[14].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[15].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[16].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[17].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[18].load_anim(IMAGES_PATH + "Tilesets/level_5/tall_platform.png")
    platforms[19].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[20].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[21].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[22].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[23].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[24].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[25].load_anim(IMAGES_PATH + "Tilesets/level_5/tall_platform.png")
    platforms[26].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[27].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[28].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[29].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[30].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[31].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[32].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[33].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[34].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[35].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[36].load_anim(IMAGES_PATH + "Tilesets/level_5/moving_tile.png")
    platforms[37].load_anim(IMAGES_PATH + "Tilesets/level_5/tall_platform.png")
    platforms[38].load_anim(IMAGES_PATH + "Tilesets/level_5/tall_platform.png")
    platforms[39].load_anim(IMAGES_PATH + "Tilesets/heal.png")
    platforms[40].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[41].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")
    platforms[42].load_anim(IMAGES_PATH + "Tilesets/level_5/platform.png")





    #loading The end portal
    portal = Endgate(11400, 142)
    portal.load_anim(IMAGES_PATH + "Tilesets/endgate.png")

    # Making the backdrop
    background = [BackDrop(), BackDrop()]

    # Loading the images for the backdrop
    background[0].load_anim(IMAGES_PATH + "Background/level_1/bg_bottom.png")
    background[1].load_anim(IMAGES_PATH + "Background/level_1/bg_top.png")

    # Setting up Enemy
    enemies = [Virus1(x=900, y=125), Virus2(x=1775, y=175), Virus1(x=2735, y=175), Virus4(x=3150, y=75),
               Virus1(x=3975, y=300), Virus2(x=4300, y=500), Virus3(x=4700, y=450), Virus1(x=5100, y=250),
               Virus1(x=5150, y=500), Virus1(x=5660, y=150), Virus2(x=7610, y=75), Virus3(x=6500, y=75),
               Virus2(x=6025, y=150), Virus4(x=8500, y=390), Virus3(x=9060, y=75), Virus2(x=8700, y=500),
               Virus4(x=10450, y=75)]

    enemies[0].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[0].set_max_distance(200)

    enemies[1].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[1].set_max_distance(150)

    enemies[2].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[2].set_max_distance(100)

    enemies[3].load_anim(IMAGES_PATH+"Characters/Virus/Virus_4/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[3].set_max_distance(150)

    enemies[4].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[4].set_max_distance(10)

    enemies[5].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[5].set_max_distance(100)

    enemies[6].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[6].set_max_distance(100)

    enemies[7].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[7].set_max_distance(100)

    enemies[8].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[8].set_max_distance(100)

    enemies[9].load_anim(IMAGES_PATH+"Characters/Virus/Virus_1/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[9].set_max_distance(100)

    enemies[10].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[10].set_max_distance(150)

    enemies[11].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[11].set_max_distance(100)

    enemies[12].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[12].set_max_distance(0)

    enemies[13].load_anim(IMAGES_PATH+"Characters/Virus/Virus_4/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[13].set_max_distance(200)

    enemies[14].load_anim(IMAGES_PATH+"Characters/Virus/Virus_3/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[14].set_max_distance(100)

    enemies[15].load_anim(IMAGES_PATH+"Characters/Virus/Virus_2/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[15].set_max_distance(100)

    enemies[16].load_anim(IMAGES_PATH+"Characters/Virus/Virus_4/idle.png", IMAGES_PATH+"Projectiles/virus_1_")
    enemies[16].set_max_distance(150)




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

LEVELS = [level_1, level_2, level_3, level_4]
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

    main_menu(win)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if LOAD_LEVEL:
            if LEVEL_NUM < 4:
                PLATFORMS, ENEMIES, BACKGROUND, PORTAL = LEVELS[LEVEL_NUM]()
                mission_logger(win)
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
                    if man.current_weapon != 0:
                        man.enemy_killed(ENEMIES, win)
                    hit_player(man, ENEMIES)
                    man.infection_damage()
                    clock.tick(30)
                    redraw(win, BACKGROUND, ENEMIES, PLATFORMS)

        pygame.display.update()


damage_delay = 20


def main_menu(win):
    menu_bg = pygame.image.load(IMAGES_PATH+"Menus/startmenu.png")
    start_button = pygame.image.load(IMAGES_PATH+"Menus/StartButton.png")
    exit_button = pygame.image.load(IMAGES_PATH+"Menus/ExitButton.png")
    help_button = pygame.image.load(IMAGES_PATH+"Menus/HelpButton.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(menu_bg, (0, 0))
        mouse_hover = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if 473 + 256 > mouse_hover[0] > 473 and 300 + 80 > mouse_hover[1] > 300:
            win.blit(start_button, (473, 300), (256, 0, 256, 80))
            if mouse_pressed[0]:
                break
        else:
            win.blit(start_button, (473, 300), (0, 0, 256, 80))

        if 473 + 256 > mouse_hover[0] > 473 and 500 + 80 > mouse_hover[1] > 500:
            win.blit(exit_button, (473, 500), (256, 0, 256, 80))
            if mouse_pressed[0]:
                pygame.quit()
                quit()

        else:
            win.blit(exit_button, (473, 500), (0, 0, 256, 80))

        if 473 + 256 > mouse_hover[0] > 473 and 400 + 80 > mouse_hover[1] > 400:
            win.blit(help_button, (473, 400), (256, 0, 256, 80))
            if mouse_pressed[0]:
                get_help()
        else:
            win.blit(help_button, (473, 400), (0, 0, 256, 80))

        pygame.display.update()


def mission_logger(win):

    global LEVEL_NUM
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            break

        win.blit(mission_log, (0, 0), (1200*LEVEL_NUM, 0, 1200, 640))
        clock.tick(30)
        pygame.display.update()


def get_help():
    image = pygame.image.load(IMAGES_PATH+"Menus/help.png")
    pages_max = 5
    pages = 0
    cooldown = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        mouse_hover = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        win.blit(image, (0, 0), (1200*pages, 0, 1200, 640))

        if cooldown <= 0:
            cooldown = 2
            if 1019 + 105 > mouse_hover[0] > 1019 and 497 + 105 > mouse_hover[1] > 497:
                if mouse_pressed[0] and pages < pages_max:
                    pages += 1

            if 49 + 105 > mouse_hover[0] > 49 and 497 + 105 > mouse_hover[1] > 497:
                if mouse_pressed[0] and pages > 0:
                    pages -= 1

            if keys[pygame.K_RIGHT] and pages < pages_max:
                pages += 1

            if keys[pygame.K_LEFT] and pages > 0:
                pages -= 1

        else:
            cooldown -= 1

        if keys[pygame.K_ESCAPE]:
            break

        clock.tick(30)
        pygame.display.update()


# draw function
def redraw(win, background, enemies, platforms):

    global DAMAGED
    global WARN
    global damage_delay
    win.fill((104, 98, 112))

    for layer in background:
        layer.draw(win)

    man.draw(win, platforms)
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
        enemy.update_bullets(win, platforms)

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
        win.blit(pause_screen, (500, 250))
        text = font_20.render("Game Paused ", 1, (0, 0, 0))
        text2 = font.render("press c to continue", 1, (0, 0, 0))
        win.blit(text, (600, 300))
        win.blit(text2, (600, 320))

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
