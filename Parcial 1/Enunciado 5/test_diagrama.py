import pytest
from Diagrama import Diagrama

# Caso de prueba para el método 'interprete' de la clase 'Diagrama'
def test_interprete():
    diagrama = Diagrama()
    result = diagrama.interprete("Python", "LOCAL")
    # Comprobamos si se definió un intérprete correctamente
    assert result == "Se definió un intérprete para 'LOCAL', escrito en 'Python'"

# Caso de prueba para el método 'traductor' de la clase 'Diagrama'
def test_traductor():
    diagrama = Diagrama()
    result = diagrama.traductor("Python", "LOCAL", "Java")
    # Comprobamos si se definió un traductor correctamente
    assert (
        result == "Se definió un traductor de 'LOCAL' hacia 'Java', escrito en 'Python'"
    )

# Caso de prueba para el método 'insertar_ejecutable' de la clase 'Diagrama'
def test_insertar_ejecutable():
    diagrama = Diagrama()
    result = diagrama.insertar_ejecutable("MiPrograma", "Python")
    # Comprobamos si se definió un programa ejecutable correctamente
    assert result == "Se definió el programa 'MiPrograma', ejecutable en 'Python'"

# Caso de prueba para el método 'es_ejecutable' de la clase 'Diagrama' (cuando el programa no es ejecutable)
def test_no_es_ejecutable():
    diagrama = Diagrama()
    result = diagrama.es_ejecutable("MiPrograma")
    # Comprobamos que no es posible ejecutar el programa
    assert result == "No es posible ejecutar el programa 'MiPrograma'"

# Caso de prueba para el método 'es_ejecutable' de la clase 'Diagrama' (cuando el programa es ejecutable)
def test_es_ejecutable():
    diagrama = Diagrama()
    result = diagrama.insertar_ejecutable("MiPrograma", "LOCAL")
    # Comprobamos si se definió un programa ejecutable correctamente
    assert result == "Se definió el programa 'MiPrograma', ejecutable en 'LOCAL'"

    result = diagrama.es_ejecutable("MiPrograma")
    # Comprobamos que es posible ejecutar el programa
    assert result == "Si, es posible ejecutar el programa 'MiPrograma'"

# Caso de prueba para el método 'compila_en' de la clase 'Diagrama'
def test_compila_en():
    diagrama = Diagrama()
    assert diagrama.compila_en("LOCAL") == True
    assert diagrama.compila_en("Java") == False

# Caso de prueba que ejecuta varias operaciones y verifica múltiples escenarios
def test_varias_pruebas():
    diagrama = Diagrama()
    assert (
        diagrama.insertar_ejecutable("fibonacci", "LOCAL")
        == "Se definió el programa 'fibonacci', ejecutable en 'LOCAL'"
    )
    assert (
        diagrama.es_ejecutable("fibonacci")
        == "Si, es posible ejecutar el programa 'fibonacci'"
    )
    assert (
        diagrama.insertar_ejecutable("factorial", "Java")
        == "Se definió el programa 'factorial', ejecutable en 'Java'"
    )
    assert (
        diagrama.es_ejecutable("factorial")
        == "No es posible ejecutar el programa 'factorial'"
    )
    assert (
        diagrama.interprete("C", "Java")
        == "Se definió un intérprete para 'Java', escrito en 'C'"
    )
    assert (
        diagrama.traductor("C", "Java", "C")
        == "Se definió un traductor de 'Java' hacia 'C', escrito en 'C'"
    )
    assert (
        diagrama.es_ejecutable("factorial")
        == "No es posible ejecutar el programa 'factorial'"
    )
    assert (
        diagrama.interprete("LOCAL", "C")
        == "Se definió un intérprete para 'C', escrito en 'LOCAL'"
    )
    assert (
        diagrama.es_ejecutable("factorial")
        == "Si, es posible ejecutar el programa 'factorial'"
    )
    assert (
        diagrama.insertar_ejecutable("holamundo", "Python3")
        == "Se definió el programa 'holamundo', ejecutable en 'Python3'"
    )
    assert (
        diagrama.traductor("wtf42", "Python3", "LOCAL")
        == "Se definió un traductor de 'Python3' hacia 'LOCAL', escrito en 'wtf42'"
    )
    assert (
        diagrama.es_ejecutable("holamundo")
        == "No es posible ejecutar el programa 'holamundo'"
    )
    assert (
        diagrama.traductor("C", "wtf42", "Java")
        == "Se definió un traductor de 'wtf42' hacia 'Java', escrito en 'C'"
    )
    assert (
        diagrama.es_ejecutable("holamundo")
        == "Si, es posible ejecutar el programa 'holamundo'"
    )

# Ejecuta las pruebas utilizando pytest
if __name__ == "__main__":
    pytest.main()
