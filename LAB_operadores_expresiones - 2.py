# Pedir al usuario que ingrese la hora y minutos de inicio
hour = int(input("Ingrese la hora de inicio (0..23): "))
mins = int(input("Ingrese los minutos de inicio (0..59): "))

# Pedir al usuario que ingrese la duración del evento en minutos
dura = int(input("Ingrese la duración del evento en minutos: "))

# Calcular la hora y minutos finales del evento
hour = (hour + (mins + dura) // 60) % 24
mins = (mins + dura) % 60

# Mostrar la hora y minutos finales en consola
print(hour,":",mins)
