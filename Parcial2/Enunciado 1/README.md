# Programas en Python: Church.py y Arbol.py

Este repositorio contiene dos programas escritos en Python que implementan estructuras de datos y operaciones específicas.

## Programa: Church.py

### Clase Church

El archivo `Church.py` define la clase `Church`, que representa números naturales mediante la codificación de Church. La clase proporciona métodos para la sucesión, conversión a enteros y operaciones aritméticas como la suma y la multiplicación.

### Uso

El ejemplo incluido en el archivo demuestra cómo crear instancias de `Church`, realizar operaciones como la suma y multiplicación, y luego convertir los resultados a enteros para su visualización.

```python
# Ejemplo de uso
diez = Church.intToChurch(10)
dos = Church.intToChurch(2)

# Sumamos 10 + 2. Retorna 12 en Church, y lo convertimos a entero para mostrarlo en consola
print((diez + dos).toInt())

# Multiplicamos 10 * 2. Retorna 20 en Church, y lo convertimos a entero para mostrarlo en consola
print((diez * dos).toInt())
```

## Programa: Arbol.py

### Clase Arbol

El archivo `Arbol.py` define la clase `Arbol`, que representa un árbol binario con métodos para realizar recorridos en preorden y postorden. Además, incluye funciones para verificar si el árbol es un max-heap y si es simétrico.

### Uso

El ejemplo incluido en el archivo demuestra cómo crear un árbol y realizar algunas operaciones como verificar si es un max-heap, mostrar recorridos en preorden y postorden, y verificar si es simétrico.

```python
# Ejemplo de uso
a = Arbol(1,
        Arbol(1,
            Arbol(1),
            Arbol(1)
        ),
        Arbol(1,
            Arbol(1),
            Arbol(1)
        )
    )

print("Max Heap: ", a.esMaxHeap())
print("Preorder: ", a.preOrder())
print("Postorder: ", a.postOrder())
print("Max Heap Simetrico: ", a.esMaxHeapSimetrico())
```