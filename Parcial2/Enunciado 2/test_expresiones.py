import pytest
from expresiones import ExpresionesAritmeticas  # Reemplaza 'tu_modulo' con el nombre real de tu archivo

# Crear una instancia de la clase ExpresionesAritmeticas para usar en las pruebas
expresiones = ExpresionesAritmeticas()

# Pruebas unitarias
def test_evaluar_prefijo():
    assert expresiones.evaluar_prefijo('* 2 3') == 6  # Multiplicación simple
    assert expresiones.evaluar_prefijo('+ 9 6') == 15  # Suma simple
    assert expresiones.evaluar_prefijo('/ 8 4') == 2  # División simple
    assert expresiones.evaluar_prefijo('- 5 3') == 2  # Resta simple
    assert expresiones.evaluar_prefijo('+ * 2 3 4') == 10  # Operaciones anidadas
    assert expresiones.evaluar_prefijo('+ * + 3 4 5 7') == 42
    assert expresiones.evaluar_prefijo('- / 10 + 4 2 2') == -1

def test_evaluar_postfijo():
    assert expresiones.evaluar_postfijo('2 3 *') == 6  # Multiplicación simple
    assert expresiones.evaluar_postfijo('9 6 +') == 15  # Suma simple
    assert expresiones.evaluar_postfijo('8 4 /') == 2  # División simple
    assert expresiones.evaluar_postfijo('5 3 -') == 2  # Resta simple
    assert expresiones.evaluar_postfijo('2 3 * 4 +') == 10  # Operaciones anidadas
    assert expresiones.evaluar_postfijo('3 4 + 5 * 7 +') == 42
    assert expresiones.evaluar_postfijo('10 4 2 + / 2 -') == -1


def test_convertir_prefijo_infijo():
    # Casos de prueba sencillos
    assert expresiones.convertir_prefijo_infijo('+ 3 4') == '3 + 4'  # No hay operador infijo
    assert expresiones.convertir_prefijo_infijo('- 8 2') == '8 - 2'  # No hay operador infijo
    assert expresiones.convertir_prefijo_infijo('* / 3 5 2') == '(3 / 5) * 2'  # Operador no compatible
    assert expresiones.convertir_prefijo_infijo('3') == '3'  # Expresión sin operados
    assert expresiones.convertir_prefijo_infijo('+ * + 3 4 5 7') == '(3 + 4) * 5 + 7'
    assert expresiones.convertir_prefijo_infijo('- / 10 + 4 2 2') == '10 / (4 + 2) - 2'
    assert expresiones.convertir_prefijo_infijo('* - 6 3 + 2 1') == '(6 - 3) * (2 + 1)'
    assert expresiones.convertir_prefijo_infijo('/ + 8 2 - 6 4') == '(8 + 2) / (6 - 4)'

    assert expresiones.convertir_prefijo_infijo('+ - 4 2 * 3 5') == '4 - 2 + 3 * 5'
    assert expresiones.convertir_prefijo_infijo('/ + 8 2 - 6 4') == '(8 + 2) / (6 - 4)'

def test_convertir_postfijo_infijo():
    # Casos de prueba negativos
    assert expresiones.convertir_postfijo_infijo('3 4 +') == '3 + 4'  # No hay operador infijo
    assert expresiones.convertir_postfijo_infijo('8 2 -') == '8 - 2'  # No hay operador infijo
    assert expresiones.convertir_postfijo_infijo('3 5 / 2 *') == '(3 / 5) * 2'  # Operador no compatible
    assert expresiones.convertir_postfijo_infijo('3') == '3'  # Expresión sin operador
    assert expresiones.convertir_postfijo_infijo ('8 3 - 8 4 4 + * +') =='8 - 3 + 8 * (4 + 4)'
    assert expresiones.convertir_postfijo_infijo('3 4 + 5 * 7 +') == '(3 + 4) * 5 + 7'
    assert expresiones.convertir_postfijo_infijo('10 4 2 + / 2 -') == '10 / (4 + 2) - 2'
    assert expresiones.convertir_postfijo_infijo('6 3 - 2 1 + *') == '(6 - 3) * (2 + 1)'
    assert expresiones.convertir_postfijo_infijo('8 2 + 6 4 - /') == '(8 + 2) / (6 - 4)'
    assert expresiones.convertir_postfijo_infijo('4 2 - 3 5 * +') == '4 - 2 + 3 * 5'
    assert expresiones.convertir_postfijo_infijo('8 2 + 6 4 - /') == '(8 + 2) / (6 - 4)'

    