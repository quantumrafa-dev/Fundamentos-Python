#Clase: Fundamentos de Programación
#Tema: 5. Bloques iterativos
#Ejercicio: 5.4.1. 
#Descripción: ¡Adivina el número!

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-31
#Estado: [Terminado]

#----------------
#Indicaciones:
# Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
# El programa debe seguir pidiendo números hasta que acierte. En cada
# intento fallido el programa notificará al usuario si el número secreto es
# mayor o menor al último valor ingresado.
# Entrada: • Números enteros entre 1 y 100.
# Salida:• Tres posibles salidas: “El número secreto es menor”, “El número secreto
# es mayor”, ¡Felicidades! Has adivinado el número secreto”
# Conceptos explorados:• Uso de bucles indefinidos

import random

numbers = [10,46,100,random.randint(1,100)]


numberfound = 0
wantstoplay = True
index = 0

while wantstoplay == True and index < len(numbers):
      numbertofind = numbers[index]
      numberfound = int(input("Ingresa un número entero entre 1 y 100: "))
      if numberfound == numbertofind: 
        print(f"¡Felicidades! Has adivinado el número secreto: {numbertofind}")
        answer = input("¿Quieres jugar de nuevo con el siguiente número (True/False)? ").capitalize()
        if answer == "True": 
           wantstoplay = True
           index += 1
        else: 
           wantstoplay = False
      elif numberfound < numbertofind: 
        print("Error, el número secreto es mayor")
      else: 
        print("Error, el número secreto es menor")

if index == len(numbers):
    print(" ¡Has adivinado todos los números secretos!")
else:
    print(" Gracias por jugar. ¡Hasta la próxima!")

