import pygame


class Platform:
    width = 600
    height = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Loading sprite
    @classmethod
    def load_anim(cls, path):
        cls.anim = pygame.image.load(path)

    # moving platform function
    def scrollx(self, vel, direction):
        self.x += vel * direction

    # rendering the sprite for the game
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))


class MockPlatform(Platform):

    x = 5
    y = 5

    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.width, self.height])
