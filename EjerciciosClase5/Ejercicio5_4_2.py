#Clase: Fundamentos de Programación
#Tema: 5. Bloques iterativos
#Ejercicio: 5.4.2. 
#Descripción: Sumador de valores posicionales

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-31
#Estado: [Terminado]

#----------------
#Indicaciones:
# Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
# Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
# Entrada:• Un numero entero.
# Restricciones:• 1 ≤ número ≤ 10^9
# Conceptos explorados:• Bucles y control de flujo.

number= input("Ingresa un número entero: ")


number = list(number)
numberfound = 0

while len(number) > 1:
    numberfound = sum(int(i) for i in number)
    print("".join(number),"=", numberfound)
    number = list(str(numberfound))

print(f"El resultado final es: {numberfound}")