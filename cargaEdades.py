

edad = 0
error = 0

while True:
    
    edad = int(input('Ingrese una edad mayor o igual a 18: '));
    

    while edad <18:
        edad = int(input('Error! Ingrese una edad mayor o igual a 18: '));
        error += 1
    print(f"La edad ingresada es: {edad}\nSe ha ingresado la edad erroneamente: {error}")
    break

    
       
           

 
    

        
        
