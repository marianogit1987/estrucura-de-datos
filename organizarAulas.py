"""
La universidad requiere un programa para organizar las aulas para los alumnos de primer
año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
a. Aulas: Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los
días cuyo número de orden son pares los alumnos cursan en el aula A-300,
mientras que aquellos días impares cursan en el aula A-315
"""


print("======================================== Aulas =======================================\n")
aula1="A-300"
aula2="A-315"


numero_ingresado = int(input("Ingrese el número del dia: 1(lunes) a 6(sábado): "))

#verificar si es numero par o impar
if numero_ingresado % 2 == 0:
    print("Aula: ",aula1)
else:
    print("Aula: ",aula2)
    
    
"""
b. Descuento: Además se requiere un programa que otorgue un descuento especial del
25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y
se inscriban a más de 3 materias, para el resto de los casos el descuento será de un
5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
c. Estacionamiento: También se requiere que el programa asigne un costo diario de
estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50
si vienen en bicicleta.
"""


print("============================ Descuentos y estacionamiento ===========================\n")
turno_tarde = "Tarde"
turno_mañana = "Mañana"
turno_noche = "Noche"

turno_mañana_minuscula =turno_mañana.lower()
turno_tarde_minuscula = turno_tarde.lower()
turno_noche_minuscula = turno_noche.lower()

descuento_especial = 25
descuento2 = 5
valor_cuota = 4400
cantidad_materias=int()



ingreso_turno = input("Ingrese el turno: Mañana, Tarde o Noche: ")

if ingreso_turno == (turno_tarde_minuscula):
    cantidad_materias = int(input("Ingrese la cantidad de materias: "))
#Calculo aplicado para la inscrpcion de + de 3 materias
    calculo_especial = int(valor_cuota) * float(descuento_especial) / 100
    valor_calculo_especial = int(valor_cuota) - int(calculo_especial)
#Calculo aplicado para la inscripcion hasta 3 materias
    calculo_noespecial = int(valor_cuota) * float(descuento2) / 100
    valor_calculo_noespecial = int(valor_cuota) - int(calculo_noespecial)
if (cantidad_materias) > 3:
    print("El valor de la cuota es: ",valor_calculo_especial)
elif(cantidad_materias):
    print("El valor de la cuota es: ",valor_calculo_noespecial)

    
if ingreso_turno == (turno_mañana_minuscula):
    print("El valor de la cuota es:",valor_cuota)
elif ingreso_turno == (turno_noche_minuscula):
    print("El valor de la cuota es: ",valor_cuota)
    

    
auto = "Auto"
moto = "Moto"
bici = "Bici"

auto_minuscula = auto.lower()
moto_minuscula = moto.lower()
bici_minuscula = bici.lower()

valor_auto = 300
valor_moto = 300
valor_bici = 50
    
ingrese_vehiculo = input("Ingrese el vehiculo en el que ingresa: Auto / Moto / Bicicleta\n")
if ingrese_vehiculo == (auto_minuscula):
    print("El costo de estacionamiento para Auto es: ",valor_auto)
elif ingrese_vehiculo == (moto_minuscula):
    print("El costo de estacionamiento para Moto es: ",valor_moto)
elif ingrese_vehiculo == (bici_minuscula):
    print("El costo de estacionamiento para Bicicleta es: ",valor_bici)
