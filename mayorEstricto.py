
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