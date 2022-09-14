#Personaje 2
from ProyectoFinal import Personajes

class paladin(Personajes):
    def __init__(self,nombre,edad,fuerza,destreza,temple):
        self.fuerza = fuerza
        self.destreza = destreza
        self.temple = temple