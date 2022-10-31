from re import S
from humano import Humano
from mago import Mago
from paladin import Paladin


global nivel
global maximo

nivel = 1
maximo = 9

enemigos = [Mago("Mago"), Paladin("Paladin"), Humano("Humano")]

class Orco():
    def __init__(self):
        self.nombre = "Orco"
        self.nivel = nivel
        self.estadisticas = {
            "SALUD": 100,
            "ATAQUE": 50,
            "DEFENSA": 30,
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
            self.estadisticas["SALUD"] += 110
            self.estadisticas["ATAQUE"] += 10
            self.estadisticas["DEFENSA"] += 10
            print("El {0} volvio!!, ahora su nivel es de  {1}".format(self.nombre,self.nivel))
            print("Las estadisticas nuevas del {0}: \n Salud: {1} \n Ataque: {2} \n Defensa: {3}".format(self.nombre,self.estadisticas["SALUD"],self.estadisticas["ATAQUE"],self.estadisticas["DEFENSA"]))
        else:
            print("El orco ah llegado a su nivel maximo!!!")
            print("Felicitaciones, has ganado el juego")

    def Ataque(self,enemigos):
        if self.estadisticas["ATAQUE"] >= enemigos.estadisticas["DEFENSA"]: 
            enemigos.estadisticas["SALUD"] -= self.estadisticas["ATAQUE"] 
            print("\n Ataque certero de {0}, ahora la salud de {1} es de {2}".format(self.nombre,enemigos.nombre,enemigos.estadisticas["SALUD"]))
        else:
            print("El orco fallo su ataque contra {0}".format(enemigos.nombre))