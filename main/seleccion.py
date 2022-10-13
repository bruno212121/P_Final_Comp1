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
            eleccion = input("""\n Por favor selecciona la clase {0}. (H)umano
(H)UMANO: El humano es un guerrero que puede usar armas y armaduras, pero no puede usar magia.
Salud: 100
Ataque: 50
Defensa: 20
Velocidad: 50
Luck: 80
---------------------------
(P)ALADIN: El paladin es un guerrero que puede usar armas y armaduras, pero no puede usar magia.
Salud: 100
Ataque: 70
Defensa: 50
Velocidad: 30
Luck: 50
---------------------------
(M)ago: El mago es un guerrero que puede usar armas y magia, pero no puede usar armadura.
Salud: 90
Ataque: 50
Defensa: 20
Velocidad: 50
Luck: 50
MAGIA: 100
--------------------------- 
\n:""".format(n).lower()) 

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
