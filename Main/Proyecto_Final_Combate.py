from Clases import humano, paladin, mago

"""
class personajes:
    def __init__(self, nombre="",clase="Humano",estadisticas=[1,50,5,5,0,'True']):
        self.clase = clase
        self.nombre = nombre
        self.estadisticas = {"Nivel": estadisticas[0],"SALUD": estadisticas[1], "Ataque": estadisticas[2], "Defensa": estadisticas[3], "Experiencia": [4], "VIVO" : estadisticas[5]}

    def __repr__(self): #Este metodo lo que hace hacer una propia representacion de los strings de las clases
        salida = ""
        salida += "Nombre del personaje: {0} con su clase elegida {1}: \n --- Estadisticas inicializadas ---- ".format(self.nombre, self.clase)
        for k, v in self.estadisticas.items(): #Con este for hace el recorrido de las estadisticas iniciales y las muestra la jugador.
            salida += "\n {0}: {1}".format(k,v)
            return salida
    def calculo_nivel(self): # Sistema de leveo de los personajes
        self.estadisticas["Nivela"] = int(self.estadisticas["Experiencia"] **.5)+1

    def ataque(self,enemigo):
        print("\n{0} poder lanzado a {1} with {2} ataque. {1} tiene {3} defensa.".format(self.nombre,enemigo.nombre,self.estadisticas["Ataque"],enemigo.estadisticas["Defensa"]))

        if self.estadisticas["Ataque"] >= enemigo.estadisticas["Defensa"]:
            enemigo.estadisticas["Salud"] -= self.estadisticas["Ataque"]
            print("\n Ataque certero, ahora la salud de {0} es de {1}".format(enemigo.nombre,enemigo.estadisticas["Salud"]))
        else:
            print("\n Fallaste el ataque")
"""
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

        registro = personajes(n,clase[eleccion])
        print("\n Personaje creado con exito: ")
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

