#Clase: Fundamentos de Programación
#Tema: 2. Bloque condicional
#Ejercicio: 2.3.2 
#Descripción: Cálculo de impuesto

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Desarrollar un programa en Python que permita calcular el impuesto que debe pagar un
#usuario por el consumo de energía. El cálculo debe realizarse basado en la sigueinte tabla
#Entrada: unidades consumidas (entero)
#Salida: Impuesto aplicado($)
#Restricciones: sin restricciones
#0-100 = sin impuestos
#101-200 = 0.5$ por cada unidad
#201 o más 0.7$ por cada unidad


precioUnidad = 1.50

unidadesCompradas = int(input("How many units do you want to buy? "))

if unidadesCompradas <= 100:
  print(f"You do not have to pay any taxes, your final price is {unidadesCompradas*precioUnidad}")
elif unidadesCompradas<201:
  print(f"You have to pay $0.5 of tax per each unit, so your final price is {(precioUnidad*0.5)*unidadesCompradas}")
else:
  print(f"You have to pay $0.7 of tax per each unit, so your final price is {(precioUnidad*0.7)*unidadesCompradas}")