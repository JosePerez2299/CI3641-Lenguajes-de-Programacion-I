# Codigo del enunciado 5 - Diagramas T
Programa que simula programas, intérpretes y traductores como los vistos al estudiar los diagramas de T

## Requisitos Previos

- Asegúrate de tener Python instalado en tu sistema. Puedes descargar Python desde [el sitio web oficial](https://www.python.org/downloads/).

## Pasos para Ejecutar el Programa

1. Clona este repositorio o descarga el código fuente en tu máquina.

2. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra el archivo `main.py` del programa principal.

3. Ejecuta el programa principal utilizando el siguiente comando:

```
python main.py
```

El programa se ejecutará y mostrará los resultados en la terminal.

## Interactuando con el programa cliente

El cliente de línea de comandos proporciona las siguientes funcionalidades:

1. **Definición de Programa Ejecutable**:
   - Sintaxis: `DEFINIR PROGRAMA <nombre> <lenguaje>`
   - Ejemplo: `DEFINIR PROGRAMA MiPrograma Python`
   - Descripción: Define un programa ejecutable con un nombre y el lenguaje en el que se ejecuta.

2. **Definición de Intérprete**:
   - Sintaxis: `DEFINIR INTERPRETE <lenguaje_base> <lenguaje>`
   - Ejemplo: `DEFINIR INTERPRETE Python LOCAL`
   - Descripción: Define un intérprete que puede interpretar un lenguaje base y convertirlo a otro lenguaje.

3. **Definición de Traductor**:
   - Sintaxis: `DEFINIR TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>`
   - Ejemplo: `DEFINIR TRADUCTOR Python LOCAL Java`
   - Descripción: Define un traductor que puede traducir un lenguaje base desde un lenguaje origen a un lenguaje destino.

4. **Verificación de Programa Ejecutable**:
   - Sintaxis: `EJECUTABLE <nombre>`
   - Ejemplo: `EJECUTABLE MiPrograma`
   - Descripción: Verifica si un programa ejecutable con el nombre especificado es ejecutable.

5. **Salir del Cliente**:
   - Sintaxis: `SALIR`
   - Descripción: Permite salir del cliente de línea de comandos.

## Instrucciones para Ejecutar las Pruebas
Este proyecto utiliza pytest para realizar pruebas unitarias. Asegúrate de tener pytest instalado en tu entorno Python.

### Requisitos Previos
- Tener Python instalado.
- Instalar pytest y coverage ejecutando el siguiente comando:
```
    pip install pytest
    pip install coverage
```

### Pasos para Ejecutar las Pruebas

1. Clona este repositorio o descarga el código fuente en tu máquina.

2. Abre una terminal o línea de comandos y navega hasta el directorio raíz del proyecto, donde se encuentra el archivo test_main.py.

3. Ejecuta las pruebas utilizando el siguiente comando:
```
coverage run -m pytest
coverage report
```

pytest ejecutará todas las pruebas definidas en test_diagrama.py y mostrará los resultados en la terminal.

### Autor

- Autor del Sistema Buddy System: José Pérez (Carnet 16-10882)

