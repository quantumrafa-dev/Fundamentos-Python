#Clase: Fundamentos de Programación
#Tema: 1. Variables, tipos, entradas y salidas
#Ejercicio: 1.4.1
#Descripción: División con precisión

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Dados tres enteros a, b y k. Imprime el resulta de a/b con k decimales exactos (sin redondear)
#Entrada: a y b (-10 <= a, b<= 10), k (1 <= 1000)
#Salida: Una cadena con la división exacta, incluyendo k decimales (truncados)
#Restricciones: No es posible dar formato utilizano {:.{k}f} para redondear los decimales
#----------------


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b (distinto de 0): "))
k = int(input("Ingrese la cantidad de decimales que desea mostrar: "))

division = a // b
residual = abs(a % b)
b = abs(b)

decimals = ""
for i in range(k):
  residual *= 10
  decimals += str(residual // b)
  residual = residual % b

if (a < 0 and b > 0) or (a > 0 and b < 0):
  print(f"{'-'}{abs(division)}.{decimals}")
else:
  print(f"{division}.{decimals}")
