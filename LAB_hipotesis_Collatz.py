numero = int(input("Ingrese un número natural: "))
contador_pasos = 0

while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
    contador_pasos += 1

print(numero)
print("Se alcanzó el objetivo en", contador_pasos, "pasos.")