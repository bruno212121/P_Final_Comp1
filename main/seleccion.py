from mago import Mago
from humano import Humano
from paladin import Paladin


def nuevo_personaje(creado): #Metodo para seleccionar la clase a jugar
        eleccion = ""
        aceptado = False
        while not aceptado:
            n = input("\n por favor ingresa el nombre del jugador:")
            aceptado = True
            for c in creado:
             if n == c.nombre:
                    aceptado = False
                    print("El nombre que ha introducido, ya esta creado")

        while not eleccion in ["h","p","m"]: 
            eleccion = input("\n Por favor selecciona la clase {0}. (H)umano, (P)aladin, (M)ago: ".format(n).lower()) 

        clase = {"h": "Humano", "p": "Paladin","m": "Mago"}

        if clase[eleccion] == "Humano":
            registro = Humano(n)
            print("\n Personaje creado con exito: ")
        elif clase[eleccion] == "Paladin":
            registro = Paladin(n)
            print("\n Personaje creado con exito: ")
        elif clase[eleccion] == "Mago":
            registro = Mago(n)
            print("\n Personaje creado con exito: ")
        else:
            print("No se ha seleccionado ninguna clase")
        print(registro)
        return  registro

def lucha(personajes): #Este es el metodo de lucha por turno
    print("--------------------- Comienza la batalla -----------------------\n")
    for c in personajes:
        print(c)
        print("")

    juego_terminado = False 
    turno = 0
    while not juego_terminado:
        print("Turno de {0} {1}. Selecciona un enemigo para atacar: ".format(personajes[turno].c,personajes[turno].nombre))
        partida = []
        for i in range (len(personajes)):
            if not i == turno:
                partida.append(i)
                print(" - ({0}): {1} nombrado {2} ".format(i, personajes[i].c,personajes[i].nombre))
        sel = -1
        while not sel in partida:
            s = input("Seleccion: ")
            try :
                sel = int(s)
            except:
                print("No es una opcion correcta")

        personajes[turno].Ataque(personajes[sel])
        if personajes[sel].estadisticas["SALUD"] <= 0:
            juego_terminado = True
            print("Juego terminado! {0} ha muerto.".format(personajes[sel].nombre))
        turno +=1
        if turno == len(personajes):
            turno = 0