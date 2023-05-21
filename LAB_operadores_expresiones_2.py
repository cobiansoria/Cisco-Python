print("Se solucionara la siguiente expresion: 1x + 1/(x + 1/(x+1/x))")
x = float(input("Ingresa valor a x: "))

#operacion
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)