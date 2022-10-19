datos = {"Salud", 100 , "Ataque", 0 , "Defensa", 0} 

class Orco():
    def __init__(self):
        self.diccionario_orcos = {
            "Orco1": {datos},
            "Orco2": {datos},
            "Orco3": {datos},
            "Orco4": {datos},
            "Orco5": {datos},
            "Orco6": {datos},
            "Orco7": {datos},
            "Orco8": {datos},
            "Orco9": {datos},
            "Orco10": {datos},
        }
        self.estadisticas = {
            "SALUD": 100,
            "ATAQUE": 0,
            "DEFENSA": 0,
        }
    def __str__(self):
        return "Salud: {0} Ataque: {1} Defensa: {2}".format(
            self.estadisticas["SALUD"],
            self.estadisticas["ATAQUE"],
            self.estadisticas["DEFENSA"],
        )
    def Ataque(self,enemigo):
        if self.estadisticas["ATAQUE"] >= enemigo.estadisticas["DEFENSA"]:
