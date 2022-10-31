from re import S
from humano import Humano
from mago import Mago
from paladin import Paladin


global nivel
global maximo

nivel = 2
maximo = 10

enemigos = [Mago("Mago"), Paladin("Paladin"), Humano("Humano")]

class Orco():
    def __init__(self):
        self.nombre = "Orco"
        self.nivel = nivel
        self.estadisticas = {
            "SALUD": 100,
            "ATAQUE": 50,
            "DEFENSA": 50,
        }
    def __str__(self):
        return "Nombre: {0} Nivel: {1} Salud: {2} Ataque: {3} Defensa: {4}".format(
            self.estadisticas["NOMBRE"],
            self.estadisticas["NIVEL"],
            self.estadisticas["SALUD"],
            self.estadisticas["ATAQUE"],
            self.estadisticas["DEFENSA"],
        )
    
    def Nivel(self):
        if self.nivel < maximo: 
            self.nivel += 1 
            self.estadisticas["SALUD"] += 100
            self.estadisticas["ATAQUE"] += 30
            self.estadisticas["DEFENSA"] += 40
            print("Has subido de nivel, ahora tu nivel es {0}".format(self.nivel))
        else:
            print("Has llegado al nivel maximo")

    def Ataque(self,enemigos):
        if self.estadisticas["ATAQUE"] <= enemigos.estadisticas["DEFENSA"]:
            enemigos.estadisticas["SALUD"] -= self.estadisticas["ATAQUE"]
            print("\n Ataque certero de {0}, ahora la salud de {1} es de {2}".format(self.nombre,enemigos.nombre,enemigos.estadisticas["SALUD"]))
            if self.estadisticas["SALUD"] <= 0: 
                self.Nivel() 
