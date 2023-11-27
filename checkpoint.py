from surface import Surface


class Checkpoint(Surface):  # Vous pouvez ajouter des classes parentes

    def __init__(self, x, y,checkpoint_id):
        super().__init__(x, y)
        self.checkpoint_id = checkpoint_id

    def draw(self, screen):
        super().draw()
        self.surface.fill((128, 128, 128))
        screen.blit(self.surface, (self.x, self.y))