from LCCV2.items import Weapons
import LCCV2.shells as shells


# Pistol
class Pistol(Weapons):
    ammo_count = 100
    hold_limit = 10
    on_load = 10
    ammo = shells.PistolShells


# Shotgun
class Shotgun(Weapons):
    ammo_count = 50
    hold_limit = 1
    on_load = 1
    ammo = shells.ShotShells


# Machine-gun
class MachineGun(Weapons):
    ammo_count = 300
    hold_limit = 50
    on_load = 50
    ammo = shells.ARShells


# rocket-Launcher
class RocketLauncher(Weapons):
    ammo_count = 50
    hold_limit = 5
    on_load = 5
    ammo = shells.RPGShells
