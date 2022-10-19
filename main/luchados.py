from seleccion import nuevo_personaje
from orcos import *

def lucha(personajes): #Este es el metodo de lucha por turno
    print("--------------------- Comienza la batalla -----------------------\n")
    for c in personajes:
        print(c)
        print("")
    juego_terminado = False
    turno = 0
    while not juego_terminado:
        for i in range(len(personajes)):
            print("Seleccionar personaje para luchar: {0} {1} ".format(i, personajes[i].c,personajes[i].nombre))
        sel = -1
        while not sel in Orco:
            
