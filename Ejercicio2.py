

def rimar():
    palabra1 = input("Introduzca una palabra a rimar: ")
    palabra2 = input("Introduzca una palabra a rimar: ")

    if palabra1[-3:]==palabra2[-3:]:
        print("Las palabras riman")
    elif palabra1[-2:]==palabra2[-2:]:
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman")


rimar()