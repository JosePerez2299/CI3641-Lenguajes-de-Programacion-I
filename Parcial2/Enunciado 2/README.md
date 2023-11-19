# Calculadora de Expresiones Aritméticas

Este repositorio contiene dos programas en Python relacionados con la evaluación y manipulación de expresiones aritméticas en notación prefija y postfija.

## Programa: expresiones.py

El archivo `expresiones.py` contiene una clase llamada `ExpresionesAritmeticas`, que proporciona métodos para evaluar expresiones en notación prefija y postfija, así como convertir entre estos formatos y la notación infija. La clase también incluye una función principal para interactuar con el usuario y realizar operaciones en tiempo real.

### Uso

Para ejecutar el programa principal, ejecuta el archivo `expresiones.py`. A continuación, se presentan algunas opciones de entrada:

1. **EVAL <orden> <expr>:** Evalúa una expresión aritmética en notación prefija o postfija.
2. **MOSTRAR <orden> <expr>:** Muestra la expresión aritmética en notación infija.
3. **SALIR:** Finaliza el programa.

## Programa: test_expresiones.py

El archivo `test_expresiones.py` contiene pruebas unitarias para validar la funcionalidad de la clase `ExpresionesAritmeticas`. Se utiliza el marco de pruebas `pytest` para ejecutar las pruebas automáticamente.

### Uso

Para ejecutar las pruebas, asegúrate de tener instalado `pytest`, `coverage` y ejecuta el archivo `test_expresiones.py`. Las pruebas evalúan la capacidad de la clase para realizar operaciones aritméticas y convertir entre diferentes notaciones.

```
coverage run -m pytest -v
coverage report
```


### Requisitos

- Python 3.x
- pytest (para ejecutar las pruebas)
- coverage

