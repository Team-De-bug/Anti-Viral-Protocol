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
        self.anim = pygame.image.load(path)
        #self.moving = pygame.image.load(path)
        #self.attack = pygame.image.load(path)

    # Move function fall back
    def move(self):
        pass

    # Draw method fallback
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))

    def scroll_x(self, speed, dir):
        self.x += speed * dir


# Main player class
class Player(Entity):

    height = 128
    width = 70
    speed = 8
    vel = 20

    weapons = {}
    anim = {}

    frames = [(0, 0, 128, 128), (129, 0, 128, 128), (259, 0, 128, 128), (385, 0, 128, 128),
              (513, 0, 128, 128), (641, 0, 128, 128), (769, 0, 128, 128), (897, 0, 128, 128)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = ["idle_", "walking_"]
        self.current_weapon = 0
        self.weapon_list = ["none", "pistol", "shotgun", "RPG", "AR"]  # ["none", "pistol", "shotgun", "RPG", "AR"]
        self.jumping = False
        self.on_platform = False
        self.status_num = 0
        self.on_moving_platform = False
        self.plat_move_dir = 1
        self.platform = None
        self.direction = "R"
        self.frame = 0
        self.frame_timer = 3
        self.frame_time = 0


    # Init guns
    def init_guns(self):
        # making the gun instances
        self.weapons["none"] = None
        self.weapons["pistol"] = guns.Pistol()
        self.weapons["shotgun"] = guns.Shotgun()
        self.weapons["RPG"] = guns.RocketLauncher()
        self.weapons["AR"] = guns.MachineGun()

        # loading the gun animations
        self.weapons["pistol"].load_anim("resources/Images/Characters/Player/Pistol/idle_R.png")
        self.weapons["shotgun"].load_anim("resources/Images/Characters/Player/Shotgun/idle_R.png")
        self.weapons["RPG"].load_anim("resources/Images/Characters/Player/RPG/idle_R.png")
        self.weapons["AR"].load_anim("resources/Images/Characters/Player/AR/idle_R.png")

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim["idle_R"] = pygame.image.load(path+"no_weapons/idle_R.png")
        self.anim["walking_R"] = pygame.image.load(path+"no_weapons/walking_R.png")
        self.anim["idle_L"] = pygame.image.load(path+"no_weapons/idle_L.png")
        self.anim["walking_L"] = pygame.image.load(path+"no_weapons/walking_L.png")

    # Moving control
    def move(self, keys, platforms, enemies):

        if keys[pygame.K_d]:

            if keys[pygame.K_LSHIFT]:
                self.speed = 15

            else:
                self.speed = 8

            collision_x = None
            collision_y = None
            self.direction = "R"
            self.status_num = 1

            for platform in platforms:
                collision_x = [(platform.x + platform.width) > self.x > platform.x,
                               (platform.x + platform.width) > (self.x + self.width) > platform.x]
                collision_y = [(platform.y + platform.height) > self.y > platform.y,
                               (platform.y + platform.height) > (self.y + self.height) > platform.y]

                if (collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1]):
                    break

            if not ((collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1])):
                if self.x < 650:
                    self.x += self.speed

                else:
                    for platform in platforms:
                        platform.scrollx(self.speed, -1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, -1)

                if self.frame_time < self.frame_timer:
                    self.frame_time += 1

                else:
                    self.frame_time = 0
                    self.frame += 1

        elif keys[pygame.K_a]:

            if keys[pygame.K_LSHIFT]:
                self.speed = 15

            else:
                self.speed = 8

            collision_x = None
            collision_y = None
            self.direction = "L"
            self.status_num = 1

            for platform in platforms:

                collision_x = [(platform.x + platform.width) > self.x > platform.x,
                               (platform.x + platform.width) > (self.x + self.width) > platform.x]
                collision_y = [(platform.y + platform.height) > self.y > platform.y,
                               (platform.y + platform.height) > (self.y + self.height) > platform.y]

                if (collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1]):
                    break

            if not ((collision_x[0] or collision_x[1]) and (collision_y[0] or collision_y[1])):
                if self.x > 200:
                    self.x -= self.speed

                else:
                    for platform in platforms:
                        platform.scrollx(self.speed, 1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, 1)

                if self.frame_time < self.frame_timer:
                    self.frame_time += 1

                else:
                    self.frame_time = 0
                    self.frame += 1

        else:
            self.status_num = 0

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
                        self.frame = 0
                        break

        if self.on_moving_platform and self.platform.move_style == "x":
            self.x += self.platform.moving_speed * self.plat_move_dir

        if self.on_moving_platform and self.platform.move_style == "y":
            self.y += self.platform.moving_speed * self.plat_move_dir


    # checking for being on platform
    def on_ground(self, platforms):

        for platform in platforms:
            x_on_platform = platform.x + platform.width > self.x > platform.x or platform.x + platform.width > (self.x + self.width) > platform.x
            if (platform.y + platform.height) > (self.y + self.height) >= platform.y and x_on_platform:
                self.on_platform = True
                self.vel = 0
                self.y = platform.y - self.height
                if platform.is_moving:
                    self.on_moving_platform = True
                    self.plat_move_dir = platform.moving_dir
                    self.platform = platform
                else:
                    self.on_moving_platform = False

                break

            else:
                self.on_moving_platform = False
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
            if self.status_num == 0:
                win.blit(self.anim[self.status[self.status_num] + self.direction], (self.x, self.y),
                         (0, 0, self.width, self.height))

            else:
                win.blit(self.anim[self.status[self.status_num]+self.direction], (self.x, self.y),
                         self.frames[self.frame%8])

        else:
            win.blit(self.weapons[self.weapon_list[self.current_weapon]].anim,
                     (self.x, self.y), (0, 0, self.width * 2, self.height))
