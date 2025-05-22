#Clase: Fundamentos de Programación
#Tema: 1. Variables, tipos, entradas y salidas
#Ejercicio: 1.3.1
#Descripción: Automatizando el cálculo de la propina

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Pide al usuario el total de una cuenta y el porcentaje de propina (por ejemplo, 10%, 15%, 20%)
#Calcula y muestra en pantalla el total a pagar.
#El formato de la salida debe ser (el ejemplo asume un total de $10 y el 10% de propina)
#Total de la cuenta: 10$
#Propina: $1
#Total de la cuenta con propina (10%): 11$
#----------------

amountPay = float(input("Ingresa el monto de tu factura a pagar: "))
tip = float(input("Ingrese el porcentaje del cuál quiere pagar la propina: "))
tipTotal = amountPay*tip/100

print(f"El total de su cuenta es: ${amountPay} y su propina escogida es del {tip}%, entonces su cuenta total es ${amountPay+tipTotal}")
