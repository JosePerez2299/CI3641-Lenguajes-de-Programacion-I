# Archivo de prueba: test_manejador.py
from Manejador import Manejador
from Clase import Clase
import pytest

# Fixture para inicializar el manejador antes de cada prueba
@pytest.fixture
def manejador():
    return Manejador()

def test_definir_clase(manejador):
    result = manejador.definir("ClaseA", ["metodoA"], None)
    assert "Se creo exitosamente la clase ClaseA" in result
    assert manejador.describir("ClaseA") == "metodoA -> ClaseA :: metodoA"

def test_definir_clase_con_padre(manejador):
    manejador.definir("ClasePadre", ["metodoPadre"], None)
    result = manejador.definir("ClaseHija", ["metodoHija"], "ClasePadre")
    assert "Se creo exitosamente la clase ClaseHija" in result
    assert manejador.describir("ClaseHija") == (
        "metodoHija -> ClaseHija :: metodoHija\nmetodoPadre -> ClasePadre :: metodoPadre"
    )

def test_definir_clase_repetida(manejador):
    manejador.definir("ClaseRepetida", ["metodoA"], None)
    result = manejador.definir("ClaseRepetida", ["metodoB"], None)
    assert "La clase 'ClaseRepetida' ya esta definida" in result

def test_describir_clase_no_existente(manejador):
    result = manejador.describir("ClaseInexistente")
    assert "La clase 'ClaseInexistente' no esta definida" in result

def test_definir_clase_con_padre_no_existente(manejador):
    result = manejador.definir("ClaseHija", ["metodoHija"], "ClasePadreInexistente")
    assert "La super clase 'ClasePadreInexistente' no esta definida" in result