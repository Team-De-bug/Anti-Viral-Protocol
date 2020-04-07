import pygame
import LCCV2.guns as guns

IMAGE_PATH = "resources/Images/"

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
    dist_max = 50
    dist = 50
    dir_x = True

    # Class initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_player = False

    # load anim_function
    def load_anim(self, path):
        self.anim = pygame.image.load(path)
        #self.moving = pygame.image.load(path)
        #self.attack = pygame.image.load(path)

    # Move function fall back

    def move(self, speed, player):
        check_y = [player.y + player.height > self.y > player.y,
                   player.y + player.height > self.y + self.width > player.y]

        if 0 < abs(player.x - self.x) < 10:
            self.on_player = True
        else:
            self.on_player = False

        if not ((0 < abs(player.x - self.x) < 300) and (check_y[0] or check_y[1])):

            if self.dir_x:
                self.x += speed
                self.dist -= speed

            else:
                self.x -= speed
                self.dist += speed

            if self.dist > self.dist_max:
                self.dir_x = True

            elif self.dist < 0:
                self.dir_x = False

        else:

            if not self.on_player:
                if self.x > player.x:
                    self.x -= speed

                else:
                    self.x += speed

    # Draw method fallback
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))

    def scroll_x(self, speed, direction):
        self.x += speed * direction

    def set_max_distance(self, dist):
        self.dist_max = dist
        self.dist = dist


# Main player class
class Player(Entity):

    height = 128
    width = 50
    width_var = [24, 42, 78]
    width_num = 0
    speed = 8
    vel = 20
    hit_x = [33, 24, 10]

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
        self.collision_x = None
        self.collision_y = None
        self.w_cool_down = 0
        self.fired = False
        self.score = 0

    # Init guns
    def init_guns(self):
        # making the gun instances
        self.weapons["none"] = None
        self.weapons["pistol"] = guns.Pistol()
        self.weapons["shotgun"] = guns.Shotgun()
        self.weapons["RPG"] = guns.RocketLauncher()
        self.weapons["AR"] = guns.MachineGun()

        # loading the gun animations
        self.weapons["pistol"].load_anim(IMAGE_PATH + "Characters/Player/Pistol/idle_R.png",
                                         IMAGE_PATH + "Projectiles/pistol.png")
        self.weapons["shotgun"].load_anim(IMAGE_PATH + "Characters/Player/Shotgun/idle_R.png",
                                          IMAGE_PATH + "Projectiles/shotgun.png")
        self.weapons["RPG"].load_anim(IMAGE_PATH + "Characters/Player/RPG/idle_R.png",
                                      IMAGE_PATH + "Ammo/bullet_basic.png")
        self.weapons["AR"].load_anim(IMAGE_PATH + "Characters/Player/AR/idle_R.png",
                                     IMAGE_PATH + "Ammo/bullet_basic.png")

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim["idle_R"] = pygame.image.load(path+"no_weapons/idle_R.png")
        self.anim["walking_R"] = pygame.image.load(path+"no_weapons/walking_R.png")
        self.anim["idle_L"] = pygame.image.load(path+"no_weapons/idle_L.png")
        self.anim["walking_L"] = pygame.image.load(path+"no_weapons/walking_L.png")

    # Moving control
    def move(self, keys, platforms, enemies, bg_layers):

        # Update hitbox
        frame_num = self.frame % 8
        if frame_num in [1, 5]:
            self.width_num = 0

        if frame_num in [2, 4, 6, 8]:
            self.width_num = 1

        if frame_num in [3, 7]:
            self.width_num = 2

        # firing cool down
        if self.current_weapon > 0 and self.fired:
            if self.w_cool_down < self.weapons[self.weapon_list[self.current_weapon]].cooldown:
                self.w_cool_down += 1

            else:
                self.fired = False
                self.w_cool_down = 0

        # Updating the collisions
        for platform in platforms:

            self.collision_x = [(platform.x + platform.width) > self.x + self.hit_x[self.width_num] > platform.x,
                                (platform.x + platform.width) > (self.x + self.hit_x[self.width_num] + self.width_var[self.width_num]) > platform.x,
                                self.x + self.hit_x[self.width_num] + self.width > platform.x > self.x,
                                self.x + self.hit_x[self.width_num] + self.width > platform.x + platform.width > self.x]

            self.collision_y = [(platform.y + platform.height) > self.y > platform.y,
                                (platform.y + platform.height) > (self.y + self.height) > platform.y,
                                (self.y + self.height) > platform.y > self.y,
                                (self.y + self.height) > (platform.y + platform.height) > self.y]

            if (self.collision_x[0] or self.collision_x[1]) and (self.collision_y[0] or self.collision_y[1]):
                break

        # increase speed if L_shift key is pressed
        if keys[pygame.K_LSHIFT]:
            self.speed = 15

        else:
            self.speed = 8

        # move right
        if keys[pygame.K_d]:

            # setting the character facing direction
            self.direction = "R"

            # checking for collisions
            if not ((self.collision_x[0] or self.collision_x[1]) and (self.collision_y[0] or self.collision_y[1])):

                # selecting the background images for scorlling
                top = bg_layers[0]
                bottom = bg_layers[1]

                # Checking wether to scroll or move the player
                if self.x < 650:
                    self.x += self.speed

                # scrolling
                else:
                    for platform in platforms:
                        platform.scroll_x(self.speed, -1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, -1)

                    top.scroll_x(self.speed / 2, -1)
                    bottom.scroll_x(self.speed / 4, -1)
                    if self.current_weapon != 0:
                        self.weapons[self.weapon_list[self.current_weapon]].scroll_bullets(self.speed, -1)

                if self.on_platform:
                    self.status_num = 1
                    if self.frame_time < self.frame_timer:
                        self.frame_time += 1

                    else:
                        self.frame_time = 0
                        self.frame += 1

                # updating frame and hitbox
                else:
                    self.width_num = 0
                    self.status_num = 0

        elif keys[pygame.K_a]:

            # setting the facing direction
            self.direction = "L"

            # checking for collision
            if not ((self.collision_x[0] or self.collision_x[1]) and (self.collision_y[0] or self.collision_y[1])):

                top = bg_layers[0]
                bottom = bg_layers[1]

                # checking wether to scroll or move the player
                if self.x > 200:
                    self.x -= self.speed

                # scrolling
                else:
                    for platform in platforms:
                        platform.scroll_x(self.speed, 1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, 1)

                    top.scroll_x(self.speed/2, 1)
                    bottom.scroll_x(self.speed/4, 1)

                    if self.current_weapon != 0:
                        self.weapons[self.weapon_list[self.current_weapon]].scroll_bullets(self.speed, 1)

                # Updating the character animation
                if self.on_platform:
                    self.status_num = 1
                    if self.frame_time < self.frame_timer:
                        self.frame_time += 1

                    else:
                        self.frame_time = 0
                        self.frame += 1

                # updating frame and hitbox
                else:
                    self.status_num = 0
                    self.width_num = 0

        # updating frame and hitbox
        else:
            self.status_num = 0
            self.width_num = 0

        # checking for starting the jump
        if keys[pygame.K_w] and self.on_platform:
            if not self.jumping:
                self.vel = 20
                self.jumping = True

        if self.jumping and self.vel > 0:
            self.y -= self.vel
            self.vel -= 1

        elif self.jumping and self.vel <= 0:
            self.jumping = False

        # falling
        if not self.on_platform and not self.jumping:
            self.y += self.vel
            self.vel += 1

        # Jumping
        if self.jumping:
            if self.collision_x[0] or self.collision_x[1] or self.collision_x[2] or self.collision_x[3]:
                if self.collision_y[0] or self.collision_y[2]:
                    self.vel = 0
                    self.frame = 0

        # moving the character if on a moving platform
        if self.on_moving_platform and self.platform.move_style == "x":
            self.x += self.platform.moving_speed * self.plat_move_dir

        if self.on_moving_platform and self.platform.move_style == "y":
            self.y += self.platform.moving_speed * self.plat_move_dir

        # Firing weapon
        if self.current_weapon != 0:
            bull_num = len(self.weapons[self.weapon_list[self.current_weapon]].ammo_list)
        else:
            bull_num = 0

        if keys[pygame.K_SPACE] and self.current_weapon > 0 and bull_num < 5 and self.w_cool_down == 0:
            self.fired = True
            if self.direction == "R":
                direction = 1
                width = self.width * 3/2

            else:
                direction = -1
                width = 0
            self.weapons[self.weapon_list[self.current_weapon]].fire(self.x+width, self.y+40, direction)


    # checking for being on platform
    def on_ground(self, platforms):

        for platform in platforms:
            x_on_platform = platform.x + platform.width > self.x + self.hit_x[self.width_num] > platform.x or platform.x + platform.width > (self.x + self.hit_x[self.width_num] + self.width_var[self.width_num]) > platform.x
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
            #pygame.draw.rect(win, (255, 255, 255),
            #                 [self.x + self.hit_x[self.width_num], self.y, self.width_var[self.width_num], self.height], 1)
            if self.status_num == 0:
                win.blit(self.anim[self.status[self.status_num] + self.direction], (self.x, self.y),
                         (0, 0, self.width * 2, self.height))

            else:
                win.blit(self.anim[self.status[self.status_num]+self.direction], (self.x, self.y),
                         self.frames[self.width_num])

        else:
            win.blit(self.weapons[self.weapon_list[self.current_weapon]].anim,
                     (self.x, self.y), (0, 0, self.width * 2, self.height))

            self.weapons[self.weapon_list[self.current_weapon]].update_bullets(win)
