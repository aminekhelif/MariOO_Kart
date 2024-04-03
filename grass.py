import pygame
from area import Area
import os

current_file_directory = os.path.dirname(__file__)


class Grass(Area):

    def __init__(self, x, y):
        Area.__init__(self, x, y)
        self.surface = pygame.image.load(os.path.join(current_file_directory, 'ressources', "gras.jpg"))
