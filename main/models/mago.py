#Personaje 3
from ProyectoFinal import Personajes
from .. import db 

class Mago(Personajes):
    def __init__(self,agilidad,magico):
        self.agilidad = agilidad
        self.magico = magico