from seleccion import nuevo_personaje
from lucha import lucha

def menu():
    personajes = []
    opcion = ""
    print("--- Bienvenido Juego de Combate LA CAIDA DEL REY I --- \n -> PARA PODER JUGAR DEBES CREAR DIEZ ENEMIGOS <-")
    while not opcion.lower() in ["q","p"]: 
        opcion = input("\n(R)egistrar nombre\n(I)niciar combate\n(S)alir del juego\n\nPor favor escriba la opcion correcta: ").lower()

        if opcion == "i" and len(personajes) < 2:
            print("\n ->no puede jugar solo con un personaje, crear al menos diez enemigos para iniciar el combate")

        elif opcion == "r":
            personajes.append(nuevo_personaje(personajes))
            opcion = ""
        elif opcion == "i":
            lucha(personajes)
        elif opcion == "s":
            print("\n !Gracias por jugar!, Hasta la proxima")
            opcion = "q"
        else:
            print("\n ->Opcion incorrecta, intente de nuevo")

menu()
