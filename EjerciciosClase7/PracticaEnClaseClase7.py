import numpy as np

#Crear una matriz a partir de una lista

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

#Crear una matriz de ceros

zeros = np.zeros(5)
print(zeros)

#Crear una matriz de unos
ones = np.ones(5)
print(ones)

#1.5.1. Suma
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2

#1.5.2. Multiplicación
resultado = arr1 * arr2

#1.6.2. jemplos de Broadcasting
arr = np.array([1, 2, 3])
result = arr + 5

#Ejemplo 2: Difusión de matrices unidimensionales y bidimensionales*

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2
