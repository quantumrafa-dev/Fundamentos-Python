#Clase: Fundamentos de Programación
#Tema: 6. Listas
#Ejercicio: 6.2.1 
#Descripción: Eliminando valores duplicados

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-30
#Estado: [Terminado]

#----------------
#Indicaciones:
#Dada una lista ingresada por el usuario, elimina los elementos duplicados
#manteniendo la primera aparición de cada número
#Entrada: La primera línea contiene n enteros a1, ..., an(1<=a, <=10^6)
#Salida: Una línea con los enteros únicos en su orden de aparición, separados por espacios

numbersinput = input("Enter the list of numbers you want to evaluate (separated by spaces): ").split()

numbersfinal = [int(i) for i in numbersinput]

finalNumbers = []

for i in numbersfinal:
    if i not in finalNumbers:
        finalNumbers.append(i)

print(finalNumbers)