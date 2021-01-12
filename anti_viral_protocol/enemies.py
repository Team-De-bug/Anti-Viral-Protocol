import pygame
from .chars import Enemy
from .shells import *
import os

# Working file paths
BASE_PATH = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(BASE_PATH, 'resources/Images/')


# virus_1
class Virus1(Enemy):
    ammo = Virus1shell
    height = 78
    width = 78
    hp = 100
    health_max = 100


# Virus_2
class Virus2(Enemy):
    ammo = Virus2shell
    height = 78
    width = 78
    hp = 200
    health_max = 200


# Virus3
class Virus3(Enemy):
    ammo = Virus3shell
    height = 156
    width = 156
    hp = 300
    health_max = 300


# Virus4
class Virus4(Enemy):
    ammo = Virus4shell
    height = 156
    width = 156
    hp = 350
    health_max = 350


# virus_boss
class VirusBoss(Enemy):
    ammo = Virus1shell
    height = 320
    width = 320
    hp = 500
    health_max = 500
    spawn_cooldown = 70

    enemy_list = []
    enemy = Virus2

    # Loading the boss health bar
    health_bar = pygame.image.load(IMAGES_PATH + "HUD/bossbar.png")

    # Function to spawn enemies
    def spawn_enemies(self, player):
        # checking if there is room to spawn enemies
        if self.spawn_cooldown <= 0 and len(self.enemy_list) < 11:
            self.spawn_cooldown = 70
            # checking for the distance from player
            if 700 > player.x - self.x or 700 > self.x - player.x:
                self.enemy_list.append(self.enemy(self.x - 50, 500))
                self.enemy_list[-1].load_anim(IMAGES_PATH + "/Characters/Virus/Virus_2/idle.png",
                                              IMAGES_PATH + "Projectiles/virus_1_")
                self.enemy_list[-1].Tracking = True

        else:
            self.spawn_cooldown -= 1

    # Checking for damage by player
    def check_hurt(self, player):
        if player.current_weapon != 0:
            if not self.enemy_list:
                ammo_list = player.weapons[player.weapon_list[player.current_weapon]].ammo_list
                for ammo in ammo_list:
                   if self.x + self.width > ammo.x > self.x and self.y + self.height > ammo.y > self.y:
                        self.hp -= ammo.damage
                        ammo_list.pop(ammo_list.index(ammo))

    # Update function for boss health-bar
    def update_health_bar(self, win):
        if self.hp > 0:
            win.blit(self.health_bar, (430, 22), (0, 0, (self.hp/self.health_max) * 500, 20))

    # function to kill player if in the virus
    def kill_on_contact(self, player):
        if self.x + self.width > player.x > self.x and self.y + self.height > player.y > self.y:
            player.hp = 0
