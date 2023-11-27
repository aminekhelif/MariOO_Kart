from surface import Surface


class Lava(Surface):  # Vous pouvez ajouter des classes parentes

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        super().draw()
        self.surface.fill((255, 0, 0))
        screen.blit(self.surface, (self.x, self.y))