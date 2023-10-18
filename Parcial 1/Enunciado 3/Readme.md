# Código del Enunciado 3 - BuddySystem: Sistema de Asignación de Bloques de Memoria

Este es un sistema de asignación de bloques de memoria implementado en Python utilizando el algoritmo de Buddy System. Permite la asignación y liberación de bloques de memoria, así como la visualización de los bloques libres y ocupados.

## Requisitos Previos

Asegúrate de tener Python 3.x instalado en tu sistema.

## Instrucciones de Uso

1. Clona o descarga el repositorio que contiene el código del sistema Buddy System.
2. Asegúrate de que los archivos `BuddySystem.py`, `Block.py`, `main.py`, y el archivo de pruebas unitarias (`test_buddy_system.py`) estén en la misma carpeta.

## Ejecución del Programa Cliente

El programa cliente te permite interactuar con el sistema Buddy System y realizar las siguientes acciones:

- Reservar un bloque de memoria: `RESERVAR <cantidad> <nombre>`
- Liberar un bloque de memoria: `LIBERAR <nombre>`
- Mostrar la representación visual de los bloques: `MOSTRAR`
- Salir del programa: `SALIR`

Para ejecutar el programa cliente, sigue estos pasos:

1. Abre una terminal en la carpeta que contiene el programa cliente (`main.py`).

2. Ejecuta el programa cliente con el siguiente comando:

```bash
python main.py
```

3. El programa te pedirá que ingreses el tamaño de la memoria en bytes.

4. A partir de este punto, puedes ingresar las acciones disponibles según las instrucciones proporcionadas. El programa te dará retroalimentación sobre las operaciones realizadas.

## Ejecución de Pruebas Unitarias

El sistema Buddy System incluye pruebas unitarias para garantizar su correcto funcionamiento. Puedes ejecutar las pruebas utilizando `pytest` y `coverage`. Asegúrate de que ambos estén instalados en tu entorno y luego ejecuta las pruebas de la siguiente manera:

1. Abre una terminal en la carpeta que contiene el archivo de pruebas unitarias (`test_buddy_system.py`).

2. Ejecuta las pruebas con el siguiente comando:

```bash
coverage run -m pytest -v
coverage report
```

## Autor

- Autor del Sistema Buddy System: José Pérez (Carnet 16-10882)
