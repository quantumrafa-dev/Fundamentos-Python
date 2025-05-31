#Clase: Fundamentos de Programación
#Tema: 5. Bloques iterativos
#Ejercicio: 5.5.1. 
#Descripción: Generando patrones

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-05-31
#Estado: [Terminado]

#----------------
 #Indicaciones:
# Imprime el siguiente patrón usando bloques for/while:
# Salida:• Patrón solicitado.
# Restricciones:• No se puede imprimir de forma estática ninguna sección de lafigura.
# Conceptos explorados:• Bloques anidados y manejo de índices.


# For the top part
for row in range(1, 6):
    if row == 1 or row == 5:
        print( "  "+ "*" + " " + "_-_-_" + " " + "*")
    elif row == 2 or row == 4:
        print(" "+ "***" + " " + "-_-_-" + " " + "***")
    elif row == 3:
        print("*****"+ "_-_-_" + "*****")

# For the below part
for row in range(1, 6):
    if row == 1 or row == 5:
        print("_-_-_" + " " + "*" + " " + "_-_-_")
    elif row == 2 or row == 4:
        print("-_-_-" + " " + "***" + " " + "-_-_-")
    elif row == 3:
        print(" _-_-_ " + "*****" +" _-_-_ ")