#Clase: Fundamentos de Programación
#Tema: 2. Bloque condicional
#Ejercicio: 2.4.1 
#Descripción: El número mágico

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Crea un programa en Python para determinar si un numero es magico
#Un numero es magico si es divisible por 7 pero no por 5
#Entrada: un entero n
#Salida: Magico o Normal
#Restricciones 1<= n <= 10^18


number = int(input("Enter the number you wanna test: "))

if number%7==0 and number%5!=0:
 print("Magic number")
else:
  print("Normal number")