# import pygame
# import math
#
# # Premier code
# string = """GGGGGGGGGGGGGGGGGGGGGGGGGG
# GRRRRRRCRRRRRRRRRBRRRRRRRG
# GRRRRRRCRRRRRRRRRBRRRRRRRG
# GRRRRRRCRRRRRRRRRRRRRRRRRG
# GRRRRRRCRRRRRRRRRRRRRRRRRG
# GGGGGGGGGGGGGGGGGGGGGRRRRG
# GGGGGGGGGGGGGGGGGGGGGRRRRG
# GRRRRGGGGGGGGGGGGGGGGRRRRG
# GFFRRGGGGGGGGGGGGGGGGRRRRG
# GLRRRGGGGGGGGGGGGGGGGRRRRG
# GRRRRGGGGGGGGGGGGGGGGDDDDG
# GRRRRRERRRRRRRBRRRRRRRRLLG
# GRRRRRERRRRRRRBRRRRRRRRRRG
# GLRRRRERRRRRGGBRRRRRRRRRRG
# GLLRRRERRRRRGGBRRRRRRRRRRG
# GGGGGGGGGGGGGGGGGGGGGGGGGG"""
#
# surface_width = 50
# surface_height = 50
#
# surface_positions = []
#
# for y, ligne in enumerate(string.split('\n')):
#     for x, char in enumerate(ligne):
#         if char != ' ':
#             surface_positions.append((x * surface_width, y * surface_height))
#
# # Deuxième code
# class Kart:
#     def __init__(self, kart_position):
#         self.kart_position = kart_position
#         self.speed = 0
#         self.theta = 0
#         self.v_theta = 0
#         self.a_c = 0
#
#     def update_position(self):
#         # Parcourir toutes les positions des surfaces et vérifier la collision
#         for surface_pos in surface_positions:
#             surface_rect = pygame.Rect(surface_pos[0], surface_pos[1], surface_width, surface_height)
#
#             if surface_rect.collidepoint(self.kart_position[0], self.kart_position[1]):
#                 f = 0.02
#                 self.speed = self.a_c + self.speed * math.cos(self.v_theta) * (1 - f)
#                 self.theta = self.theta + self.v_theta
#                 self.kart_position[0] = self.kart_position[0] + self.speed * math.cos(self.theta)
#                 self.kart_position[1] = self.kart_position[1] + self.speed * math.sin(self.theta)
#
#                 self.v_theta = 0
#                 self.a_c = 0
#                 break  # Sortir de la boucle si une collision est détectée
#
# # Votre instance de Kart
# kart = Kart([kart_x, kart_y])
#
# # Votre logique pour mettre à jour la position du kart et vérifier les collisions
# kart.update_position()