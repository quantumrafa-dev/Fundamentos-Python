#Clase: Fundamentos de Programación
#Tema: 2. Bloque condicional
#Ejercicio: 2.3.1
#Descripción: Contraseña segura

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
#cumple con las siguientes condiciones: tener al menos 8 caácteres, un número y una mayúscula
#Entrada: Una cadena de texto
#Salida:Dos posibles valores: "Contraseña Segura" o "Contraseña no segura"
#Restricciones: sin restricciones
#Sugerencias: investigar sobre los métodos isdigit() y isupper()
#----------------


password = input("Enter your password, please, ensure it complies with the requirements: ")

longitudgood = False
hasNumber = False
hasUpper = False

if len(password) >= 8:
  longitudgood = True


for i in password:
  if i.isdigit():
    hasNumber = True
  if i.isupper():
    hasUpper = True


if longitudgood == True and hasNumber == True and hasUpper == True:
  print("Contraseña segura")
else:
  print("Contraseña no segura")
