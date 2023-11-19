# Programa de Evaluación de Tiempos

Este programa evalúa y compara el tiempo de ejecución de tres implementaciones diferentes de una función F. La función F se define de acuerdo con la siguiente fórmula:

```math
F(n) = \begin{cases} 
n & \text{si } 0 \leq n < \alpha \cdot \beta \\
\sum_{i=1}^{\alpha} F(n - \beta \cdot i) & \text{en otros casos}
\end{cases}

```
## Archivos del Proyecto

1. **funciones.py:**
   Este archivo contiene tres implementaciones diferentes de la función F: recursiva, recursiva de cola e iterativa. Además, se define la función de sumatoria utilizada en las implementaciones.

2. **main.py:**
   Este archivo realiza la evaluación de tiempos para cada implementación de la función F utilizando diferentes valores de entrada. Luego, crea un gráfico comparativo de los tiempos de ejecución.

## Ejecución del Programa

1. **funciones.py:**
   Contiene la definición de la función F en sus tres variantes. Para utilizar estas funciones, simplemente impórtalas en tu script y utilízalas como se muestra en el ejemplo.

   ```python
   from funciones import f_iterativa, f_recursiva, f_recursiva_cola

   valor = 100
   resultado_iterativa = f_iterativa(valor)
   resultado_recursiva = f_recursiva(valor)
   resultado_recursiva_cola = f_recursiva_cola(valor)
   ```

2. **main.py:**
   Este script evalúa y compara los tiempos de ejecución de las implementaciones de la función F para diferentes valores de entrada. Asegúrate de tener matplotlib instalado antes de ejecutar el script.

   ```bash
   pip install matplotlib
   ```

   Luego, ejecuta el script:

   ```bash
   python main.py
   ```

   El resultado será un gráfico que compara los tiempos de ejecución de las implementaciones de la función F.

## Configuración Adicional

- **Límite de Recursión:**
   Se ha ajustado el límite de recursión utilizando `sys.setrecursionlimit(1000000000)` en el archivo `funciones.py` para permitir la ejecución de la implementación recursiva con valores más grandes. Asegúrate de tener suficiente memoria disponible antes de ajustar este límite.

## Notas Adicionales

- **Caché de Resultados:**
   La implementación recursiva utiliza la decorador `functools.cache` para almacenar en caché los resultados y mejorar el rendimiento al evitar cálculos redundantes.

- **Comparación Gráfica:**
   El script `main.py` genera un gráfico que compara los tiempos de ejecución de las implementaciones de la función F. Puedes ajustar los valores de entrada en la lista `valores_prueba` para adaptar la evaluación a tus necesidades.