from LCCV2.items import Shells
import pygame


# defining and creating the bullets for each gun
class ShotShells(Shells):
    damage = 50
    dist_limit = 500

    # animation loader function
    @classmethod
    def load_anim(cls, path):
        cls.anim = pygame.image.load(path)

    def draw(self, win):
        win.blit(self.anim, (self.x, self.y))


class ARShells(Shells):
    damage = 10
    dist_limit = 750


class RPGShells(Shells):
    damage = 100
    vel = 20
    dist_limit = 600


class PistolShells(Shells):
    damage = 15
    dist_limit =700
    


class Virus1shell(Shells):
    pass
