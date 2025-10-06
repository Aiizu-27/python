materias_inscritas = int(input("Introduzca el número de materias a las que esté inscrito o inscrita: "))
notas_materias = []
for i in range(materias_inscritas):
    numero = i + 1
    nota_materia = int(input(f"Introduzca la nota de la materia {numero}:
 "))
    notas_materias.append(nota_materia)
    i + 1

print (notas_materias)
