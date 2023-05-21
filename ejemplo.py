import random

print("Juguemos piedra, papel o tijera.")
print("Las opciones son:\n1. Piedra\n2. Papel\n3. Tijera")

while True:
    # El usuario elige su opción
    jugador = int(input("Ingrese su elección (1-3): "))

    # La computadora elige su opción
    computadora = random.randint(1, 3)

    # Mostramos las opciones elegidas
    print(f"Tu elección fue: {jugador}")
    print(f"La elección de la computadora fue: {computadora}")

    # Comparamos las opciones y determinamos el ganador
    if jugador == computadora:
        print("Empate!")
    elif jugador == 1 and computadora == 3:
        print("Ganaste! Piedra gana a tijera.")
    elif jugador == 2 and computadora == 1:
        print("Ganaste! Papel gana a piedra.")
    elif jugador == 3 and computadora == 2:
        print("Ganaste! Tijera gana a papel.")
    else:
        print("Perdiste! La computadora gana.")

    # Preguntamos al usuario si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n)").lower()
    if jugar_de_nuevo != "s":
        break

print("¡Gracias por jugar!")