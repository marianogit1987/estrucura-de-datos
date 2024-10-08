"""
La universidad ahora pide un programa que permita cargar las notas de dos exámenes y
obtener el promedio. Además deberá determinar si el alumno aprobó el último examen
(nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre
ambos parciales. Para ello se deberá informar "Mejoró su desempeño" si la nota del
segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son
iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del
segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio
mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar.
"""

print("=======================Cargar Notas========================\n")
primer_parcial=input("Ingrese la nota del primer parcial: ")
segundo_parcial=input("Ingrese la nota del segundo parcial: ")
cantidad_parciales= 2
suma_parciales= int(primer_parcial) + int(segundo_parcial)
calculo_promedio= int(suma_parciales) / float(cantidad_parciales)
print("El promedio de las notas es: ", calculo_promedio)
if int(segundo_parcial)>=7:
    print("Aprobó el segundo parcial 😁")
else:
    print("No aprobó el segundo parcial 😢")

progreso=()
if int(segundo_parcial)>int(primer_parcial):
    print("Progreso del 1er al 2do parcial: Mejoró su desempeño 😎")
elif int(segundo_parcial)==int(primer_parcial):
    print("Progreso del 1er al 2do parcial: Mantuvo la nota 😊")
else:
    print("Progreso del 1er al 2do parcial: Empeoró su desempeño 😢")   

promocion=()
if float(calculo_promedio)>=7:
    print("Promocionó la Materia")
elif float(calculo_promedio)>=4:
    print("Debe recursar la materia\n")