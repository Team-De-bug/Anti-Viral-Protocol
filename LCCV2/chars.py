# Entity class for all characters
class Entity:

    # Default variables
    hp = 100
    facing = None
    speed = 10

    width = 50
    height = 50

    def __init__(self, x, y,):

        # Getting the character location setup
        self.x = x
        self.y = y

    # Taking health away
    def hurt(self, damage):
        self.hp -= damage

    # Getting health
    def re_gen(self, hp):
        self.hp += hp

    # Load animations
    @classmethod
    def load_anim(cls):
        print("animation lot loaded")


class Enemy(Entity):

    # Variables
    points = 100
    hit = 5

    # Class initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Move function fall back
    @staticmethod
    def move():
        print("move not created")

    # Draw method fallback
    @staticmethod
    def draw(self):
        print("draw method not made")