import os
import pygame


class Weapons:

    # Variables
    ammo_limit = 100
    ammo = 100
    hold_limit = 25
    on_load = 25

    def __init__(self):
        self.anim = None

    # ammo firing function
    def fire(self):
        self.ammo -= 1

    # Reloading ammo function
    def reload(self):
        self.ammo -= self.hold_limit - self.on_load

    # Loading ammo function
    def load_ammo(self, bullets):
        self.ammo += bullets
        if self.ammo > self.ammo_limit:
            self.ammo = self.ammo_limit

    # Load animations
    def load_anim(self, path):
        self.anim = pygame.image.load(path)
