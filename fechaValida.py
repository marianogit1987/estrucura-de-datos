"""
Desarrollar una función que reciba tres números positivos y verifique si corresponde a una fecha válida(día, mes, año). Devolver True o False según la fecha sea corrscta o no. Realizar también un programa para verificar el comportamiento de la función.
"""

import datetime

def fecha(dia,mes,año):
    try:
        datetime.datetime(año,mes,dia)
        return True
    except ValueError:
        return False
    
dia = int(input('Ingrese un día: '))
mes = int(input('Ingrese un mes: '))
año = int(input('Ingrese un año: '))
    
if fecha(dia,mes,año):
    print('la fecha ingresada es válida')
else:
    print('la fecha ingresada no es válida')
    


    