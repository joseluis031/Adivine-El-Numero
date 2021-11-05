# voy a pedirle al ordenador que escoja un numero, aleatoriamente entre 0 y 99
import random
numero = random.randint(0, 100)
self = numero

class Juegonumeroaleatorio:
    def Como_conseguir_un_numero_aleatorio():
        return random.randint()
    def Como_empieza_el_juego():
        random_number = self.random.randint()
        print()
        f'Adivina el numero ganador'
        
    Intentos = 0
    while True:
        numero_elegido = int(input("Adivina el numero ganador "))
        if numero_elegido ==  numero:
            print("Enhorabuena Campeon")
            break
        elif numero_elegido < numero:
            print("Te has quedado corto")
        else:
            print("Te has pasado crack")
        Intentos += 1

    print ("Has necesitado ", Intentos, " intentos para adivinar el numero")