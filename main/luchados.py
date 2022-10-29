from seleccion import nuevo_personaje
from orcos import *
import os,time


malo = Orco()

def limpiar():
    os.system("cls")

class Batalla():
    
    def __init__(self,personajes):
        self.personajes = personajes
        self.malo = malo
        self.opcion = 0

    def seleccion(personajes):
        print("Selecciona tu personaje")
        for i in range(len(personajes)):
            print("{0}. {1}".format(i+1,personajes[i].nombre))
            opcion = int(input("Selecciona tu personaje: "))
            return opcion

    def lucha(self,personajes,malo):
        print("--------------------- Comienza la batalla -----------------------\n")
        
        juego_terminado = False
        turno = 0
        
        while not juego_terminado:
            print("Turno de {0} {1} : ".format(self.opcion.c,self.opcion.nombre))
            partida = []
            for i in range(len(personajes)):
                if not i == turno:
                    partida.append()
                    print(" - ({0}): {1} nombrado {2}".format(i, personajes[i].c,personajes[i].nombre))
            sel = -1

        while personajes[sel].estadisticas["SALUD"] > 0 and malo.estadisticas["SALUD"] > 0:
            limpiar()
            print("-----------------------------------------")
            print(sel)
            print("----------------------------------------")
            print(malo)
            print("----------------------------------------")
            print("Es turno de atacar de  {0} ".format(personajes[sel].nombre))
            select = personajes[sel]
            malo.estadisticas["SALUD"] -= personajes[sel].Ataque
            print("Atacando")
            time.sleep(1)
            if personajes[sel].estadisticas["SALUD"] <= 0 and malo.estadisticas["SALUD"] <=0:
                break
            print("turno de ", malo.NOMBRE)
            personajes[sel].estadisticas["SALUD"] -= malo.Ataque
            print(malo.nombre,"esta empezando a atacar")
            print("Atacando..")
            time.sleep(1)
            if personajes[sel].estadisticas["SALUD"] <= 0 and malo.estadisticas["SALUD"] <=0:
                break
        if personajes[sel].estadisticas["SALUD"] > 0:
            print("GANO", personajes[sel].nombre)
        else:
            print("GANO", malo.nombre)





           
