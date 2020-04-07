from LCCV2.items import Shells
import pygame


# defining and creating the bullets for each gun
class ShotShells(Shells):

    # animation loader function
    @classmethod
    def load_anim(cls, path):
        cls.anim = pygame.image.load(path)

    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))


class ARShells(Shells):
    pass


class RPGShells(Shells):
    pass


class PistolShells(Shells):
    pass


class Virus1shell(Shells):
    pass
