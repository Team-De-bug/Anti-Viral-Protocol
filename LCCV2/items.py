import pygame


class Weapons:

    # Variables
    ammo_limit = 100
    ammo_count = 100
    hold_limit = 25
    on_load = 25
    cooldown = 3

    ammo = None

    def __init__(self):
        self.ammo_list = []
        self.anim = {}

    # ammo firing function
    def fire(self, x, y, direction):
        if self.on_load > 0:
            self.on_load -= 1
            self.sound.play()
            self.ammo_list.append(self.ammo(x, y, direction))

    # Reloading ammo function
    def reload(self):
        if self.on_load >= 0:
            if self.ammo_count > self.hold_limit:
                self.ammo_count -= self.hold_limit - self.on_load
                self.on_load = self.hold_limit
            else:
                self.on_load = self.ammo_count
                self.ammo_count = 0

    # Loading ammo function
    def load_ammo(self, bullets):
        self.ammo_count += bullets
        if self.ammo_count > self.ammo_limit:
            self.ammo_count = self.ammo_limit

    # Load animations
    def load_anim(self, path, ammo_path, sound):
        self.anim["idle_R"] = pygame.image.load(path+"idle_R.png")
        self.anim["walking_R"] = pygame.image.load(path+"walking_R.png")
        self.anim["idle_L"] = pygame.image.load(path+"idle_L.png")
        self.anim["walking_L"] = pygame.image.load(path+"walking_L.png")

        self.ammo.load_anim(ammo_path)
        self.sound = pygame.mixer.Sound(sound)

    def update_bullets(self, win):
        for ammo in self.ammo_list:
            if ammo.dist < ammo.dist_limit:
                ammo.move()
                ammo.draw(win)
            else:
                self.ammo_list.pop(self.ammo_list.index(ammo))

    def scroll_bullets(self, vel, direction):
        for ammo in self.ammo_list:
            ammo.scroll_x(vel, direction)


class Shells:

    dist_limit = 1000
    damage = 10
    vel = 30
    width = 20
    height = 10

    # setting up the bullet loc
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dist = 0
        self.direction = direction

    # animation loader function
    @classmethod
    def load_anim(cls, path):

        cls.anim = [pygame.image.load(path + "L.png"),
                    pygame.image.load(path + "R.png")]

    # scrolling function
    def scroll_x(self, vel, direction):
        self.x += vel * direction

    def move(self):
        if self.dist < self.dist_limit:
            self.x += self.vel * self.direction
            self.dist += self.vel

    def draw(self, win):
        if self.direction > 0:
            win.blit(self.anim[1], (self.x, self.y))
        else:
            win.blit(self.anim[0], (self.x, self.y))