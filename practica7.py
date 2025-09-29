calificacion=int(input('Introduce la calificación del examen del 1 al 100: '))
if calificacion < 50:
    print('Tienes un insuficiente.')
elif 50 <= calificacion <= 69:
    print('Tienes un suficiente.')
elif 70 <= calificacion <= 84:
    print('Tienes un bien')
elif 85 <= calificacion <= 94:
    print('Tienes un notable')
else:
    print('Tienes un sobresaliente')
