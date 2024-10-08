"""
Listado de aulas: desarrollar un programa que muestre en dos columnas el número de día y
el aula, de acuerdo al número de día par o impar desarrollado en el ejercicio anterior.
Imprimir el listado como el siguiente:
Día Aula
1 A-315
2 A-300
...
5 A-315
6 A-300
"""
print("====================================== Listado de Aulas ==========================================")
aula1 = "A-300"
aula2 = "A-315"

print("Dia" + "    " + "Aula")

for x in range(1,7):
    if x % 2 == 0:
        print( x , "    " , aula1)
    else:
        print( x , "    " , aula2)