import math
import pygame

MAX_ANGLE_VELOCITY = 0.05
MAX_ACCELERATION = 0.25


class Kart():  # Vous pouvez ajouter des classes parentes
    """
    Classe implementant l'affichage et la physique du kart dans le jeu
    """

    def __init__(self, controller):
        self.has_finished = False
        self.controller = controller
        self.kart_position = []  # position (x,y)
        self.theta = 0  # orientation
        self.speed = 0  # v(t)
        self.v_theta = 0  # commande orientation
        self.a_c = 0  # commande acceleration
        self.theta_checkpoint = 0
        self.position_checkpoint = [0,0]
        self.id_next_checkpoint = 0

    def reset(self, initial_position, initial_orientation):
        self.kart_position = initial_position
        self.theta = initial_orientation

    def forward(self):
        self.a_c += MAX_ACCELERATION
        # A completer

    def backward(self):
        self.a_c -= MAX_ACCELERATION

    def turn_left(self):
        self.v_theta -= MAX_ANGLE_VELOCITY

    def turn_right(self):
        self.v_theta += MAX_ANGLE_VELOCITY

    def update_position(self, string, screen):

        # on détermine la position de surface dont kart appartient pour l'utiliser ensuite dans
        # la détermination de type de surface en utilisant le string
        self.surface_position_x = int(self.kart_position[0] // 50)
        self.surface_position_y = int(self.kart_position[1] // 50)

        try:
            type_of_surface = string.split('\n')[self.surface_position_y][self.surface_position_x]
        except:  # il se peut que la positione est dehors de track dans ce cas on aurra erreur listindex
            type_of_surface = 'R'   # si kart sort de track par défaut elle se comport comme si elle est dans R

        if type_of_surface == 'R':
            f = 0.02
            self.speed = self.a_c + self.speed * math.cos(self.v_theta) * (1 - f)  # on a remplacé l'équation (2) dans (3) pour éviter de créer une autre variable
            self.theta = self.theta + self.v_theta
            self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
            self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)

        elif type_of_surface == 'G':
            f = 0.2
            self.speed = self.a_c + self.speed * math.cos(self.v_theta) * (1 - f)  # on a remplacé l'équation (2) dans (3) pour éviter de créer une autre variable
            self.theta = self.theta + self.v_theta
            self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
            self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)

        elif type_of_surface == 'B':
            self.speed = 25
            self.theta = self.theta + self.v_theta
            self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
            self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)

        elif type_of_surface == 'L':
            self.speed = 0
            self.theta = self.theta_checkpoint
            self.kart_position = [self.position_checkpoint[0],self.position_checkpoint[1]]

        for id,checkpoint in [(0,'C'),(1,'D'),(2,'E'),(3,'F')]:
            if type_of_surface == checkpoint:
                if id == self.id_next_checkpoint:
                    self.theta_checkpoint = self.theta
                    self.position_checkpoint = [self.kart_position[0],self.kart_position[1]] # parceque si on fait dirctement égalité entre les deux tableuax on aura une égalité tout
                                                                                             # le temps position check poitn suit toujours kartpositon ou on peut utiliser .copy()
                    self.id_next_checkpoint += 1
                    if self.id_next_checkpoint == 4:
                        self.has_finished = True
                f = 0.02
                self.speed = self.a_c + self.speed * math.cos(self.v_theta) * (1 - f)
                self.theta = self.theta + self.v_theta
                self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
                self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)

        # Réinitialisation
        self.v_theta = 0
        self.a_c = 0

    def draw(self, screen):
        # A modifier et completer
        kart_radius = 20

        # Draw a circle
        pygame.draw.circle(screen, (255, 255, 255), self.kart_position, kart_radius)

    # Completer avec d'autres methodes si besoin (ce sera probablement le cas)