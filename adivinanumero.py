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
    # creo un bucle que permita tener varios internos para poder jugar hasta adivinar el numero
    while True:
        numero_elegido = int(input("Adivina el numero ganador "))
        # Defino lo que quiero que se responda en la terminal, si has adivinado el numero o no
        if numero_elegido ==  numero:
            print("Enhorabuena Campeon")
            print ("Has necesitado ", Intentos, " intentos para adivinar el numero")
        elif numero_elegido < numero:
            print("Te has quedado corto")
        else:
            print("Te has pasado crack")
        Intentos += 1