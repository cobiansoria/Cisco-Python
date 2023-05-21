 # Se lee la palabra ingresada
espati = input("Ingresa el nombre de una flor: ")
 
# Comprobamos si es la palabra ESPATIFILO (Mayusculas)
if espati == "ESPATIFILO":
    print("Si - El Espatifilo! es la mejor planta de todos los tiempos")
# Comprobamos si es la palabra espatifilo (minusculas)
elif espati == "espatifilo":
    print("No, quiero un gran 'Espatifilo!!!'")
# Comprobamos si es una palabra diferente a ESPATIFILO
else:
    print("Espatifilo!, No", espati)