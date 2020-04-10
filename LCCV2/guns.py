from items import Weapons
import shells
import pygame


# Pistol
class Pistol(Weapons):
    ammo_limit = 35
    ammo_count = 35
    hold_limit = 7
    on_load = 7
    cooldown = 5
    ammo = shells.PistolShells


# Shotgun
class Shotgun(Weapons):
    ammo_limit = 25
    ammo_count = 25
    hold_limit = 5
    on_load = 5
    cooldown = 20
    ammo = shells.ShotShells


# Machine-gun
class MachineGun(Weapons):
    ammo_limit = 90
    ammo_count = 90
    hold_limit = 30
    on_load = 30
    cooldown = 2
    ammo = shells.ARShells


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo_limit = 50
    ammo_count = 50
    hold_limit = 5
    on_load = 5
    cooldown = 60
    ammo = shells.RPGShells
    explode_img = pygame.image.load("resources/Images/Projectiles/explosion.png")

    def update_bullets(self, win, double=False):
        for ammo in self.ammo_list:
            if ammo.dist < ammo.dist_limit and not ammo.exploded:
                ammo.move()
                ammo.draw(win, double)
            else:
                self.explode(ammo, win)

    def explode(self, ammo, win):
        ammo.exploded = True
        ammo.vel = 0
        if ammo.explode_delay <= 0:
            ammo.explode_delay = 4
            if ammo.explode_stage < 5:
                ammo.explode_stage += 1
            else:
                self.ammo_list.pop(self.ammo_list.index(ammo))
        else:
            ammo.explode_delay -= 1

        win.blit(self.explode_img, (ammo.x, ammo.y), (32 * ammo.explode_stage, 0, 32, 32))
