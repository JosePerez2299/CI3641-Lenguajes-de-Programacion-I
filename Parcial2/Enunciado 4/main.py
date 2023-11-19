import time
import sys
import matplotlib.pyplot as plt
from funciones import f_iterativa, f_recursiva, f_recursiva_cola

sys.setrecursionlimit(1000000000)
# Definir la función que realiza la medición del tiempo
def medir_tiempo(funcion, valores):
    tiempos = []
    for valor in valores:
        inicio = time.time()
        funcion(valor)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

# Definir los valores de entrada para la prueba
valores_prueba = list(range(100, 40000, 120))

# Medir tiempos para cada implementación
tiempos_recursiva = medir_tiempo(f_recursiva, valores_prueba)
tiempos_recursiva_cola = medir_tiempo(f_recursiva_cola, valores_prueba)
tiempos_iterativa = medir_tiempo(f_iterativa, valores_prueba)

# Crear un gráfico comparativo
plt.figure(figsize=(10, 10))
plt.plot(valores_prueba, tiempos_recursiva, label='Recursiva')
plt.plot(valores_prueba, tiempos_recursiva_cola, label='Recursiva de Cola')
plt.plot(valores_prueba, tiempos_iterativa, label='Iterativa')

# Agregar etiquetas y leyenda al gráfico
plt.xlabel('Valor de Entrada')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución para Implementaciones de F')
plt.legend()

# Mostrar el gráfico
plt.show()
