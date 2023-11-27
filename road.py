from surface import Surface


class Road(Surface):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        super().draw()
        self.surface.fill((0, 0, 0))
        screen.blit(self.surface, (self.x, self.y))