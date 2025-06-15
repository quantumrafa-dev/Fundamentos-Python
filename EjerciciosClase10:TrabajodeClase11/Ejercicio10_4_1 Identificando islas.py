#Clase: Fundamentos de Programación
#Tema: 10. Manejo de matrices
#Ejercicio: 10.4.1. 
#Descripción: Identificando islas

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-06-14
#Estado: [Terminado]

#----------------
#Indicaciones:
# Dada una matriz binaria ingresada por el usuario (0 = agua, 1 = tierra),
# cuenta la cantidad de islas disponibles.
# Una isla está formada por elementos con valor de 1 conectados horizontal o verticalmente.
# Entrada:
# Dos números N, M con la dimensión de la matriz.
# N conjuntos de M cantidad de números enteros separados por coma.
# Salida:
# Un número entero con la cantidad de islas disponibles en la matriz.


rows = int(input("Ingrese la cantidad de filas : "))
columns = int(input("Ingrese la cantidad de columnas : "))

print("\nAhora ingrese los datos de la matriz fila por fila, separados por comas.")
print("Use solo 0 (agua) y 1 (tierra). Ejemplo: 1,0,1,1,0\n")

matrix = []
for i in range(1, rows + 1):
    row = list(map(int, input(f"Ingrese los datos de su fila {i}: ").split(',')))
    while len(row) != columns:
        print(f"  Error: Debe ingresar exactamente {columns} valores.")
        row = list(map(int, input(f"Intente de nuevo para fila {i}: ").split(',')))
    matrix.append(row)

def dfs(i, j):
    if i < 0 or i >= rows or j < 0 or j >= columns:
        return
    if matrix[i][j] == 0:
        return
    matrix[i][j] = 0
    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)

islas = 0
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 1:
            dfs(i, j)
            islas += 1

print(f"\nNúmero de islas encontradas: {islas}")
