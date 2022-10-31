from seleccion import nuevo_personaje
from luchados import *

def menu():
    personajes = []
    opcion = ""
    print("--- Bienvenido Juego de Combate LA CAIDA DEL REY I --- \n -> PARA PODER JUGAR DEBES CREAR TRES PERSONAJES <-")
    while not opcion.lower() in ["q","p"]: 
        opcion = input("\n(R)egistrar nombre\n(I)niciar combate\n(S)alir del juego\n\nPor favor escriba la opcion correcta: ").lower()

        if opcion == "i" and len(personajes) < 3:
            print("\n ->no puede jugar con tan pocos personajes, crear al menos tres personajes para iniciar")
        elif opcion == "r" and len(personajes) == 3:
            print("no se pueden crear mas personajes")
        elif opcion == "r":
            personajes.append(nuevo_personaje(personajes))
            opcion = ""
        elif opcion == "i":
            batalla(personajes)
        elif opcion == "s":
            print("\n !Gracias por jugar!, Hasta la proxima")
            opcion = "q"
        else:
            print("\n ->Opcion incorrecta, intente de nuevo")

menu()
