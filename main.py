from track import Track
from ai import AI
from human import Human
from kart import Kart

# Ci-dessous, il y a deux chaines de carateres qui decrivent le terrain : le premier est simple, tandis que le deuxième
# est plus complexe, conçu pour tester l'intelligence artificielle
string1 = """GGGGGGGGGGGGGGGGGGGGGGGGGG
GRRRRRRCRRRRRRRRRGRRRRRRRG
GRRRRRRCRRRRRRRRRGRRRRRRRG
GRRRRRRCRRRRRRRRRBRRRRRRRG
GRRRRRRCRRRRRRRRRBRRRRRRRG
GGGGGGGGGGGGGGGGGGGGGRRRRG
GLLLLLLLLLLLLLLLLLLLGRRRRG
GGGGGGLLLLLLLLLLLLLLGRRRRG
GFFFFGLLLLLLLLLLLLLLGRRRRG
GLLRRGLLLLLLLLLLLLLLGRRRRG
GRRRRGGGGGGGGGGGGGGGGDDDDG
GRRRRRERRRRRRRBRRRRRRRRLLG
GRRRRRERRRRRRRBRRRRRRRRRRG
GLRRRRERRRRRGGBRRRRRRRRRRG
GLLRRRERRRRRGGBRRRRRRRRRRG
GGGGGGGGGGGGGGGGGGGGGGGGGG"""

string2 = """GGGGGGGGGGGGGGGGGGGGGGGGGG
GRRRRRRRRRRRRRCRRBRRRRRRRG
GRRRRRRRRRRRRRCRRBRRRRRRRG
GRRRRRRRRRRBRRCRRRRRRRRRRG
GRRRRRRRRRRBRRCRRRRLLLLLRG
GGGGGGGGGGGGGGGGGGGLLRRRRG
GLLLLLLLLLLLLLLLLGGGGRRLLG
GGGGGGLLLLLLLLLLLLLLGRRRRG
GFFFFGLLLLLLLLLLLLLLLLLRRG
GGGRRGLLLLLLLLLLLLLLGRRRRG
GRRRRGGGGGGGGGGGGGGGGDDDDG
GRRRRRRRRERRRRRRBRRRRRRRRG
GRRRRRRRRERRRRRRGRRRRRRRRG
GGGRRRRRRERRRRRRGRRRRRRRRG
GGGRRRRRRERRRRRRBRRRRRRRRG
GGGGGGGGGGGGGGGGGGGGGGGGGG"""

string = string1

# La position et l'orientation initiale du kart
initial_position = [150, 150]
initial_angle = 0
controller = Human() # ou AI()

# Le code que nous avons développé permet également de participer à une course avec une intelligence artificielle
# controller2 = AI()
# kart2=Kart(controller2)
# ...
# track.add_kart(kart1)
"""
==================== ATTENTION =====================
Vous ne devez pas modifier ces quatre lignes de code 
====================================================
"""
kart = Kart(controller)
track = Track(string, initial_position, initial_angle)
track.add_kart(kart)
track.play()