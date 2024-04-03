class Area():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface= None

    def draw(self,screen):
        screen.blit(self.surface, (self.x, self.y))