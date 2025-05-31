#Clase: Fundamentos de Programación
#Tema: 6. Listas
#Ejercicio: 6.3.1 
#Descripción: Números líderes

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-30
#Estado: [Terminado]

#----------------
#Indicaciones:
# Un número en una lista es "líder" si es estrictamente mayor que todos los elementos
#a su derecha. Dada una lista de números ingresada por el usuario, imprime todos los
#números líderes
#Entrada: La primera línea contiene n enteros a1, ..., an (a<=a<=10^9)
#Salida: Una línea con todos los números líderes en el orden en que aparecen en el arreglo


numbers = list(map(int, input("Ingresa la lista de números que quieres evaluar: ").split()))
leaders = []
highest = -1

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > highest:
        leaders.append(numbers[i])
        highest = numbers[i]

leaders.reverse()

print(f"Estos son los números líderes: {leaders}")
