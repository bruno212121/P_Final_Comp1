from items import *
from random import *

class Humano():
    def __init__(self, nombre):
        self.nombre = nombre  
        self.c = "Humano" 
        self.estadisticas = {
            "SALUD": 100, 
            "ATAQUE": 50,
            "DEFENSA": 20,
            "VELOCIDAD": 50,
            "EXPERIENCIA": 80,
            "NIVEL": 1,
            }
    def __str__(self):
        return "Nombre: {0} Clase: {1} Salud: {2} Ataque: {3} Defensa: {4} Velocidad: {5} Experiencia: {6} Nivel: {7}".format(
            self.nombre, 
            self.c, 
            self.estadisticas["SALUD"], 
            self.estadisticas["ATAQUE"], 
            self.estadisticas["DEFENSA"],
            self.estadisticas["VELOCIDAD"],
            self.estadisticas["EXPERIENCIA"],
            self.estadisticas["NIVEL"] 
            )
    def Ataque(self, enemigo):
        if enemigo.estadisticas["SALUD"] <= 0: 
            self.estadisticas.update(emp.get_itm())
            print("-->Felicidades has dropeado", emp.get_itm(), " y mejoraste tus atributos<---")
            items = ()
            while not items in ["EMBLEMA","PECHERA","BOTAS","POCION","ESPECIAL","emblema","pechera","botas","pocion","especial"]:
                items = input("¿Que item quieres mejorar? ")
                if items == ("EMBLEMA").lower():
                    self.estadisticas["ATAQUE"] = self.estadisticas["ATAQUE"] + 10
                    print("Has mejorado tu atributo ATAQUE")
                elif items == ("PECHERA").lower():
                    self.estadisticas["DEFENSA"] = self.estadisticas["DEFENSA"] + 20
                    print("Has mejorado tu atributo DEFENSA")
                elif items == ("BOTAS").lower():
                    self.estadisticas["VELOCIDAD"] = self.estadisticas["VELOCIDAD"] + 30
                    print("Has mejorado tu atributo VELOCIDAD")
                elif items == ("POCION").lower():
                    self.estadisticas["SALUD"] = self.estadisticas["SALUD"] + 5
                    print("Has mejorado tu atributo SALUD")
                elif items == ("ESPECIAL").lower():
                    self.estadisticas["VELOCIDAD"] = self.estadisticas["VELOCIDAD"] + 23
                    self.estadisticas["SALUD"] = self.estadisticas["SALUD"] + 23
                    print("Has mejorado tus atributos VELOCIDAD y SALUD")
                else:
                    print("No has mejorado tus atributos")
                    print("los atributos que se pueden mejorar son: EMBLEMA, GUANTES, PECHERA, BOTAS, POCION, ESPECIAL")    
        elif self.estadisticas["ATAQUE"] >= enemigo.estadisticas["DEFENSA"]:
            enemigo.estadisticas["SALUD"] -= self.estadisticas["ATAQUE"]
            print("\n Ataque certero de {0}, ahora la salud de {1} es de {2}".format(self.nombre,enemigo.nombre,enemigo.estadisticas["SALUD"]))
            self.estadisticas.update(emp.get_itm())
        
