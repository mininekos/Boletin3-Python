import random
import time

MAX_CUEVAS = 5
puntos = 0
perdido = False
cont=0

print("*****************************************************************")
print("*                    El reino del dragón                        *")
print("*****************************************************************")
time.sleep(1)
def entrar():
    print("Te acercas a una entrada y ves 2 cuevas\n"
          "En una de ellas se encuetra un dragon amistoso y en otra un dragon malvado\n"
          "¿En cual entras? 1 ó 2")
    cuevaSeleccionada=input();
    return cuevaSeleccionada

while cont<MAX_CUEVAS and perdido==False:

    cueva=entrar()
    dragonBueno = random.randint(1, 2)
    print("Has entrado en la cueva de .....")
    time.sleep(1)
    if dragonBueno == int(cueva):
        print("Un dragon bueno\nTe da su tesoro")
        puntos += 100
    else:
        print("Un dragon malvado y te devora")
        perdido = True


print(f"Has obtenido {puntos} puntos")
