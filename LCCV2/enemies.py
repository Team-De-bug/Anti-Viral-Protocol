from chars import Enemy
from shells import Virus1shell


# virus_1
class Virus1(Enemy):
    ammo = Virus1shell


# Virus_2
class Virus2(Enemy):
    ammo = Virus1shell
    height = 150
    width = 150


# Virus3
class Virus3(Enemy):
    ammo = Virus1shell
    height = 150
    width = 150


# Virus4
class Virus4(Enemy):
    ammo = Virus1shell
    height = 150
    width = 150


# virus_boss
class VirusBoss(Enemy):
    ammo = Virus1shell
    height = 500
    width = 500
    spawn_cooldown = 70

    enemy_list = []
    enemy = Virus2

    def spawn_enemies(self, player):
        if self.spawn_cooldown <= 0:
            self.spawn_cooldown = 70
            if 700 > player.x - self.x > 200 or 700 > self.x - player.x > 200:
                self.enemy_list.append(self.enemy(self.x - 50, 500))
                self.enemy_list[-1].load_anim("resources/Images/Characters/Virus/Virus_2/idle.png", "resources/Images/Projectiles/virus_1_")
                self.enemy_list[-1].Tracking = True

        else:
            self.spawn_cooldown -= 1
