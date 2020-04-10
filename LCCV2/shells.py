from items import Shells
import pygame


# defining and creating the bullets for each gun
class ShotShells(Shells):
    damage = 50
    dist_limit = 500

    # animation loader function
    @classmethod
    def load_anim(cls, path):
        cls.anim = [pygame.image.load(path+".png"),
                    pygame.image.load(path+"_2x.png")]

    def draw(self, win, double):
        if double:
            win.blit(self.anim[1], (self.x, self.y))
        else:
            win.blit(self.anim[0], (self.x, self.y))


class ARShells(Shells):
    damage = 10
    dist_limit = 750


class RPGShells(Shells):
    damage = 100
    vel = 20
    dist_limit = 600


class PistolShells(Shells):
    damage = 15
    dist_limit = 700
    

class Virus1shell(Shells):
    dist_limit = 500

    # animation loader function
    @classmethod
    def load_anim(cls, path):

        cls.anim = [pygame.image.load(path + "L.png"),
                    pygame.image.load(path + "R.png")]

    def draw(self, win):
        if self.direction > 0:
            win.blit(self.anim[1], (self.x, self.y))
        else:
            win.blit(self.anim[0], (self.x, self.y))
