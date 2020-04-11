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
