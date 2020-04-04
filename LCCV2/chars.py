import pygame


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


class Enemy(Entity):

    # Variables
    points = 100
    hit = 5

    # Class initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # load anim_function
    def load_anim(self, path):
        self.idle = pygame.image.load(path)
        self.moving = pygame.image.load(path)
        self.attack = pygame.image.load(path)

    # Move function fall back
    def move(self):
        pass

    # Draw method fallback
    def draw(self):
        pass
