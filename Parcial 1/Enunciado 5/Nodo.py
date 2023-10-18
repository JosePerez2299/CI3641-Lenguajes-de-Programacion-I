class Nodo:
    def __init__(self, i, f, dependencia = None) -> None:
        self.i = i
        self.f = f
        self.dependencia = dependencia
    def inicio(self):
        return self.i

    def fin(self):
        return self.f

    def __eq__(self, otroNodo) -> str:
        return self.i == otroNodo.i and self.f == otroNodo.f

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str((self.i, self.f))
