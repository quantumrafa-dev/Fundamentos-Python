#Clase: Fundamentos de Programación
#Tema: 10. Manejo de matrices
#Ejercicio: 10.2.1
#Descripción: Diagonal principal y secundaria

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-06-14
#Estado: [Terminado]

#----------------
#Indicaciones:
# Dada una matriz cuadrada ingresada por el usuario,
# crea dos listas, una con los elementos de la diagonal principal
# y la otra con los elementos de la diagonal secundaria.
# Entrada:
# Número entero N con la dimensión de la matriz.
# N conjuntos de números enteros separados por coma.
# Salida:
# Dos listas, una con los elementos de la diagonal principal
# y la otra con los elementos de la diagonal secundaria.

dimension = int(input("Ingrese la dimensión de su matriz deseada: "))
counter = 1
matriz = []

for counter in range(1, dimension + 1):
    fila = list(map(int,input(f"Ingrese los datos de su fila {counter}: ").split(',')))
    matriz.append(fila)

principal_diagonal = [matriz[i][i] for i in range(dimension)]
secondary_diagonal = [matriz[i][dimension - 1-i] for i in range(dimension)]

print("\nla diagonal principal es:", principal_diagonal)
print("\nFinalmente, la diagonal secundaria es:", secondary_diagonal)