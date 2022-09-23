#Personaje 1
from ProyectoFinal import Personajes



class Humano(Personajes):
    def __init__(self,fuerza,inteligencia):
        self.fuerza = fuerza
        self.inteligencia = inteligencia