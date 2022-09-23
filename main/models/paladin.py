#Personaje 2
from ProyectoFinal import Personajes
from .. import db 

class Paladin(Personajes):
    def __init__(self,fuerza,destreza,temple):
        self.fuerza = fuerza
        self.destreza = destreza
        self.temple = temple