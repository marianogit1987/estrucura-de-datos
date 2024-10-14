"""
 Carga de edades: se desea mejorar el sistema de carga de edades, validando que
correspondan a mayores de edad. Desarrollar un programa que solicite edades válidas e
imprima la edad ingresada y cuántas cargas erróneas se realizaron
"""



print('=============================== Cargas Edades ===============================================')

edad = 0
error = 0

while True:
    
    edad = int(input('Ingrese una edad mayor o igual a 18: '));
    

    while edad <18:
        edad = int(input('Error! Ingrese una edad mayor o igual a 18: '));
        error += 1
    print(f"La edad ingresada es: {edad}\nSe ha ingresado la edad erroneamente: {error}")
    break

    
       
           

 
    

        
        
