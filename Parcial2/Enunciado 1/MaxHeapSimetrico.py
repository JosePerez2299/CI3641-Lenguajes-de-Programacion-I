class Arbol:
    def __init__(self, valor, hijoIzq=None, hijoDer=None) -> None:
        """
        Inicializa un objeto Arbol con un valor y dos hijos opcionales.
        """
        self.valor = valor
        self.hijoIzq = hijoIzq
        self.hijoDer = hijoDer

    def obtenerValor(self):
        """
        Devuelve el valor del nodo actual.
        """
        return self.valor

    def obtenerHijoIzq(self):
        """
        Devuelve el hijo izquierdo del nodo actual.
        """
        return self.hijoIzq

    def obtenerHijoDer(self):
        """
        Devuelve el hijo derecho del nodo actual.
        """
        return self.hijoDer

    def preOrder(self):
        """
        Devuelve una lista que representa el recorrido preorden del árbol.
        """
        return self.preOrderSubTree(self)

    def postOrder(self):
        """
        Devuelve una lista que representa el recorrido postorden del árbol.
        """
        return self.postOrderSubTree(self)

    def preOrderSubTree(self, node):
        """
        Devuelve una lista que representa el recorrido preorden del subárbol con raíz en el nodo dado.
        """
        result = [node.valor]

        if node.obtenerHijoIzq() is not None:
            result += self.preOrderSubTree(node.obtenerHijoIzq())

        if node.obtenerHijoDer() is not None:
            result += self.preOrderSubTree(node.obtenerHijoDer())

        return result

    def postOrderSubTree(self, node):
        """
        Devuelve una lista que representa el recorrido postorden del subárbol con raíz en el nodo dado.
        """
        result = []

        if node.obtenerHijoIzq() is not None:
            result += self.postOrderSubTree(node.obtenerHijoIzq())

        if node.obtenerHijoDer() is not None:
            result += self.postOrderSubTree(node.obtenerHijoDer())

        return result + [node.obtenerValor()]


    def esMaxHeap(self):
        """
        Devuelve True si el árbol es un max-heap, False en caso contrario.
        """
        queue = [self]
        while len(queue) != 0:
            elem = queue.pop()
            hijoIzq = elem.obtenerHijoIzq()
            hijoDer = elem.obtenerHijoDer()
            if hijoIzq is not None:
                if hijoIzq.obtenerValor() > elem.obtenerValor():
                    return False
                queue.append(hijoIzq)

            if hijoDer is not None:
                if hijoDer.obtenerValor() > elem.obtenerValor():
                    return False
                queue.append(hijoDer)

        return True

    def esMaxHeapSimetrico(self) -> bool:
        """
        Devuelve True si el árbol es un max-heap simétrico, False en caso contrario.
        """
        return self.esMaxHeap() and self.preOrder() == self.postOrder()
    
if __name__ == "__main__":
    a = Arbol(1,
            Arbol(1,
                Arbol(1),
                Arbol(1)
            ),
            Arbol(1,
                Arbol(1),
                Arbol(1)
            )
        )

    print("Max Heap: ", a.esMaxHeap())
    print("Preorder: ", a.preOrder())
    print("Postorder: ", a.postOrder())
    print("Max Heap Simetrico: ", a.esMaxHeapSimetrico())
