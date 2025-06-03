#Clase: Fundamentos de Programación
#Tema: 7. Introducción al manejo de datos tabulares con NumPy
#Ejercicio: Tarea 10
#Descripción: Casos de Estudio, Consumo Energetico

#Autor: Rafael Alfonso Ruíz García 
#Fecha: 2025-06-03
#Estado: [Terminado]

import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# #Exploración inicial de los datos
# print("Dimensiones:", consumo.ndim) #2 (filas y columnas)
# print("Forma:", consumo.shape)
# print("Tipo de datos: ",consumo.dtype)
# print("Consumo primer hogar:", consumo[0])
# print("Consumo el miércoles (día 3):", consumo[:,2])

# #Promedio de consumo por hogar
# promedio_por_hogar = np.mean(consumo, axis=1)

# #Promedio de consumo diario de todos los hogares
# promedio_por_dia = np.mean(consumo, axis = 0)

# #Suma total de consumo en la semana de los 10 hogares
# total_consumo = np.sum(consumo)

# print(promedio_por_hogar)
# print(promedio_por_dia)
# print(total_consumo)

# #Maximo por hogar
# maximos = np.max(consumo, axis=1)

# #Minimo por dia
# minimos = np.min(consumo, axis=0)

# #Desviacion estandar global
# desviacion = np.std(consumo)

# print(maximos)
# print(minimos)
# print(desviacion)

# #Suma por hogar (semana)
# consumo_total_hogar = np.sum(consumo, axis=1)
# #Indice del hogar con mayor consumo
# hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# #Indice del hogar con mejor consumo
# hogar_mas_eficiente = np.argmin(consumo_total_hogar)

# print(consumo_total_hogar)
# print(hogar_mayor_consumo)
# print(hogar_mas_eficiente)

# #Suma por hogar (semana)
# consumo_total_hogar = np.sum(consumo, axis=1)
# print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")
# #Compara cada hogar con un valor mayor a 100
# altos = consumo_total_hogar > 100
# #Filtrando hogares que cumplen la condicion:
# consumo_mayor_100 = np.where(altos)[0]

# print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

# # #Aplicando normalizacion MinMax al conjunto de datos
# # consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# # #Resultado
# print(consumo_normalizado)

#Todo esto anterior fue comentado para evitar confuciones en mi codigo

print("Estas son las respuestas del cuestionario de trabajo")
# Pregunta 1
consumo_hogar5_viernes = consumo[4, 4]
print("Pregunta 1: Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)

# Pregunta 2
consumo_ultimos3_domingo = consumo[7:, 6]
print("Pregunta 2: Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_domingo)

# Pregunta 3
fines_de_semana = consumo[:, 5:7]  # columnas 5 y 6
promedio_fines_de_semana = np.mean(fines_de_semana)
print("Pregunta 3: Promedio de consumo en fines de semana:", promedio_fines_de_semana)

# Pregunta 4
desviaciones_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviaciones_por_dia)
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Pregunta 4: Desviaciones estándar por día:", desviaciones_por_dia)
print("Día con mayor desviación estándar entre hogares:", dias_semana[dia_mayor_desviacion])

# Explicación: este día tiene más variación en el consumo entre los hogares. Es decir, algunos consumen mucho y otros poco, sin uniformidad.

# Pregunta 5
consumo_total_hogar = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print("Pregunta 5: Índices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("Valores de consumo de esos hogares:", valores_menor_consumo)

# Pregunta 6
hogar3_original = consumo[2]
hogar3_aumentado = hogar3_original * 1.10
nuevo_total_hogar3 = np.sum(hogar3_aumentado)
print("Pregunta 6: Nuevo consumo total semanal del hogar 3 (con 10% de aumento):", nuevo_total_hogar3)
