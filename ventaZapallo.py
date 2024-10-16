precioZapallo = 1000.0
producto = ['Zapallo']
divisas = {'dolares':0.95, 'yenes':0.85, 'guaranies':0.80, 'pesos':0.90, 'otra moneda':1.10} #Guardo el descuento o incremento a aplicarse
print('============================= Venta de Zapallos: $1000 cada uno =================================================')

print(F'Descuento según el pago con diferentes divisas:\nDólares: 5% OFF\nYenes: 15% OFF\nGuaraníes: 20% OFF\nPesos: 10% OFF\notra moneda: 10% AUMENTO')
print('==================================================================================================================')
print('Producto: Zapallo')
print('Precio: $ 1000.0')

cantidad = int(input('Cantidad: '))
operacion = cantidad * precioZapallo
PagoDivisas = input('Pago de Moneda: ')

while True: #Pedir ingreso de la divisa
    if PagoDivisas in divisas.keys():
        print('Pago en: ',PagoDivisas)
        break
    else:
        print('Error! Intenete Nuevamente')
        
if PagoDivisas == 'otra moneda': #Aplica incremento o descuento segun la divisa elegida anteriormente
    print(f'Incremento del {round((divisas[PagoDivisas]-1)*100)}%')
else:
    print(f'Descuento del {round((1-divisas[PagoDivisas])*100)}%')
    
print('================ Ingrese los datos para emitir el recibo ============================')
nombre = input('Ingrese su nombre: ')
nombreEmpresa = input ('Nombre de la empresa: ')
print('Cantidad de zapallos: ',cantidad)
precioTotal = cantidad * precioZapallo*divisas[PagoDivisas]

print(f'============================ Recibo ==========================================\nNombre: {nombre}\nNombre de la Empresa: {nombreEmpresa}\nTipo de Moneda, {PagoDivisas}\nCantidad: {cantidad}\nProducto: {producto[0]}\nTotal a Pagar: ${precioTotal}')



