#from main import nuevo_personaje, lucha
#from Clases import humano, paladin, mago
from Main import nuevo_personaje, lucha

def menu():
    personajes = []
    opcion = ""
    print("--- Bienvenido Juego de Combate LA CAIDA DEL REY I ---")
    while not opcion.lower() in ["q","p"]:
        opcion = input("\n(R)egistrar nombre\n(I)niciar combate\n(S)alir del juego\n\nPor favor escriba la opcion correcta: ").lower()

        if opcion == "i" and len(personajes) < 2:
            print("\n ->no puede jugar solo con un personaje, crea los personajes primero")

        elif opcion == "r":
            personajes.append(nuevo_personaje(personajes))
            opcion = ""
        elif opcion == "i":
            lucha(personajes)
        elif opcion == "s":
            print("\n !Gracias por jugar!, Hasta la proxima")

menu()
