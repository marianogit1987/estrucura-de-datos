"""
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único(mayor estricto). En caso de no existir mayor estricto devolver - No utilizar operadores lógicos (AND, OR, NOT). Desarrollar también un programa para ingresar los tres valores, invocar a la funcion y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""


def mayorEstricto(*valores):
    numeroMaximo = max(valores)
    contador = sum(1 for valor in valores if valor == numeroMaximo)
    
    if contador == 1:
        return numeroMaximo
    else:
        return "Inexistente"
    
numeros=[]

for i in range(1,4):
    num=0
    while num <=0:
        num = int(input(f'Ingrese un numero positivo: '))
    numeros.append(num)
    
maxNum = mayorEstricto(*numeros)

print(f'El mayor estricto es: {maxNum}')