import pygame
from surface import Surface

class Grass(Surface):  # Vous pouvez ajouter des classes parentes

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        super().draw()
        #self.image = pygame.image.load("C:/Users/ED/Desktop/Mes documents/Photo Identité.jpg")
        #self.image = pygame.transform.scale(self.image, (50, 50))
        self.surface.fill((0, 255, 0))
        screen.blit(self.surface, (self.x, self.y))
