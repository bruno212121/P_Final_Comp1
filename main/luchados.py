from seleccion import nuevo_personaje
from orcos import *
import os,time

malo = Orco()

def limpiar():
    os.system("cls") 


def batalla(personajes):

    for c in personajes:
        print(c)
        print("")
    
        juego_terminado = False

    while not juego_terminado:

        print("Seleciona personaje para la batalla: ")
        partida = []
        for i in range (len(personajes)):
            partida.append(i)
            print(" - ({0}): {1} nombrado {2} ".format(i, personajes[i].c,personajes[i].nombre)) 
        sel = -1 
        while not sel in partida:
            s = input("Seleccion: ") 
            try :
                sel = int(s)
            except:
                print("No es una opcion correcta")
        print("--------------------- Comienza la batalla -----------------------\n")
        if personajes[sel].estadisticas["SALUD"] <= 0:
            print("El personaje esta muerto, no puede participar en la batalla")
            break
        while not malo.estadisticas["SALUD"] <= 0 and not personajes[sel].estadisticas["SALUD"] <= 0: 
            if personajes[sel].estadisticas["SALUD"] > 0:
                personajes[sel].Ataque(malo)
                time.sleep(1)
            else:
                print("El personaje fallo en su ataque") 
            if malo.estadisticas["SALUD"] > 0:
                malo.Ataque(personajes[sel])
                time.sleep(1)
            else:
                print("El orco se ha quedado sin salud")      
            if malo.estadisticas["SALUD"] <= 0:   
                print("Felicitaciones! {0} ha muerto.".format(malo.nombre))
                malo.Nivel()
                nivel = " "
                while not nivel in ["SALUD","DEFENSA","VELOCIDAD","ATAQUE","salud","defensa","velocidad","ataque"]:
                    nivel = input("ingrese el atributo que desea subir de nivel: ")
                    if nivel == ("SALUD").lower():
                        personajes[sel].estadisticas["SALUD"] = personajes[sel].estadisticas["SALUD"] + 100
                        print("La salud de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["SALUD"])) 
                    elif nivel == ("ATAQUE").lower():
                        personajes[sel].estadisticas["ATAQUE"] = personajes[sel].estadisticas["ATAQUE"] + 10
                        print("El ataque de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["ATAQUE"]))
                    elif nivel == ("DEFENSA").lower():
                        personajes[sel].estadisticas["DEFENSA"] = personajes[sel].estadisticas["DEFENSA"] + 10
                        print("La defensa de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["DEFENSA"]))        
                    elif nivel == ("VELOCIDAD").lower():
                        personajes[sel].estadisticas["VELOCIDAD"] = personajes[sel].estadisticas["VELOCIDAD"] + 10
                        print("La velocidad de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["VELOCIDAD"]))    
                    else:
                        print("No es una opcion correcta")
                        print("Los atributos que puedes utilizar son: Salud, Ataque, Defensa, Velocidad")       
           
            elif personajes[sel].estadisticas["SALUD"] <= 0:
                print("OH NO {0} AH MUERTO!!!.".format(personajes[sel].nombre))
                print("GAME OVER")
                juego_terminado = True 
            
            elif malo.estadisticas["SALUD"] <= 0 and malo.nivel == maximo: 
                print("HAS GANADO LA BATALLA!!!!!")
                juego_terminado = True
        

        






           
