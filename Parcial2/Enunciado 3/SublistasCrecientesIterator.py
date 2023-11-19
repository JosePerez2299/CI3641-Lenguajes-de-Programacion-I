class SublistasCrecientesIterator:
    def __init__(self, lista):
        """
        Inicializa el iterador con la lista dada.

        Parameters:
        - lista (list): La lista de la cual se generarán las sublistas crecientes.
        """
        self.lista = lista
        self.tamano = len(lista)

    def __iter__(self):
        """
        Retorna un iterador que genera todas las sublistas crecientes de la lista.

        Yields:
        - list: Sublistas crecientes de la lista.
        """
        yield []  # La lista vacía es el primer elemento en las sublistas crecientes
        for index, item in enumerate(self.lista):
            yield from self.buscarSecuencia(index, [item])

    def buscarSecuencia(self, index, acumulador):
        """
        Genera de manera recursiva todas las sublistas crecientes a partir de una posición dada.

        Parameters:
        - index (int): Índice actual en la lista.
        - acumulador (list): Sublista creciente acumulada hasta el momento.

        Yields:
        - list: Sublistas crecientes a partir de la posición actual.
        """
        yield acumulador

        contador = index + 1
        while contador < self.tamano:
            item = self.lista[contador]
            if item > acumulador[-1]:
                yield from self.buscarSecuencia(contador, acumulador + [item])
            contador += 1

# Ejemplo de uso
lista = [1, 4, 3, 2, 5]

for sublista in SublistasCrecientesIterator(lista):
    print(sublista)
