import math
import pygame
import time
from controller import Controller

MAX_ANGLE_VELOCITY = 0.05
BLOCK_SIZE = 50


class AI(Controller):

    def __init__(self):
        Controller.__init__(self)

        # indct1 et indct2 sont des indicateurs
        self.indct1 = False
        self.indct2 = False
        self.indct3 = False

        # l'attribut i permet de parcourir le tableau de checkpoints
        self.i = 0
        self.tableaux_checkpoints_provisoirs = []

    @property
    def indct1(self):
        return self.__indct1

    @indct1.setter
    def indct1(self, value):
        self.__indct1 = value

    @property
    def indct2(self):
        return self.__indct2

    @indct2.setter
    def indct2(self, value):
        self.__indct2 = value

    @property
    def indct3(self):
        return self.__indct3

    @indct3.setter
    def indct3(self, value):
        self.__indct3 = value

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, value):
        self.__i = value

    @property
    def tableaux_checkpoints_provisoirs(self):
        return self.__tableaux_checkpoints_provisoirs

    @tableaux_checkpoints_provisoirs.setter
    def tableaux_checkpoints_provisoirs(self, value):
        self.__tableaux_checkpoints_provisoirs = value

    def move(self, string, x=0, y=0):

        # Trouver la position du checkpoint (x,y) si elle n'est pas indique lors de l'appelle de la méthode move
        # C-à-d dans le cas ou il n'y pas de checkpoint provisoir (récurssion), on cherche le vrai checkpoint
        if x == 0 and y == 0:
            # On crée une liste qui stocke les positions des caractères de next_checkpoint afin de l'utiliser
            # ensuite pour trouver la position de caratère le plus proche à notre kart
            liste_positions = []
            if self.kart.next_checkpoint_id == 0:
                char = 'C'
            elif self.kart.next_checkpoint_id == 1:
                char = 'D'
            elif self.kart.next_checkpoint_id == 2:
                char = 'E'
            elif self.kart.next_checkpoint_id == 3:
                char = 'F'

            for c in string:

                # Si on trouve le caractère correpsondant au checkpoint, on enregistre sa position et à la fin
                # de la boucle on prend le plus proche
                if c == char:
                    liste_positions.append([x, y])
                    # Afin de ne pas parcourir tout les caratères de string on fait cette condition
                    if len(liste_positions) == string.count(c):
                        break

                # Si on trouve le caractere de retour a la ligne "\n" on incremente y et on remet x a 0
                # Sinon on incremente x
                if c == "\n":
                    y += 1
                    x = 0
                else:
                    x += 1

            # indct1 devient True lorsque la méthode move est appelée sans les paramètres x et y
            # Ce qui signifie qu'on entre dans la condition de recherche d'un vrai checkpoint
            # Cet indicateur est ensuite utilisé avec la condition valid_move et indct2
            # Par exemple, si indct1 et valid_move sont tous les deux True, cela signifie que les coordonnées x, y
            # correspondent à un vrai checkpoint accessible.
            self.indct1 = True

            # On cherche la position la plus proche de caratère qui correspond au checkpoint
            x, y = min(liste_positions, key=lambda point: ((point[0] - self.kart.surface_position_x) ** 2 + (
                    point[1] - self.kart.surface_position_y) ** 2) ** 0.5)

        # x,y ici prennent la position de chechkpoint ou de checkpoint provisoir
        next_checkpoint_position = [x * BLOCK_SIZE + .5 * BLOCK_SIZE, y * BLOCK_SIZE + .5 * BLOCK_SIZE]

        # Ensuite, trouver l'angle vers le checkpoint
        relative_x = next_checkpoint_position[0] - self.kart.kart_position[0]
        relative_y = next_checkpoint_position[1] - self.kart.kart_position[1]

        # On utilise la fonction arctangente pour calculer l'angle du vecteur [relative_x, relative_y]
        next_checkpoint_angle = math.atan2(relative_y, relative_x)

        # L'angle relatif correspond a la rotation que doit faire le kart pour se trouver face au checkpoint
        # On applique l'operation (a + pi) % (2*pi) - pi pour obtenir un angle entre -pi et pi
        relative_angle = (next_checkpoint_angle - self.kart.theta + math.pi) % (2 * math.pi) - math.pi

        # Si x,y sont accessibles depuis la position actuelle de kart on passe la command selon relative_angle
        # Si non, on appelle la méthode move (réccursion) qui prend comme x,y la position de checkpoint provisoir
        if self.valid_move(string, relative_x, relative_y, next_checkpoint_angle):

            # indct2 permet de déterminer si kart était en train de parcourir les checkpoints provisoires
            # En résumé, si les trois conditions sont satisfaites, cela signifie que nous avons détecté que
            # le vrai checkpoint est devenu accessible
            if self.indct1 and self.indct2:
                # Réinitialisation
                self.indct2 = False
                self.indct3 = False
                # On règle la vitesse à 2 pour assurer une fluidité optimale, afin d'éviter tout contact avec la lave
                self.kart.speed = 2

            # Enfin, commander le kart en fonction de l'angle
            if relative_angle > MAX_ANGLE_VELOCITY:
                # On tourne a droite
                command = [False, False, False, True]
            elif relative_angle < -MAX_ANGLE_VELOCITY:
                # On tourne a gauche
                command = [False, False, True, False]
            else:
                # On avance seulement si le chemin est libre
                command = [True, False, False, False]
        else:

            # z devient True
            self.indct2 = True
            # Réinitialisation
            self.indct1 = False

            # Si la kart est dans un checkpoint, on appelle la méthode qui donne la liste des checkpoints provisoirs
            # Si non si la kart a attendu le checkpoint provisoir on arrete kart au niveau de ce checkpoint provisoir
            # Et on incrémente i pour passer au deuxième checkpoint
            if string.split('\n')[self.kart.surface_position_y][self.kart.surface_position_x] in ['C', 'D', 'E',
                                                                                                  'F'] and self.indct3 == False:
                self.tableaux_checkpoints_provisoirs = self.cherche_provisoir_checkpoint(string, x, y)
                # à chaque appelle de la méthode cherche_provisoir_checkpoint on réinitialise i et on active z
                self.i = 0
            elif self.tableaux_checkpoints_provisoirs[self.i] == [self.kart.surface_position_x,
                                                                  self.kart.surface_position_y]:
                self.i += 1
                self.kart.speed = 0

            return self.move(string, *self.tableaux_checkpoints_provisoirs[self.i])

        key_list = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        keys = {key: command[i] for i, key in enumerate(key_list)}
        time.sleep(0.02)
        return keys

    # Cette méthode permet de vérifier si un checkpoint est accesible depuis la position de kart
    def valid_move(self, string, relative_x, relative_y, next_checkpoint_angle):

        # Taille du pas pour la vérification des obstacles
        step_size = 5
        valid_move = True

        # Cette boucle permet de tester la validité des cases vers le checkpoint
        for i in range(0, int(math.hypot(relative_x, relative_y)), step_size):
            next_x = int((self.kart.kart_position[0] + i * math.cos(next_checkpoint_angle)) / BLOCK_SIZE)
            next_y = int((self.kart.kart_position[1] + i * math.sin(next_checkpoint_angle)) / BLOCK_SIZE)

            if string.split('\n')[next_y][next_x] in ['L', 'G']:
                valid_move = False
                break
        return valid_move

    # Cette méthode renvoie une liste de checkpoints provisoirs dans le cas ou
    # il y'a des obstacles entre le vrai checkpoint et la position de kart
    def cherche_provisoir_checkpoint(self, string, x, y):
        liste_checkpoints_provisoirs = []

        # Afin de ne pas appellé la fonction plusieurs fois indct3 = True veut dire c'est bon on a déterminé notre liste
        self.indct3 = True

        # Initialisation
        checkpoint_provisoir_x = self.kart.surface_position_x
        checkpoint_provisoir_y = self.kart.surface_position_y

        # Les puissances permettent de parcourir les circuits en zegzag
        puissance1 = 1
        puissance2 = 1
        puissance3 = 1
        puissance4 = 1

        # Tant que le checkpoint provisoir n'a pas attendu le vrai checkpoint
        # on continu notre série de checkpoints provisoirs
        while True:
            if checkpoint_provisoir_x < x and checkpoint_provisoir_y <= y:
                dx = 1 * puissance1
                dy = 1
                puissance1 *= -1
            if checkpoint_provisoir_x <= x and checkpoint_provisoir_y > y:
                dx = 1 * puissance2
                dy = -1
                puissance2 *= -1
            if checkpoint_provisoir_x >= x and checkpoint_provisoir_y < y:
                dx = -1 * puissance3
                dy = 1
                puissance3 *= -1
            if checkpoint_provisoir_x > x and checkpoint_provisoir_y >= y:
                dx = -1 * puissance4
                dy = -1
                puissance4 *= -1

            # Si on a déja passé par un des cas précédents
            test_x, checkpoint_provisoir_x = self.cherche_dans_direction_x(string, checkpoint_provisoir_x,
                                                                           checkpoint_provisoir_y, dx)
            liste_checkpoints_provisoirs.append([checkpoint_provisoir_x, checkpoint_provisoir_y])
            if test_x:
                return liste_checkpoints_provisoirs

            test_y, checkpoint_provisoir_y = self.cherche_dans_direction_y(string, checkpoint_provisoir_x,
                                                                           checkpoint_provisoir_y, dy)
            liste_checkpoints_provisoirs.append([checkpoint_provisoir_x, checkpoint_provisoir_y])
            if test_y:
                return liste_checkpoints_provisoirs

    @staticmethod
    def cherche_dans_direction_x(string, checkpoint_provisoir_x, checkpoint_provisoir_y, dx):
        while not string.split('\n')[checkpoint_provisoir_y][checkpoint_provisoir_x] in ['L', 'G']:
            checkpoint_provisoir_x += dx
            # Si on atteint un vrai checkpoint, on sort
            if string.split('\n')[checkpoint_provisoir_y][checkpoint_provisoir_x] in ['C', 'D', 'E', 'F']:
                return True, checkpoint_provisoir_x
        checkpoint_provisoir_x -= dx
        return False, checkpoint_provisoir_x

    @staticmethod
    def cherche_dans_direction_y(string, checkpoint_provisoir_x, checkpoint_provisoir_y, dy):
        while not string.split('\n')[checkpoint_provisoir_y][checkpoint_provisoir_x] in ['L', 'G']:
            checkpoint_provisoir_y += dy
            if string.split('\n')[checkpoint_provisoir_y][checkpoint_provisoir_x] in ['C', 'D', 'E', 'F']:
                return True, checkpoint_provisoir_y
        checkpoint_provisoir_y -= dy
        return False, checkpoint_provisoir_y
