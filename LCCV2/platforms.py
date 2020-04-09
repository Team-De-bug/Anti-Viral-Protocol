import pygame


class Platform:
    width = 600
    height = 50
    is_moving = False
    healer = False
    Taller = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Loading sprite
    def load_anim(self, path):
        self.anim = pygame.image.load(path)

    # moving platform function
    def scroll_x(self, vel, direction):
        self.x += vel * direction

    # rendering the sprite for the game
    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))


class FloatingPlatform(Platform):
    width = 128
    height = 25


class TallPlatform(Platform):
    width = 540
    height = 404
    Taller = True


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
    width = 144
    height = 64
    dist_x = 70
    dist_x_max = 70
    dir_x = True
    dist_y_max = 70
    dist_y = 70
    dir_y = True
    is_moving = True
    moving_dir = 1
    move_style = None
    moving_speed = 1

    def move_x(self, speed):
        self.move_style = "x"
        self.moving_speed = speed
        if self.dir_x:
            self.x += speed
            self.dist_x -= speed
            self.moving_dir = 1

        else:
            self.x -= speed
            self.dist_x += speed
            self.moving_dir = -1

        if self.dist_x > self.dist_x_max:
            self.dir_x = True

        elif self.dist_x < 0:
            self.dir_x = False

    def move_y(self, speed):
        self.move_style = "y"
        if self.dir_y:
            self.y += speed
            self.dist_y -= speed

        else:
            self.y -= speed
            self.dist_y += speed

        if self.dist_y > self.dist_y_max:
            self.dir_y = True

        elif self.dist_y < 0:
            self.dir_y = False

    # Set the distance to move in x axis
    def set_distance_x(self, dist):
        self.dist_x = dist
        self.dist_x_max = dist

    # Set the distance to move in y axis
    def set_distance_y(self, dist):
        self.dist_y = dist
        self.dist_y_max = dist


class BasePlatform(Platform):
    width = 1600
    height = 50
    y = 602

    def __init__(self, x):
        super().__init__(x, self.y)


class BackDrop(Platform):
    height = 640
    width = 1600
    x = 0
    y = 0

    def __init__(self):
        super().__init__(self.x, self.y)


class Boost(Platform):
    width = 64
    height = 25

    healer = True
    used = False

    def __init__(self, x, y):
        super().__init__(x, y)
        self.vir_y = self.y + 153


class Endgate(Platform):
    width = 32
    height = 129