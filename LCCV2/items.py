class Weapons:

    # Variables
    ammo = 100
    damage = 10
    hold_limit = 25
    on_load = 25

    # Initializer
    def __init__(self, on_player):
        self.on_player = on_player

    # Animation loader
    @classmethod
    def load_anim(cls):
        print("animation not linked")

    # ammo firing function
    def fire(self):
        self.ammo -= 1

    # Loading ammo func
    def load(self):
        self.ammo -= self.hold_limit - self.on_load
