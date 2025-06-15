#Clase: Fundamentos de Programación
#Tema: 10. Manejo de matrices
#Ejercicio: 10.3.1. 
#Descripción: Matriz simétrica

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-06-14
#Estado: [Terminado]

#----------------
#Indicaciones:
# Dada una matriz cuadrada ingresada por el usuario,
# comprueba si la matriz cuadrada es simétrica respecto a su diagonal principal.
# Entrada:
# Número entero N con la dimensión de la matriz.
# N conjuntos de números enteros separados por coma.
# Salida:
# Una línea con una cadena de texto:
# "La matriz es simétrica" si es simétrica;
# "La matriz no es simétrica" en caso contrario.


dimension = int(input("Ingrese la dimensión de su matriz deseada: "))
counter = 1
matriz = []

for counter in range(1, dimension + 1):
    fila = list(map(int,input(f"Ingrese los datos de su fila {counter}: ").split(',')))
    matriz.append(fila)

symetrical = True
for i in range(dimension):
    for j in range(dimension):
        if matriz[i][j] != matriz[j][i]:
            symetrical = False
            break
if symetrical:
    print("\nLa matriz sí es simétrica")
else:
    print("\nLa matriz no es simétrica")
