#Clase: Fundamentos de Programación
#Tema: 1. Variables, tipos, entradas y salidas
#Ejercicio: 1.3.2
#Descripción: Generador del correo de Key

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-22
#Estado: [Terminado]

#----------------
#Indicaciones:
#Solicita al usuario su nombre completo (asume dos nombres y
#dos apellidos). Luego, el programa generará, su correo con el formato:
#primer_nombre.primer_apellido@keyinstitute.edu.sv
#Finalmente, el programa mostrará en pantalla el siguiente
#mensaje:
#El correo que se debe asignar al usuario ingresado es:
#nombre.apellido@keyinstitute.edu.sv

#----------------

firstName = str(input("Bienvenido al instituto Key, para comenzar ingresa tu primer nombre: "))
secondName = str(input("Ahora ingresa tu segundo nombre: "))
firstLastName = str(input("Ahora ingresa tu primer apellido: "))
secondLastName = str(input("Ahora ingresa tu segundo apellido: "))
email = firstName.lower() + "." + firstLastName.lower() + "@keyinstitute.edu.sv"


input(f"Excelente, tu correo electrónico nuevo es {email}")