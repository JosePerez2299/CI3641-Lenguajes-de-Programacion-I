# Sublistas Crecientes Iterator

Este programa implementa un iterador en Python que genera todas las sublistas crecientes a partir de una lista dada de enteros con elementos únicos. Por ejemplo, para la lista `[1, 4, 3, 2, 5]`, el iterador produce las siguientes sublistas crecientes:

- []
- [1]
- [1, 4]
- [1, 4, 5]
- [1, 3]
- [1, 3, 5]
- [1, 2]
- [1, 2, 5]
- [1, 5]
- [4]
- [4, 5]
- [3]
- [3, 5]
- [2]
- [2, 5]
- [5]

## Uso

Para utilizar el iterador, instancie la clase `SublistasCrecientesIterator` proporcionándole la lista de enteros. Luego, itere sobre la instancia para obtener las sublistas crecientes.

```python
# Ejemplo de uso
from SublistasCrecientesIterator import SublistasCrecientesIterator

lista = [1, 4, 3, 2, 5]

for sublista in SublistasCrecientesIterator(lista):
    print(sublista)
```

Este ejemplo imprimirá todas las sublistas crecientes generadas por el iterador a partir de la lista `[1, 4, 3, 2, 5]`.
