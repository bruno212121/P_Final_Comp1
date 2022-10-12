from ...Main import humano, paladin, mago

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
            registro = humano.Humano(n,clase[eleccion])
            print("\n Personaje creado con exito: ")
        elif clase[eleccion] == "Paladin":
            registro = paladin.Paladin(n,clase[eleccion])
            print("\n Personaje creado con exito: ")
        elif clase[eleccion] == "Mago":
            registro = mago.Mago(n,clase[eleccion])
            print("\n Personaje creado con exito: ")
        else:
            print("No se ha seleccionado ninguna clase")
        print(registro)
        return  registro

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