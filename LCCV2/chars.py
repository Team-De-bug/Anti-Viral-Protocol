import pygame
import LCCV2.guns as guns


# Entity class for all characters
class Entity:

    # Default variables
    hp = 100
    facing = None
    speed = 10

    width = 50
    height = 50

    def __init__(self, x, y):

        # Getting the character location setup
        self.x = x
        self.y = y

    # Taking health away
    def hurt(self, damage):
        self.hp -= damage

    # Getting health
    def re_gen(self, hp):
        self.hp += hp


class Enemy(Entity):

    # Variables
    points = 100
    hit = 5

    # Class initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # load anim_function
    def load_anim(self, path):
        self.idle = pygame.image.load(path)
        self.moving = pygame.image.load(path)
        self.attack = pygame.image.load(path)

    # Move function fall back
    def move(self):
        pass

    # Draw method fallback
    def draw(self):
        pass


# Main player class
class Player(Entity):

    height = 128
    speed = 10
    vel = 20
    jumping = False
    on_platform = False
    weapon_list = ["none", "pistol", "shotgun", "RPG", "AR"]  # ["none", "pistol", "shotgun", "RPG", "AR"]
    current_weapon = 0
    weapons = {}

    # Init guns
    def init_guns(self):
        # making the gun instances
        self.weapons["none"] = None
        self.weapons["pistol"] = guns.Pistol()
        self.weapons["shotgun"] = guns.Shotgun()
        self.weapons["RPG"] = guns.RocketLauncher()
        self.weapons["AR"] = guns.MachineGun()

        # loading the gun animations
        self.weapons["pistol"].load_anim("resources/Images/Characters/Player/Weilding_Pistol_Idle/Weilding_Pistol.png")
        self.weapons["shotgun"].load_anim("resources/Images/Characters/Player/Weilding_Shotgun_Idle/Weilding_Shotgun.png")
        self.weapons["RPG"].load_anim("resources/Images/Characters/Player/Weilding_RPG_Idle/Weilding_RPG.png")
        self.weapons["AR"].load_anim("resources/Images/Characters/Player/Weilding_AR_Idle/Weilding_AR.png")

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim = pygame.image.load(path)
        '''
        self.anim = {"idle_L": [], "jumping_L": [], "running_L": [],
                     "idle_R": [], "jumping_R": [], "running_R": []}
        '''
    # Moving control
    def move(self, keys, platforms):

        if keys[pygame.K_d]:

            if keys[pygame.K_LSHIFT]:
                self.speed = 15

            else:
                self.speed = 10

            collision_x = None
            collision_y = None
            self.facing = "right"

            for platform in platforms:
                collision_x = [(self.x + self.width) > platform.x > self.x,
                               (self.x + self.width) > platform.x + platform.width > self.x]
                collision_y = [(self.y + self.height) > platform.y > self.y,
                               (self.y + self.height) > platform.y + platform.height > self.y]

                if (collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1]):
                    break

            if not ((collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1])):
                if self.x < 650:
                    self.x += self.speed

                else:
                    for platform in platforms:
                        platform.scrollx(self.speed, -1)

        elif keys[pygame.K_a]:

            if keys[pygame.K_LSHIFT]:
                self.speed = 15

            else:
                self.speed = 10

            collision_x = None
            collision_y = None
            self.facing = "left"

            for platform in platforms:
                collision_x = [(self.x + self.width) > platform.x > self.x,
                               (self.x + self.width) > platform.x + platform.width > self.x]
                collision_y = [(self.y + self.height) > platform.y > self.y,
                               (self.y + self.height) > platform.y + platform.height > self.y]

                if (collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1]):
                    break

            if not ((collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1])):
                if self.x > 200:
                    self.x -= self.speed

                else:
                    for platform in platforms:
                        platform.scrollx(self.speed, 1)

        if keys[pygame.K_w] and self.on_platform:
            if not self.jumping:
                self.vel = 20
                self.jumping = True

        if self.jumping and self.vel > 0:
            self.y -= self.vel
            self.vel -= 1

        elif self.jumping and self.vel <= 0:
            self.jumping = False

        if not self.on_platform and not self.jumping:
            self.y += self.vel
            self.vel += 1

        if self.jumping:
            for platform in platforms:
                if (platform.x + platform.width > self.x > platform.x) or (platform.x + platform.width > self.x + self.width> platform.x):
                    if platform.y + platform.height > self.y > platform.y:
                        self.vel = 0
                        break

    def on_ground(self, platforms):

        for platform in platforms:
            x_on_platform = platform.x + platform.width > self.x > platform.x or platform.x + platform.width > (self.x + self.width) > platform.x
            if (platform.y + platform.height) > (self.y + self.height) >= platform.y and x_on_platform:
                self.on_platform = True
                self.vel = 0
                self.y = platform.y - self.height
                break

            else:
                self.on_platform = False

    # Changing weapon function
    def change_weapon(self, keys):

        if keys[pygame.K_1]:
            self.current_weapon = 0

        if keys[pygame.K_2]:
            self.current_weapon = 1

        if keys[pygame.K_3]:
            self.current_weapon = 2

        if keys[pygame.K_4]:
            self.current_weapon = 4

        if keys[pygame.K_5]:
            self.current_weapon = 3

    # rendering function
    def draw(self, win):
        if not self.weapons[self.weapon_list[self.current_weapon]]:
            win.blit(self.anim, (self.x, self.y))

        else:
            win.blit(self.weapons[self.weapon_list[self.current_weapon]].anim, (self.x, self.y))
