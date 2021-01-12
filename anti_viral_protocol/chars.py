from . import guns
import pygame
import os

# Working file paths
BASE_PATH = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(BASE_PATH, 'resources/Images/')


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
    ammo = None
    damage = 15
    health_max = 100

    cooldown = 30

    # Class initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_player = False
        self.ammo_list = []
        self.meele_cooldown = 0
        self.Tracking = False

    # load anim_function
    def load_anim(self, path, ammo_path):
        self.anim = pygame.image.load(path)
        self.ammo.load_anim(ammo_path)

    # Move function fall back
    def move(self, speed, player):
        check_y = [player.y + player.height > self.y > player.y,
                   player.y + player.height > self.y + self.width > player.y]

        # checking if on the player
        if 0 < abs(player.x - self.x) < 10:
            self.on_player = True
        else:
            self.on_player = False

        # Checking if player not in range or tracking is disabled
        if (not ((0 < abs(player.x - self.x) < 400) and (check_y[0] or check_y[1]))) or (not self.Tracking):

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
            # if tracking enabled then go towards player
            if not self.on_player and self.Tracking:
                if self.x > player.x:
                    self.x -= speed

                else:
                    self.x += speed

        # checking if player is in firing range
        if (200 < player.x - self.x < 400) or (200 < self.x - player.x < 400) and (check_y[0] or check_y[1]):
            if self.x > player.x:
                self.fire(self.x + self.width / 2, self.y + self.height / 2, -1)
            else:
                self.fire(self.x + self.width / 2, self.y + self.height / 2, 1)

    # Draw method for the enemies
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))

    # scroll funnction
    def scroll_x(self, speed, direction):
        self.x += speed * direction

    # function to set the max patrolling distance
    def set_max_distance(self, dist):
        self.dist_max = dist
        self.dist = dist

    # function to update bullets fired by the enemies
    def update_bullets(self, win, platforms):
        for ammo in self.ammo_list:
            on_x, on_y = ammo.check_collision(platforms)
            if ammo.dist < ammo.dist_limit and not (on_x and on_y):
                ammo.move()
                ammo.draw(win)
            else:
                self.ammo_list.pop(self.ammo_list.index(ammo))

    # function to scroll enemy bullets
    def scroll_bullets(self, vel, direction):
        for ammo in self.ammo_list:
            ammo.scroll_x(vel, direction)

    # Fire function for enemy to fire bullets
    def fire(self, x, y, direction):
        if self.cooldown <= 0:
            self.cooldown = 60
            self.ammo_list.append(self.ammo(x, y, direction))

        else:
            self.cooldown -= 1

    # function to check for meele attack on player
    def hurt_player(self, player):
        if player.x + player.width > self.x > player.x and player.y + player.height > self.y > player.y:
            if self.meele_cooldown <= 0:
                player.hurt(self.damage)
                self.meele_cooldown = 20
            else:
                self.meele_cooldown -= 1


# Main player class
class Player(Entity):

    height = 128
    width = 50
    width_var = [24, 42, 78]
    width_num = 0
    speed = 8
    vel = 20
    hit_nudge = 26
    hit_x = [33, 24, 10]
    infection = 0

    weapons = {}
    anim = {}

    frames = [(0, 0, 128, 128), (129, 0, 128, 128), (259, 0, 128, 128), (385, 0, 128, 128),
              (513, 0, 128, 128), (641, 0, 128, 128), (769, 0, 128, 128), (897, 0, 128, 128)]

    # Player initializing function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status = ["idle_", "walking_"]
        self.current_weapon = 0
        self.weapon_list = ["none", "pistol", "shotgun", "AR", "RPG"]  # ["none", "pistol", "shotgun", "RPG", "AR"]
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
        self.score = 0
        self.infection_cooldown = 100
        self.on_healer = False
        self.healer = None
        self.double_damage = False
        self.double_damage_timer = 400
        self.double_damage_count = 3
        self.level = 0

    # Reset player for each level
    def spawn(self):
        self.current_weapon = 0
        self.double_damage_count = 3
        self.hp = 100
        self.infection = 0

        # Setting the weapons back to full load
        self.weapons["pistol"].ammo_count = self.weapons["pistol"].ammo_limit
        self.weapons["pistol"].on_load = self.weapons["pistol"].hold_limit
        self.weapons["shotgun"].ammo_count = self.weapons["shotgun"].ammo_limit
        self.weapons["shotgun"].on_load = self.weapons["shotgun"].hold_limit
        self.weapons["AR"].ammo_count = self.weapons["AR"].ammo_limit
        self.weapons["AR"].on_load = self.weapons["AR"].hold_limit
        self.weapons["RPG"].ammo_count = self.weapons["RPG"].ammo_limit
        self.weapons["RPG"].on_load = self.weapons["RPG"].hold_limit

    # Init guns
    def init_guns(self):
        # making the gun instances
        self.weapons["none"] = None
        self.weapons["pistol"] = guns.Pistol()
        self.weapons["shotgun"] = guns.Shotgun()
        self.weapons["RPG"] = guns.RocketLauncher()
        self.weapons["AR"] = guns.MachineGun()

        # loading the gun animations
        self.weapons["pistol"].load_anim(IMAGES_PATH + "Characters/Player/Pistol/",
                                         IMAGES_PATH + "Projectiles/pistol_", BASE_PATH + "/resources/Sounds/Shoot_Pistol_1.wav")
        self.weapons["shotgun"].load_anim(IMAGES_PATH + "Characters/Player/Shotgun/",
                                          IMAGES_PATH + "Projectiles/shotgun", BASE_PATH + "/resources/Sounds/Shotgun.wav")
        self.weapons["RPG"].load_anim(IMAGES_PATH + "Characters/Player/RPG/",
                                      IMAGES_PATH + "Projectiles/rpg_", BASE_PATH + "/resources/Sounds/RPG.wav")
        self.weapons["AR"].load_anim(IMAGES_PATH + "Characters/Player/AR/",
                                     IMAGES_PATH + "Projectiles/ar_", BASE_PATH + "/resources/Sounds/Shoot_AR_1.wav")

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim["idle_R"] = pygame.image.load(path+"no_weapons/idle_R.png")
        self.anim["walking_R"] = pygame.image.load(path+"no_weapons/walking_R.png")
        self.anim["idle_L"] = pygame.image.load(path+"no_weapons/idle_L.png")
        self.anim["walking_L"] = pygame.image.load(path+"no_weapons/walking_L.png")

        # load sounds
        self.hit = pygame.mixer.Sound(BASE_PATH + "/resources/Sounds/hit.wav")

        # load bars for hud
        self.health_bar = pygame.image.load(IMAGES_PATH + "HUD/health_bar.png")
        self.shoot = pygame.image.load(IMAGES_PATH + "HUD/shoot.png")
        self.double_d = [pygame.image.load(IMAGES_PATH + "HUD/2x_on.png"),
                         pygame.image.load(IMAGES_PATH + "HUD/2x_off.png")]

    # Moving control
    def move(self, keys, platforms, enemies, bg_layers, portal, boss=False):

        # Update hitbox
        frame_num = self.frame % 8
        if frame_num in [1, 5]:
            self.width_num = 0

        if frame_num in [2, 4, 6, 8]:
            self.width_num = 1

        if frame_num in [3, 7]:
            self.width_num = 2

        # firing cool down
        if self.current_weapon > 0 and self.weapons[self.weapon_list[self.current_weapon]].fired:
            self.weapons[self.weapon_list[self.current_weapon]].fired = True
            if self.weapons[self.weapon_list[self.current_weapon]].cooldown < self.weapons[self.weapon_list[self.current_weapon]].cooldown_max:
                self.weapons[self.weapon_list[self.current_weapon]].cooldown += 1

            else:
                self.weapons[self.weapon_list[self.current_weapon]].fired = False
                self.weapons[self.weapon_list[self.current_weapon]].cooldown = 0

        # increase speed if L_shift key is pressed
        if keys[pygame.K_LSHIFT] and self.current_weapon != 4 and self.on_platform:
            self.speed = 15

        else:
            self.speed = 8

        # move right
        if keys[pygame.K_d]:

            # setting the character facing direction
            self.direction = "R"

            on_y = None
            on_x = None

            on_yh = None
            on_xw = None

            # checking for collisions
            for platform in platforms:

                if self.direction == "L" and self.current_weapon != 0:
                    on_x = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.hit_nudge> platform.x
                    on_xw = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.hit_nudge + self.width_var[self.width_num] > platform.x
                else:
                    on_x = platform.x + platform.width > self.x + self.hit_x[self.width_num] > platform.x
                    on_xw = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.width_var[self.width_num] > platform.x

                if platform.Taller:
                    on_y = platform.y + platform.height > self.y > platform.y
                    on_yh = platform.y + platform.height > self.y + self.height > platform.y

                else:
                    on_y = self.y+self.height > platform.y > self.y
                    on_yh = self.y+self.height > platform.y + platform.height > self.y

                if (on_x or on_xw) and (on_y or on_yh):
                    break

            if not ((on_x or on_xw) and (on_y or on_yh)):

                # selecting the background images for scorlling
                top = bg_layers[1]
                bottom = bg_layers[0]

                # Checking wether to scroll or move the player
                if self.x < 800:
                    self.x += self.speed

                # scrolling
                else:
                    for platform in platforms:
                        platform.scroll_x(self.speed, -1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, -1)

                    if boss:
                        boss.scroll_x(self.speed, -1)

                    top.scroll_x(self.speed / 2, -1)
                    bottom.scroll_x(self.speed / 3, -1)
                    portal.scroll_x(self.speed, -1)
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

            on_y = None
            on_x = None

            on_yh = None
            on_xw = None

            # checking for collision
            for platform in platforms:

                if self.direction == "L" and self.current_weapon != 0:
                    on_x = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.hit_nudge> platform.x
                    on_xw = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.hit_nudge + self.width_var[self.width_num] > platform.x
                else:
                    on_x = platform.x + platform.width > self.x + self.hit_x[self.width_num] > platform.x
                    on_xw = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.width_var[self.width_num] > platform.x

                if platform.Taller:
                    on_y = platform.y + platform.height > self.y > platform.y
                    on_yh = platform.y + platform.height > self.y + self.height > platform.y

                else:
                    on_y = self.y+self.height > platform.y > self.y
                    on_yh = self.y+self.height > platform.y + platform.height > self.y

                if (on_x or on_xw) and (on_y or on_yh):
                    break

            if not ((on_x or on_xw) and (on_y or on_yh)):
                top = bg_layers[1]
                bottom = bg_layers[0]

                # checking wether to scroll or move the player
                if self.x > 400:
                    self.x -= self.speed

                # scrolling
                else:
                    for platform in platforms:
                        platform.scroll_x(self.speed, 1)

                    for enemy in enemies:
                        enemy.scroll_x(self.speed, 1)

                    if boss:
                        boss.scroll_x(self.speed, 1)

                    top.scroll_x(self.speed/2, 1)
                    bottom.scroll_x(self.speed/3, 1)
                    portal.scroll_x(self.speed, 1)
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
                if self.current_weapon == 4:
                    self.vel = 10
                else:
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
            if self.vel < 12:
                self.vel += 1

        # Jumping
        if self.jumping:

            on_y = None
            on_x = None

            on_yh = None
            on_xw = None
            # checking for collisions
            for platform in platforms:
                on_x = platform.x + platform.width > self.x + self.hit_x[self.width_num] > platform.x

                if self.direction == "L" and self.current_weapon != 0:
                    on_xw = platform.x + platform.width > self.x + self.hit_x[
                        self.width_num] + self.hit_nudge + self.width_var[self.width_num] > platform.x
                else:
                    on_xw = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.width_var[self.width_num] > platform.x

                on_y = self.y + self.height > platform.y > self.y
                on_yh = self.y + self.height > platform.y + platform.height > self.y

                if (on_x or on_xw) and (on_y or on_yh):
                    break

            if (on_x or on_xw) and (on_y or on_yh):
                self.vel = 0
                self.frame = 0

        # moving the character if on a moving platform
        if self.on_moving_platform and self.platform.move_style == "x":

            top = bg_layers[1]
            bottom = bg_layers[0]

            if 800 > self.x > 400:
                self.x += self.platform.moving_speed * self.plat_move_dir

            # scrolling
            else:
                for platform in platforms:
                    platform.scroll_x(self.platform.moving_speed, self.plat_move_dir * -1)

                for enemy in enemies:
                    enemy.scroll_x(self.platform.moving_speed, self.plat_move_dir * -1)

                top.scroll_x(self.platform.moving_speed / 2, self.plat_move_dir * -1)
                bottom.scroll_x(self.platform.moving_speed / 3, self.plat_move_dir * -1)
                portal.scroll_x(self.platform.moving_speed, self.plat_move_dir * -1)

                if self.current_weapon != 0:
                    self.weapons[self.weapon_list[self.current_weapon]].scroll_bullets(self.platform.moving_speed, self.plat_move_dir * -1)

        if self.on_moving_platform and self.platform.move_style == "y":
            self.y += self.platform.moving_speed * self.plat_move_dir

        # Firing the bullets if the conditions are met
        if (keys[pygame.K_SPACE] and self.current_weapon > 0 and self.weapons[self.weapon_list[self.current_weapon]].cooldown <= 0
                and self.weapons[self.weapon_list[self.current_weapon]].on_load > 0):
            self.weapons[self.weapon_list[self.current_weapon]].fired = True
            if self.direction == "R":
                direction = 1
                width = self.width * 3/2
            else:
                direction = -1
                width = 0
            self.weapons[self.weapon_list[self.current_weapon]].fire(self.x+width, self.y+40, direction)

        # Call reload function of the guns if conditions met
        if keys[pygame.K_r] and not keys[pygame.K_SPACE] and self.current_weapon != 0:
            self.weapons[self.weapon_list[self.current_weapon]].reload()

        # restock if on healer
        if keys[pygame.K_e] and self.on_healer and self.on_platform:
            self.hp = 100
            if not self.healer.used:
                for weapon in self.weapon_list:
                    if weapon == "none":
                        pass
                    else:
                        self.weapons[weapon].ammo_count = self.weapons[weapon].ammo_limit
                self.healer.used = True

        # Conditions to enable Double Damage
        if keys[pygame.K_f] and not self.double_damage and self.double_damage_count > 0 and self.level >= 2:
            self.double_damage = True
            self.double_damage_count -= 1

        # updating the double damage timer
        if self.double_damage:
            if self.double_damage_timer > 0:
                self.double_damage_timer -= 1

            else:
                self.double_damage = False
                self.double_damage_timer = 300

    # checking for being on platform
    def on_ground(self, platforms):

        for platform in platforms:
            if self.direction == "L" and self.current_weapon != 0:
                x_on_platform = platform.x + platform.width > self.x + self.hit_x[self.width_num] + self.hit_nudge > platform.x or platform.x + platform.width > (self.x + self.hit_x[self.width_num] + self.hit_nudge + self.width_var[self.width_num]) > platform.x

            else:
                x_on_platform = platform.x + platform.width > self.x + self.hit_x[self.width_num] > platform.x or platform.x + platform.width > (self.x + self.hit_x[self.width_num] + self.width_var[self.width_num]) > platform.x

            if (platform.y + platform.height) > (self.y + self.height) >= platform.y and x_on_platform:
                self.on_platform = True
                self.vel = 0

                # Setting the player back on platform if he falls into the platform
                if self.y+self.height - platform.y < 20 and not platform.Taller:
                    self.y = platform.y - self.height

                # Checking if on Moving Platform
                if platform.is_moving:
                    self.on_moving_platform = True
                    self.occupied = True
                    self.plat_move_dir = platform.moving_dir
                    self.platform = platform
                else:
                    self.on_moving_platform = False

                # Checking if on healer(boost) platform
                if platform.healer:
                    self.infection = 0
                    self.on_healer = True
                    self.healer = platform
                else:
                    self.on_healer = False
                    self.healer = None

                # checking if on a tall platform
                if platform.Taller:
                    if self.y + self.height - platform.y < 20:
                        self.y = platform.y - self.height

                    elif (self.x + self.hit_x[self.width_num] + self.width_var[self.width_num]) - platform.x <= 40 and self.y + self.height - platform.y >= 21:
                        self.x = platform.x - (self.hit_x[self.width_num] + self.width_var[self.width_num] + self.hit_nudge) - 10
                        self.on_platform = False

                    elif (self.x + self.hit_x[self.width_num] + self.width_var[self.width_num]) - (platform.x + platform.width) <= 40 and self.y + self.height - platform.y >= 21:
                        self.x = platform.x + platform.width + (self.hit_x[self.width_num] + self.width_var[self.width_num] + self.hit_nudge) + 10
                        self.on_platform = False
                break

            else:
                self.on_moving_platform = False
                self.on_platform = False

            if self.y > 660:
                self.hp = 0

    # Changing weapon function
    def change_weapon(self, keys):

        # Checking if any ammo is still on screen
        if self.current_weapon != 0:
            if not self.weapons[self.weapon_list[self.current_weapon]].ammo_list:
                can_switch = True
            else:
                # if no ammo on screen then allow player to switch weapons
                can_switch = False
        else:
            can_switch = True

        if can_switch:
            if keys[pygame.K_1]:
                self.current_weapon = 0

            if keys[pygame.K_2]:
                self.current_weapon = 1

            if keys[pygame.K_3]:
                self.current_weapon = 2

            if keys[pygame.K_4] and self.level >= 1:
                self.current_weapon = 3

            if keys[pygame.K_5] and self.level >= 3:
                self.current_weapon = 4

    # rendering function
    def draw(self, win, platforms):
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
            if self.status_num == 0:
                win.blit(self.weapons[self.weapon_list[self.current_weapon]].anim[self.status[self.status_num] + self.direction], (self.x, self.y),
                         (0, 0, self.width * 2, self.height))

            else:
                win.blit(self.weapons[self.weapon_list[self.current_weapon]].anim[self.status[self.status_num]+self.direction],
                         (self.x, self.y), self.frames[self.width_num])

            self.weapons[self.weapon_list[self.current_weapon]].update_bullets(win, platforms, self.double_damage)

    # if player infected then damage player over time
    def infection_damage(self):
        if self.infection_cooldown <= 0:
            self.hp -= self.infection
            self.infection_cooldown = 100
        else:
            self.infection_cooldown -= 1

    # check if enemy is hurt by bullets
    def enemy_killed(self, enemies, win):
        for enemy in enemies:
            ammo_list = self.weapons[self.weapon_list[self.current_weapon]].ammo_list
            for ammo in ammo_list:
                if enemy.width + enemy.x > ammo.x > enemy.x and enemy.y + enemy.height > ammo.y > enemy.y:
                    # playing the hit sound as the enemy is hit by the player
                    self.hit.play()
                    # if weapon is RPG then explode shell
                    if self.current_weapon == 4:
                        self.weapons[self.weapon_list[self.current_weapon]].explode(ammo, win)
                    else:
                        ammo_list.pop(ammo_list.index(ammo))

                    if enemy.hp > 0:
                        # do double the damage if double damage is on
                        if self.double_damage:
                            enemy.hp -= ammo.damage * 2
                        else:
                            enemy.hp -= ammo.damage

    # Update function for player health bar
    def update_player_hb(self, win):
        if self.hp < 0:
            self.hp = 0
        win.blit(self.health_bar, (96, 13), (0, 0, (self.hp/100) * 239, 13))

    # Update function for weapon cooldown bar and fire indicator
    def update_weapon_cdb(self, win):
        if self.current_weapon != 0:
            cooldown = self.weapons[self.weapon_list[self.current_weapon]].cooldown
            cooldown_max = self.weapons[self.weapon_list[self.current_weapon]].cooldown_max
            pygame.draw.rect(win, (230, 230, 230), (246, 69, 13, 53))
            pygame.draw.rect(win, (31, 31, 31), (246, 69, 13, (1-(cooldown/cooldown_max)) * 53))

            if self.weapons[self.weapon_list[self.current_weapon]].fired:
                win.blit(self.shoot, (212, 107), (0, 0, 18, 18))
            else:
                win.blit(self.shoot, (212, 107), (18, 0, 18, 18))

    # Update function to draw double damage indicator
    def update_double_d(self, win):
        if self.double_damage:
            win.blit(self.double_d[0], (968, 8))
        else:
            win.blit(self.double_d[1], (968, 8))
