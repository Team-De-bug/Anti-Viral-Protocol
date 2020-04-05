from .items import Weapons


# Pistol
class Pistol(Weapons):
    ammo = 100
    hold_limit = 10
    on_load = 10
    width = 10
    height = 10
    anim = None


# Shotgun
class Shotgun(Weapons):
    ammo = 50
    hold_limit = 1
    on_load = 1
    width = 10
    height = 10
    anim = None


# Machine-gun
class MachineGun(Weapons):
    ammo = 300
    hold_limit = 50
    on_load = 50
    width = 10
    height = 10
    anim = None


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo = 50
    hold_limit = 5
    on_load = 5
    width = 10
    height = 10
    anim = None