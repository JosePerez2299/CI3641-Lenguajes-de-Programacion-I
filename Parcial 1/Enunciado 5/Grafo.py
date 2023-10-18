from Nodo import Nodo

class Grafo:
    def __init__(self) -> None:
        """
        Constructor de la clase Grafo. Inicializa un grafo vacío representado como un diccionario.
        La clave es el vértice y el valor es una lista de lados conectados a ese vértice.
        """
        self.grafo = {}

    def insertar(self, lado: Nodo):
        """
        Inserta un lado en el grafo.

        Args:
            lado (Nodo): El lado que se va a insertar en el grafo.

        Si el vértice de inicio del lado no existe en el grafo, se agrega con el lado.
        Si el vértice de inicio ya existe en el grafo, se verifica si el lado ya está en la lista de lados
        conectados a ese vértice. Si no está, se agrega a la lista.

        Si el vértice de fin del lado no existe en el grafo, se crea un vértice con una lista vacía de lados.

        No devuelve nada.
        """
        vertice_inicio = self.grafo.get(lado.inicio())

        if vertice_inicio is None:
            self.grafo[lado.inicio()] = [lado]
        else:
            if lado not in vertice_inicio:
                vertice_inicio.append(lado)

        if not self.grafo.get(lado.fin()):
            self.grafo[lado.fin()] = []

    def eliminar(self, lado: Nodo):
        """
        Elimina un lado del grafo.

        Args:
            lado (Nodo): El lado que se va a eliminar del grafo.

        Busca el vértice de inicio del lado en el grafo. Si no existe, no hace nada.
        Si existe, elimina el lado de la lista de lados conectados a ese vértice.

        No devuelve nada.
        """
        vertice = self.grafo.get(lado.inicio())
        if vertice is None:
            return False
        
        self.grafo[lado.inicio()] = [x for x in vertice if x != lado]

    def adyacentes(self, inicio: str):
        """
        Obtiene los lados adyacentes a un vértice dado.

        Args:
            inicio (str): El vértice del cual se desean obtener los lados adyacentes.

        Returns:
            list: Una lista de lados adyacentes al vértice especificado.
        """
        return self.grafo[inicio]

    def __repr__(self) -> str:
        """
        Representación en cadena de la clase Grafo. Llama a __str__ para obtener la representación de cadena.
        """
        return self.__str__()

    def __str__(self) -> str:
        """
        Representación en cadena del grafo.

        Returns:
            str: Una representación en cadena del grafo en un formato legible.
        """
        string = "\n\n"
        for lados in self.grafo.items():
            string += f"{lados[0]}\t\t---> {lados[1]}\n"
        return string
