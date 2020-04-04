
class Weapons:

    # Variables
    ammo_limit = 100
    ammo = 100
    hold_limit = 25
    on_load = 25
    width = 10
    height = 10

    # ammo firing function
    def fire(self):
        self.ammo -= 1

    # Reloading ammo function
    def reload(self):
        self.ammo -= self.hold_limit - self.on_load

    # Loading ammo function
    def load_ammo(self, bullets):
        self.ammo += bullets
        if self.ammo > self.ammo_limit:
            self.ammo = self.ammo_limit
