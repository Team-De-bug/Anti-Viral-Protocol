from .items import Weapons


# Pistol
class Pistol(Weapons):
    ammo = 100
    hold_limit = 10
    on_load = 10

    def draw(self):
        pass


# Shotgun
class Shotgun(Weapons):
    ammo = 50
    hold_limit = 1
    on_load = 1

    def draw(self):
        pass


# Machine-gun
class MachineGun(Weapons):
    ammo = 300
    hold_limit = 50
    on_load = 50

    def draw(self):
        pass


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo = 50
    hold_limit = 5
    on_load = 5

    def draw(self):
        pass
