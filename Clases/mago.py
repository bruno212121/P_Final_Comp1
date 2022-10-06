class Mago():
    def __init__(self, nombre):
        self.nombre = nombre
        self.c = "Mago"
        self.estadisticas = {
            "SALUD": 100,
            "ATAQUE": 50,
            "DEFENSA": 20,
            "MAGIA": 100,
            "VELOCIDAD": 50,
            "LUCK": 50,
        }
    def __str__(self):
        return "Nombre: {0} Clase: {1} Salud: {2} Ataque: {3} Defensa: {4} Magia: {5} Velocidad: {6} Luck: {7}".format(
            self.nombre,
            self.c,
            self.estadisticas["SALUD"],
            self.estadisticas["ATAQUE"],
            self.estadisticas["DEFENSA"],
            self.estadisticas["MAGIA"],
            self.estadisticas["VELOCIDAD"],
            self.estadisticas["LUCK"]
        )
    def Ataque(self, enemigo):
        if self.estadisticas["ATAQUE"] >= enemigo.estadisticas["DEFENSA"]:
            enemigo.estadisticas["SALUD"] -= self.estadisticas["ATAQUE"]
            print("\n Ataque certero, ahora la salud de {0} es de {1}".format(enemigo.nombre,enemigo.estadisticas["SALUD"]))
        else:
            print("\n Fallaste el ataque")
