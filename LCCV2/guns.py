from LCCV2.items import Weapons
import LCCV2.shells as shells


# Pistol
class Pistol(Weapons):
    ammo_count = 35
    hold_limit = 7
    on_load = 7
    cooldown = 5
    ammo = shells.PistolShells


# Shotgun
class Shotgun(Weapons):
    ammo_count = 25
    hold_limit = 5
    on_load = 5
    cooldown = 20
    ammo = shells.ShotShells


# Machine-gun
class MachineGun(Weapons):
    ammo_limit = 90
    ammo_count = 90
    hold_limit = 30
    on_load = 30
    cooldown = 2
    ammo = shells.ARShells


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo_count = 50
    hold_limit = 5
    on_load = 5
    cooldown = 60
    ammo = shells.RPGShells
