"""
Costo del comedor: Finalmente se pide calcular el costo del comedor. La cuota vale $ 1250
por día y se desea imprimir un informe que muestre la cantidad de días (de 1 a 6) y el costo
total (for). Por ejemplo: 1 día cuesta $ 1250, 2 días cuestan $ 2500…
"""

print("===================================== Costo del Comedor ====================================")
suma = 1250

print ("Dia" + "   " + "Costo")

for dia in range(1,7):
    suma_total = suma * dia 
    print(f"{dia}"  + "     " + f"$ {suma_total}")