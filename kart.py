import math
import pygame
from ai import AI
import os

current_file_directory = os.path.dirname(__file__)

MAX_ANGLE_VELOCITY = 0.05
MAX_ACCELERATION = 0.25


class Kart():

    def __init__(self, controller):
        self.has_finished = False
        self.controller = controller
        # La condition est ajoutée en raison de l'erreur affichée lors du test : "L'objet 'SequencePlayer'
        # ne possède pas l'attribut 'set_kart'"
        if isinstance(self.controller, AI):
            self.controller.set_kart(self)
        self.kart_position = []  # position (x,y)
        self.surface_position_x = 0
        self.surface_position_y = 0
        self.theta = 0  # orientation
        self.speed = 0  # v(t)
        self.v_theta = 0  # commande orientation
        self.a_c = 0  # commande acceleration
        self.theta_checkpoint = 0
        self.position_checkpoint = [0, 0]
        self.next_checkpoint_id = 0
        self.kart_image = pygame.image.load(os.path.join(current_file_directory, 'ressources', 'kart.png'))
        self.kart_image = pygame.transform.scale(self.kart_image, (75, 50))

    def reset(self, initial_position, initial_orientation):
        self.kart_position = [position for position in initial_position]
        self.position_checkpoint = [position for position in initial_position]
        self.theta = initial_orientation

    def forward(self):
        self.a_c += MAX_ACCELERATION

    def backward(self):
        self.a_c -= MAX_ACCELERATION

    def turn_left(self):
        self.v_theta -= MAX_ANGLE_VELOCITY

    def turn_right(self):
        self.v_theta += MAX_ANGLE_VELOCITY

    def commands(self, f=0, speed=-1):
        if speed == -1:
            # On a remplacé l'équation (2) dans (3) pour éviter de créer une autre variable
            self.speed = self.a_c + self.speed * math.cos(self.v_theta) * (1 - f)
        elif speed == 0:
            self.theta = self.theta_checkpoint
            self.kart_position = [self.position_checkpoint[0], self.position_checkpoint[1]]
        else:
            self.speed = speed
        self.theta = self.theta + self.v_theta
        self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
        self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)

    def update_position(self, string, screen):

        # Nombre de checkpoints
        nbr_checkpoints = set(char for char in string if char in ['C', 'D', 'E', 'F'])

        # La position de la surface à laquelle appartient le kart est déterminée pour être ensuite utilisée
        # dans la détermination du type de surface en utilisant string
        self.surface_position_x = int(self.kart_position[0] // 50)
        self.surface_position_y = int(self.kart_position[1] // 50)

        # On détermine le type de surface auquel le kart appartient en utilisant une structure try, car il est possible
        # que la position soit en dehors de la piste, auquel cas une erreur de liste (listindex) pourrait survenir
        try:
            type_of_surface = string.split('\n')[self.surface_position_y][self.surface_position_x]
            # Si le kart sort du côté Nord ou Ouest, il n'y aura pas d'erreur d'index de liste, car les listes
            # acceptent les indices négatifs
            if self.surface_position_x < 0 or self.surface_position_y < 0:
                type_of_surface = 'L'
        except:
            # Si kart sort de la piste, il adopte par défaut le comportement comme s'il était dans la lave
            # (retour au point de contrôle)
            type_of_surface = 'L'

        if type_of_surface == 'R':
            f = 0.02
            self.commands(f)

        elif type_of_surface == 'G':
            f = 0.2
            self.commands(f)

        elif type_of_surface == 'B':
            speed = 25
            self.commands(0, speed)

        elif type_of_surface == 'L':
            speed = 0
            self.commands(0, speed)

        for id, checkpoint in [(0, 'C'), (1, 'D'), (2, 'E'), (3, 'F')]:
            if type_of_surface == checkpoint:
                if id == self.next_checkpoint_id:
                    self.theta_checkpoint = self.theta
                    self.position_checkpoint = [self.kart_position[0], self.kart_position[1]]
                    self.next_checkpoint_id += 1
                    if self.next_checkpoint_id == len(nbr_checkpoints):
                        self.has_finished = True
                f = 0.02
                self.commands(f)

        # Réinitialisation
        self.v_theta = 0
        self.a_c = 0

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.kart_image, -math.degrees(self.theta))
        rect = rotated_image.get_rect(center=self.kart_position)
        screen.blit(rotated_image, rect.topleft)