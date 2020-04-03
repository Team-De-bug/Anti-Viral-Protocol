import pygame


class Weapons:

    # Variables
    ammo = 100
    hold_limit = 25
    on_load = 25
    width = 10
    height = 10

    # Initializer
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, self.width, self.height)

    # update location
    def update_loc(self, x, y):
        self.x = x
        self.y = y

    # update hitbox
    def update_hitbox(self):
        self.hitbox = (self.x, self.y, self.width, self.height)

    # Animation loader
    @classmethod
    def load_anim(cls, path):
        cls.anim = pygame.image.load(path)

    # ammo firing function
    def fire(self):
        self.ammo -= 1

    # Loading ammo func
    def load(self):
        self.ammo -= self.hold_limit - self.on_load

    # draw method fallback
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))
