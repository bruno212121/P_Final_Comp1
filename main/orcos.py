from re import S


global nivel
global maximo

nivel = 0
maximo = 10

class Orco():
    def __init__(self):
        self.nombre = "Orco"
        self.nivel = nivel
        self.estadisticas = {
            "SALUD": 100,
            "ATAQUE": 0,
            "DEFENSA": 0,
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
            self.estadisticas["SALUD"] += 10
            self.estadisticas["ATAQUE"] += 10
            self.estadisticas["DEFENSA"] += 10
            print("Has subido de nivel, ahora tu nivel es {0}".format(self.nivel))
        else:
            print("Has llegado al nivel maximo")

    def Ataque(self,enemigo):
        if self.estadisticas["ATAQUE"] >= enemigo.estadisticas["DEFENSA"]: #Si el ataque del orco es mayor o igual a la defensa del mago
            enemigo.estadisticas["SALUD"] -= self.estadisticas["ATAQUE"]
            print("\n Ataque certero, ahora la salud de {0} es de {1}".format(enemigo.nombre,enemigo.estadisticas["SALUD"]))
            if self.estadisticas["SALUD"] <= 0: 
                print("Has derrotado a {0}".format(self.nombre))
                self.Nivel() 
            else:
                print("Has fallado el ataque")
        else:
            print("\n Fallaste el ataque") 
