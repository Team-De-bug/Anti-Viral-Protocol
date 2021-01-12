import os
import pygame
from . import shells
from .items import Weapons

# Setting up the mixer for sounds
pygame.mixer.init()

# Working file paths
BASE_PATH = os.path.dirname(__file__)
RES_PATH = os.path.join(BASE_PATH, 'resources/')


# Pistol
class Pistol(Weapons):
    ammo_limit = 35
    ammo_count = 35
    hold_limit = 7
    on_load = 7
    cooldown_max = 5
    ammo = shells.PistolShells


# Shotgun
class Shotgun(Weapons):
    ammo_limit = 25
    ammo_count = 25
    hold_limit = 5
    on_load = 5
    cooldown_max = 20
    ammo = shells.ShotShells


# Machine-gun
class MachineGun(Weapons):
    ammo_limit = 90
    ammo_count = 90
    hold_limit = 30
    on_load = 30
    cooldown_max = 2
    ammo = shells.ARShells


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo_limit = 50
    ammo_count = 50
    hold_limit = 5
    on_load = 5
    cooldown_max = 60
    ammo = shells.RPGShells
    explode_img = pygame.image.load(RES_PATH + "/Images/Projectiles/explosion.png")
    explode_sound = pygame.mixer.Sound(RES_PATH + "/Sounds/Explode.wav")

    # Overreide for update bullets function
    def update_bullets(self, win, platforms, double=False):
        for ammo in self.ammo_list:
            on_x, on_y = ammo.check_collision(platforms)
            if ammo.dist < ammo.dist_limit and not (on_x and on_y) and not ammo.exploded:
                ammo.move()
                ammo.draw(win, double)
            else:
                self.explode(ammo, win)

    # function to play the explosion image and sounds
    def explode(self, ammo, win):
        ammo.exploded = True
        ammo.vel = 0
        if not ammo.explode_played:
            ammo.explode_played = True
            self.explode_sound.play()

        if ammo.explode_delay <= 0:
            ammo.explode_delay = 4
            if ammo.explode_stage < 5:
                ammo.explode_stage += 1
            else:
                self.ammo_list.pop(self.ammo_list.index(ammo))
        else:
            ammo.explode_delay -= 1

        win.blit(self.explode_img, (ammo.x, ammo.y - 30), (128 * ammo.explode_stage, 0, 128, 128))
