

dinero = float(input("Introduzca dolares: "))
interes = float(input("Introduzca una tasa de interes:"))
tiempo = float(input("Introduzca numero de años: "))

tasa = dinero * pow((1+interes/100),tiempo)

print(tasa)