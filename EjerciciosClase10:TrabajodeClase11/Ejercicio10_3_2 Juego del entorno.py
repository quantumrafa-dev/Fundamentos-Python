#Clase: Fundamentos de Programación
#Tema: 10. Manejo de matrices
#Ejercicio: 10.3.2. 
#Descripción: Juego del entorno

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-06-14
#Estado: [Terminado]

#----------------
#Indicaciones:
# Dada una matriz binaria ingresada por el usuario,
# verifica para cada celda de una matriz binaria cuántos elementos con valor de 1
# hay en las celdas vecinas (arriba, abajo, izquierda, derecha, diagonales).
# Entrada:
# Dos números N, M con la dimensión de la matriz.
# N conjuntos de M cantidad de números enteros separados por coma.
# Salida:
# Matriz NxM. Cada celda contiene la suma de elementos con valor de 1
# en las celdas vecinas.


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

directions = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]

result = []
for i in range(rows):
    row_result = []
    for j in range(columns):
        counter = 0
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < columns and matrix[x][y] == 1:
                counter += 1
        row_result.append(counter)
    result.append(row_result)

print("\nLa matriz resultado es (cantidad de 1s vecinos por celda):")
for row in result:
    print(row)
