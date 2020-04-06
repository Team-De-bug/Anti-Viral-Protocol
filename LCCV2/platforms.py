import pygame


class Platform:
    width = 600
    height = 50
    is_moving = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Loading sprite
    def load_anim(self, path):
        self.anim = pygame.image.load(path)

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


class MovingTile(Platform):

    x = 72
    y = 32
    width = 70
    height = 50
    dist_x = 70
    dir_x = True
    dist_y = 70
    dir_y = True
    is_moving = True
    moving_dir = 1
    moving_speed = 1

    def move_x(self, speed):
        self.moving_speed = speed
        if self.dir_x:
            self.x += speed
            self.dist_x -= speed
            self.moving_dir = 1

        else:
            self.x -= speed
            self.dist_x += speed
            self.moving_dir = -1

        if self.dist_x > 64:
            self.dir_x = True

        elif self.dist_x < 0:
            self.dir_x = False

    def move_y(self, speed):
        if self.dir_y:
            self.y += speed
            self.dist_y -= speed

        else:
            self.y -= speed
            self.dist_y += speed

        if self.dist_y > 64:
            self.dir_y = True

        elif self.dist_y < 0:
            self.dir_y = False