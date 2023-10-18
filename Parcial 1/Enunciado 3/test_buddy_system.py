import pytest
from BuddySystem import BuddySystem


def test_allocate():
    buddy = BuddySystem(64)
    assert buddy.allocate("Block1", 8) == "Se ha asignado memoria exitosamente para 'Block1' en el bloque '(0, 7)'"
    assert buddy.allocate("Block2", 4) == "Se ha asignado memoria exitosamente para 'Block2' en el bloque '(8, 11)'"
    assert buddy.allocate("Block3", 35) == "El tamaño solicitado excede la capacidad de la memoria"
    assert buddy.allocate("Block1", 4) == "Ya existe una asignación para este nombre: Block1"


def test_deallocate():
    buddy = BuddySystem(64)
    buddy.allocate("Block1", 8)
    buddy.allocate("Block2", 4)

    assert buddy.deallocate("Block3") == "No se encontró un bloque con el nombre: Block3"
    assert buddy.deallocate("Block1") == "Se ha liberado el bloque de memoria 'Block1' : '(0, 7)'"
    assert buddy.deallocate("Block2") == "Se ha liberado el bloque de memoria 'Block2' : '(8, 11)'"

def test_printm(capsys):
    buddy = BuddySystem(64)
    buddy.allocate("Block1", 8)
    buddy.allocate("Block2", 4)

    buddy.printm()

    captured = capsys.readouterr()
    assert "Bloques libres:" in captured.out
    assert "Bloques ocupados:" in captured.out


if __name__ == "__main__":
    pytest.main()
