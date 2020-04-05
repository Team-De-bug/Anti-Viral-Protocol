import pygame


# Entity class for all characters
class Entity:

    # Default variables
    hp = 100
    facing = None
    speed = 10

    width = 50
    height = 50

    def __init__(self, x, y):

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

    height = 128
    speed = 10
    vel = 20
    jumping = False
    on_platform = False

    # loading animation function
    def load_anim(self, path):

        # empty hand animations
        self.anim = pygame.image.load(path)
        '''
        self.anim = {"idle_L": [], "jumping_L": [], "running_L": [],
                     "idle_R": [], "jumping_R": [], "running_R": []}
        '''
    # Moving control
    def move(self, platforms):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:

            if self.x < 650:
                self.x += self.speed

            else:
                for platform in platforms:
                    platform.scrollx(self.speed, -1)

        elif keys[pygame.K_LEFT]:
            if self.x > 100:
                self.x -= self.speed

            else:
                for platform in platforms:
                    platform.scrollx(self.speed, 1)

        if keys[pygame.K_UP] and self.on_platform:
            if not self.jumping:
                self.vel = 20
                self.jumping = True

        if self.jumping and self.vel > 0:
            self.y -= self.vel
            self.vel -= 1

        elif self.jumping and self.vel <= 0:
            self.jumping = False

        if not self.on_platform and not self.jumping:
            self.y += self.vel
            self.vel += 1

    def on_ground(self, platforms):

        for platform in platforms:
            x_on_platform = platform.x + platform.width > self.x > platform.x or platform.x + platform.width > (self.x + self.width) > platform.x
            if (platform.y + platform.height) > (self.y + self.height) >= platform.y and x_on_platform:
                self.on_platform = True
                self.vel = 20
                self.y = platform.y - self.height
                break

            else:
                self.on_platform = False

    # rendering function
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))
