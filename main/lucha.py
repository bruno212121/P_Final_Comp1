from seleccion import nuevo_personaje

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
        while not sel in partida: #Este es el metodo de seleccion de enemigo
            s = input("Seleccion: ") 
            try :
                sel = int(s)
            except:
                print("No es una opcion correcta")

        personajes[turno].Ataque(personajes[sel]) 
        if personajes[sel].estadisticas["SALUD"] <= 0: 
            juego_terminado = True
            print("Juego terminado! {0} ha muerto.".format(personajes[sel].nombre))
        else:
            personajes[sel].estadisticas["EXPERIENCIA"] = personajes[sel].estadisticas["EXPERIENCIA"] + 10
            personajes[sel].estadisticas["NIVEL"] = personajes[sel].estadisticas["NIVEL"] + 1
            print("La experiencia de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["EXPERIENCIA"]))
            print("El personaje {0} subio de nivel {1}:".format(personajes[sel].nombre,personajes[sel].estadisticas["NIVEL"]))
            nivel = ""
            while not nivel in ["SALUD","DEFENSA","VELOCIDAD","ATAQUE","salud","defensa","velocidad","ataque"]:
                nivel = input("ingrese el atributo que desea subir de nivel: ")
                if nivel == ("SALUD").lower():
                    personajes[sel].estadisticas["SALUD"] = personajes[sel].estadisticas["SALUD"] + 10
                    print("La salud de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["SALUD"])) 
                elif nivel == ("ATAQUE").lower():
                    personajes[sel].estadisticas["ATAQUE"] = personajes[sel].estadisticas["ATAQUE"] + 10
                    print("El ataque de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["ATAQUE"]))
                elif nivel == ("DEFENSA").lower():
                    personajes[sel].estadisticas["DEFENSA"] = personajes[sel].estadisticas["DEFENSA"] + 10
                    print("La defensa de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["DEFENSA"]))
                elif nivel == ("VELOCIDAD").lower():
                    personajes[sel].estadisticas["VELOCIDAD"] = personajes[sel].estadisticas["VELOCIDAD"] + 10
                    print("La velocidad de {0} es de {1}".format(personajes[sel].nombre,personajes[sel].estadisticas["VELOCIDAD"]))
                else:
                    print("No es una opcion correcta")
                    print("Los atributos que puedes utilizar son: Salud, Ataque, Defensa, Velocidad")
            
        turno +=1
        if turno == len(personajes):
            turno = 0
