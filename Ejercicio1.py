import random
import time

MAX_CUEVAS = 5
puntos = 0
perdido = False
cont=0
repetir=True

while repetir == True:
    while cont<MAX_CUEVAS and perdido==False:
        print("Te acercas a una entrada y ves 2 cuevas\n"
              "En una de ellas se encuetra un dragon amistoso y en otra un dragon malvado\n"
              "¿En cual entras? 1 ó 2")
        cueva = input()

        dragonBueno = random.randint(1, 2)
        print("Has entrado en la cueva de .....")
        time.sleep(1)
        if dragonBueno == int(cueva):
            print("Un dragon bueno\nTe da su tesoro")
            puntos += 100
        else:
            print("Un dragon malvado y te devora\n Has perdido\n")
            perdido = True
    print(f"Has obtenido {puntos} puntos")
    if input("¿Desea volver a jugar? ").lower().__eq__("si"):
        perdido = False
        puntos = 0
    else:
        repetir=False