"""
Crear un programa que permita registrar las inscripciones de los alumnos de una universidad
privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de
nacimiento). Crear una variable que muestre True o False si posee título secundario (ese
dato no se pide al usuario, se escribe en el programa).
Además se deberá ingresar el monto de matrícula y calcular la cuota (valor de la matrícula +
$ 1000).
La materia "Python I" tiene un arancel especial, cuyo valor es $ 12000 por cuatrimestre.
Mostrar el costo mensual y calcular un descuento del 15% de la cuota para aquellos que
paguen en efectivo.
Finalmente se deberán imprimir todos los datos pedidos.

"""

nombre = input("Ingrese su Nombre : ")
apellido = input("Ingrese su Apellido: ")
edad = int(input("Ingrese su edad: "))
nacimiento= input("Fecha de Nacimiento: ")
matricula= int(input("Ingrese el monto de la matricula: $ "))

print("====================================================================================================================")
print("===============================  Universidad de Python - Inscripciones  ============================================")
print("====================================================================================================================")

print("================ Datos de Ingreso ===================")
print("Nombre Completo:" , nombre, apellido )
print(f"Fecha de Nacimiento y edad: {nacimiento} - {(edad)}")



posee_titulo=input("Posee titulo secundario? Si / No: ")

verdadero = "Si"
falso = "No"

verdadero_minuscula = verdadero.lower()
falso_minsucula = falso.lower()

if (posee_titulo == (verdadero_minuscula)):
    print("EXCELENTE!! Seguimos")
    print("Matricula:$ ",matricula)
    calculo_cuota = int(matricula) + 1000
    print("Cuota Mensual:$ " , + int(calculo_cuota))
    arancel_especial = 12000
    cuatrimeste = 4
    valor_mensual =int(arancel_especial) / int(cuatrimeste)
    print("Arancel mensual materia 'Python I':$ ", + float(valor_mensual))
    descuento = int(valor_mensual) * 15 / 100
    descuento1 = valor_mensual - descuento
    print("Arancel mensual materia 'Python I' con descuento: $ ", + float(descuento1))
else:
    print("Lo siento!! Debe regularizar su tramite \n")