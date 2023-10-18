from Vector3d import Vector3d
import pytest
import math

vectorA = Vector3d(4, 5, 6)
vectorB = Vector3d(3, 2, 1)
vectorC = Vector3d(4, 5, 6)
vectorAfloat = Vector3d(4.4, 5.5, 6.6)
vectorBfloat = Vector3d(0.1, 0.2, 0.3)


def test_eq_vector():
    """
    Comprueba que un vector es igual a otro
    """
    assert vectorA == vectorC


def test_eq_vector_tipo_erroneo():
    """
    Comprueba que una excepción TypeError se genera cuando se compara un Vector3d con un tipo incorrecto.
    """
    with pytest.raises(TypeError):
        assert vectorA == 42


def test_suma_vectores():
    """
    Comprueba que la suma de dos vectores da el resultado esperado.
    """
    assert vectorA + vectorB == Vector3d(7, 7, 7)


def test_suma_vectores_con_float():
    """
    Comprueba que la suma de dos vectores con valores flotantes da el resultado esperado.
    """
    assert vectorAfloat + vectorBfloat == Vector3d(4.5, 5.7, 6.9)


def test_suma_vector_y_entero():
    """
    Comprueba que la suma de un Vector3d y un número flotante da el resultado esperado.
    """
    assert vectorAfloat + 1.1 == Vector3d(5.5, 6.6, 7.7)


def test_suma_vectores_con_tipo_erroneo():
    """
    Comprueba que una excepción TypeError se genera al sumar un Vector3d con un tipo incorrecto.
    """
    with pytest.raises(TypeError):
        assert vectorA + "invalid"


def test_resta_vectores():
    """
    Comprueba que la resta de dos vectores da el resultado esperado.
    """
    assert vectorA - vectorB == Vector3d(1, 3, 5)


def test_resta_vectores_con_float():
    """
    Comprueba que la resta de dos vectores con valores flotantes da el resultado esperado.
    """
    assert vectorAfloat - vectorBfloat == Vector3d(4.3, 5.3, 6.3)


def test_resta_vector_y_entero():
    """
    Comprueba que la resta de un Vector3d y un número flotante da el resultado esperado.
    """
    assert vectorAfloat - 1.1 == Vector3d(3.3, 4.4, 5.5)


def test_resta_vectores_con_tipo_erroneo():
    """
    Comprueba que una excepción TypeError se genera al restar un Vector3d con un tipo incorrecto.
    """
    with pytest.raises(TypeError):
        assert vectorA - ""


def test_str_vectores():
    """
    Comprueba que la representación de cadena de un Vector3d sea la esperada.
    """
    assert str(vectorA) == "(4, 5, 6)"


def test_producto_vectorial():
    """
    Comprueba que el producto vectorial de dos vectores da el resultado esperado.
    """
    assert vectorA * vectorB == Vector3d(-7, 14, -7)


def test_producto_vectorial_con_float():
    """
    Comprueba que el producto vectorial de dos vectores con valores flotantes da el resultado esperado.
    """
    assert vectorAfloat * vectorBfloat == Vector3d(0.33, -0.66, 0.33)


def test_producto_por_entero():
    """
    Comprueba que la multiplicación de un Vector3d por un número entero da el resultado esperado.
    """
    assert vectorA * 2 == Vector3d(8, 10, 12)


def test_producto_por_flotante():
    """
    Comprueba que la multiplicación de un Vector3d por un número flotante da el resultado esperado.
    """
    assert vectorA * 3.2 == Vector3d(12.8, 16.0, 19.2)


def test_producto_con_tipo_erroneo():
    """
    Comprueba que una excepción TypeError se genera al multiplicar un Vector3d con un tipo incorrecto.
    """
    with pytest.raises(TypeError):
        assert vectorA * "error"


def test_mod_vectores():
    """
    Comprueba que el producto punto entre dos vectores da el resultado esperado.
    """
    assert vectorA % vectorB == 28


def test_mod_vectores_con_float():
    """
    Comprueba que el producto punto entre dos vectores con valores flotantes da el resultado esperado.
    """
    assert math.isclose(vectorAfloat % vectorBfloat, 3.52)


def test_mod_vectores_con_tipo_erroneo():
    """
    Comprueba que una excepción TypeError se genera al calcular el producto punto con un tipo incorrecto.
    """
    with pytest.raises(TypeError):
        assert vectorA % True


def test_modulo_de_vector():
    """
    Comprueba que el módulo de un vector sea el resultado esperado.
    """
    assert ~vectorB == pytest.approx(3.74, abs=0.01)


def test_modulo_de_vector_con_valores_flotantes():
    """
    Comprueba que el módulo de un vector con valores flotantes sea el resultado esperado.
    """
    assert ~vectorBfloat == pytest.approx(0.374, abs=0.01)


if __name__ == "__main__":
    pytest.main()
