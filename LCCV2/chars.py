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


# Main player class
class Player(Entity):

    speed = 1

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim = pygame.image.load(path)
        '''
        self.anim = {"idle_L": [], "jumping_L": [], "running_L": [],
                     "idle_R": [], "jumping_R": [], "running_R": []}
        '''
    # Moving control
    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

    # rendering function
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))
