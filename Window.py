import pygame
from pygame.locals import *


class Window:
    colors = ((0, 0, 0), (255, 255, 255), (0, 255, 0))
    width = 700
    height = 700

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption("Runnig!")
        self.fill()

    def fill(self):
        self.screen.fill(self.colors[1])

    def draw(self, x, y, size, thickness, colour):
        pygame.draw.circle(self.screen, colour, (x, y), size, thickness)
