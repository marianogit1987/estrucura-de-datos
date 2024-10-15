



totalCompra = float(input('Total de compras: $ '))
dineroRecibido = float(input('Dinero recibido: $ '))

def calcularVuelto(totalCompra, dineroRecibido):
    if dineroRecibido < totalCompra:
        return 'Dinero recibido es Insuficiente'

    cambio = dineroRecibido - totalCompra
    
#Denominacion billetes    
    billetes = [500,100,50,20,10,5,1]
    resultado = {}
    
#Calcula la cantidad de cada billete
    for billete in billetes:
        cantidadBilletes = cambio // billete
        if cantidadBilletes > 0:
            resultado[billete] = int(cantidadBilletes)
            cambio %= billete
        
    return resultado

#llama a la función y almacena el resultado
cambio = calcularVuelto(totalCompra, dineroRecibido)

#imprime el resultado
if isinstance(cambio, dict):
        print('El vuelto es:')
        for billete, (cantidad) in cambio.items():
            print(f"$ {billete}: {cantidad} billete(s)")
else:
    print(cambio)