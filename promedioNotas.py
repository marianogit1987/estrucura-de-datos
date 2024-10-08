"""
Promedio de notas: cargar las notas de 5 alumnos y obtener el promedio (for). Nota: Al usar
for probar cómo se podría plantear el ejercicio usando 1, 2 o 3 parámetros.
"""


print("============================== Pomedios de Notas ==========================================")

suma_notas = 0

for i in range(5):
    nota= float(input(f"Ingrese la nota: "  ))
    suma_notas += nota
promedio_notas = suma_notas / 5
print(f"El promedio de notas es: {promedio_notas}")
