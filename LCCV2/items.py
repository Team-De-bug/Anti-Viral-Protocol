import pygame


class Weapons:

    # Variables
    ammo_limit = 100
    ammo_count = 100
    hold_limit = 25
    on_load = 25
    cooldown = 0
    cooldown_max = 3
    fired = False

    ammo = None

    # Initializing the weapons
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
        if self.on_load <= 0:
            if self.hold_limit > self.on_load >= 0:
                if self.ammo_count >= self.hold_limit:
                    self.ammo_count -= self.hold_limit - self.on_load
                    self.on_load = self.hold_limit
                else:
                    if self.ammo_count > 0:
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

    # updating the on screen bullets
    def update_bullets(self, win, platforms, double=False):

        for ammo in self.ammo_list:
            on_x, on_y = ammo.check_collision(platforms)
            if ammo.dist < ammo.dist_limit and not(on_x and on_y):
                ammo.move()
                ammo.draw(win, double)
            else:
                self.ammo_list.pop(self.ammo_list.index(ammo))

    # scrolling the bullets as the player walks
    def scroll_bullets(self, vel, direction):
        for ammo in self.ammo_list:
            ammo.scroll_x(vel, direction)


# Shells/Bullets class
class Shells:

    dist_limit = 1000
    damage = 10
    vel = 30
    width = 20
    height = 10

    # Setting up the bullet loc
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dist = 0
        self.direction = direction

    # Loading the animation function
    @classmethod
    def load_anim(cls, path):

        cls.anim = [pygame.image.load(path + "L.png"),
                    pygame.image.load(path + "R.png"),
                    pygame.image.load(path + "2x_R.png"),
                    pygame.image.load(path + "2x_L.png")]

    # Scrolling function
    def scroll_x(self, vel, direction):
        self.x += vel * direction

    # Moving the bullet in the fired direction
    def move(self):
        if self.dist < self.dist_limit:
            self.x += self.vel * self.direction
            self.dist += self.vel

    # Drawing the bullet on screen
    def draw(self, win, double):

        # Checking if double damage is on
        if double:
            if self.direction > 0:
                win.blit(self.anim[2], (self.x, self.y))
            else:
                win.blit(self.anim[3], (self.x, self.y))

        else:
            if self.direction > 0:
                win.blit(self.anim[1], (self.x, self.y))
            else:
                win.blit(self.anim[0], (self.x, self.y))

    # Checking for collision with platforms
    def check_collision(self, platforms):
        on_x = None
        on_y = None
        for platform in platforms:
            on_x = platform.x + platform.width > self.x > platform.x
            on_y = platform.y + platform.height > self.y > platform.y
            if on_x and on_y:
                break

        return on_x, on_y
