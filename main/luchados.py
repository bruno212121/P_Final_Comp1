from seleccion import nuevo_personaje
from orcos import *

malo = Orco()


class Batalla():
    
    def __init__(self):
        self.personajes = personajes
        self.malo = malo
        self.opcion = 0

    def seleccion(personajes):
        print("Selecciona tu personaje")
        for i in range(len(personajes)):
            print("{0}. {1}".format(i+1,personajes[i].nombre))
            opcion = int(input("Selecciona tu personaje: "))
            return opcion

    def lucha(personajes,opcion,malo):
        print("--------------------- Comienza la batalla -----------------------\n")
        
        juego_terminado = False
        turno = 0
        
        while not juego_terminado:
            print("Turno de {0} {1} : ".format(self.opcion.c,self.opcion.nombre))
            partida = []

           
