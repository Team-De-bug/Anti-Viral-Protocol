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
        # empty hand animations
        self.anim = pygame.image.load(path)
        #self.anim["walking_R"] = pygame.image.load(path+"no_weapons/walking_R.png")
        #self.anim["idle_L"] = pygame.image.load(path+"no_weapons/idle_L.png")
        #self.anim["walking_L"] = pygame.image.load(path+"no_weapons/walking_L.png")


class Shells:

    dist_limit = 300
    damage = 10

    # setting up the bullet loc
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.anim = None
        self.dist = 0

    # animation loader function
    def load_anim(self, path):
        self.anim = pygame.image.load(path)

    # scrolling function
    def scroll_x(self, vel, direction):
        self.x += vel * direction

    def move(self, vel):
        if self.dist < self.dist_limit:
            self.x += vel
            self.dist += vel
