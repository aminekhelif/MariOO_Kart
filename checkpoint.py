import pygame
from area import Area
import os

current_file_directory = os.path.dirname(__file__)


class Checkpoint(Area):

    def __init__(self, x, y, checkpoint_id):
        Area.__init__(self, x, y)
        self.surface = pygame.image.load(os.path.join(current_file_directory, 'ressources', "check.png"))
        self.checkpoint_id = checkpoint_id
