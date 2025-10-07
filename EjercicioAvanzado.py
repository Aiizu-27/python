materias_inscritas = int(input("Introduzca el número de materias a las que esté inscrito o inscrita: "))
notas_materias = []

for i in range(materias_inscritas):
    numero = i + 1
    nota_materia = float(input(f"Introduzca la nota de la materia {numero}: "))
    notas_materias.append(nota_materia)

media_notas = sum(notas_materias) / materias_inscritas

if media_notas < 5:
    print(f"Tu media es de {media_notas:.2f} y tienes un insuficiente")
elif media_notas < 6:
    print(f"Tu media es de {media_notas:.2f} y tienes un suficiente")
elif media_notas < 7.5:
    print(f"Tu media es de {media_notas:.2f} y tienes un bien")
elif media_notas < 9:
    print(f"Tu media es de {media_notas:.2f} y tienes un notable")
elif media_notas < 10:
    print(f"Tu media es de {media_notas:.2f} y tienes un sobresaliente")
else:  # media_notas == 10
    print(f"Tu media es de {media_notas:.2f} y tienes un sobresaliente con mención honorífica")
