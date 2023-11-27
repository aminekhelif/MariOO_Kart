import pygame

class Surface():
    BLOCK_SIZE = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.surface = pygame.Surface((Surface.BLOCK_SIZE, Surface.BLOCK_SIZE))