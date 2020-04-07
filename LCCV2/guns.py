from LCCV2.items import Weapons
import LCCV2.shells as shells


# Pistol
class Pistol(Weapons):
    ammo_count = 100
    hold_limit = 10
    on_load = 10
    cooldown = 10
    ammo = shells.PistolShells


# Shotgun
class Shotgun(Weapons):
    ammo_count = 50
    hold_limit = 7
    on_load = 7
    cooldown = 20
    ammo = shells.ShotShells


# Machine-gun
class MachineGun(Weapons):
    ammo_count = 300
    hold_limit = 30
    on_load = 30
    cooldown = 3
    ammo = shells.ARShells


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo_count = 50
    hold_limit = 5
    on_load = 5
    cooldown = 60
    ammo = shells.RPGShells
