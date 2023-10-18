""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""
from Nodo import Nodo
from Grafo import Grafo

class Diagrama:
    def __init__(self) -> None:
        # Lenguajes que ejecuta la máquina
        self.lenguajes_conocidos = {"LOCAL": True}

        # Para los traductores, aquí se almacenan aquellos que no entiende la máquina
        self.dependencias = {}
        # Programas a ejecutar
        self.ejecutables = {}
        # Grafo donde se almacenan las relaciones entre intérpretes
        self.grafo = Grafo()

    def interprete(self, escrito_en, lenguaje):
        """
        Agrega un intérprete al grafo de lenguajes y resuelve dependencias si es necesario.

        Args:
            escrito_en (str): El lenguaje en el que está escrito el intérprete.
            lenguaje (str): El lenguaje que se interpreta.

        Returns:
            str: Un mensaje indicando si se definió un intérprete exitosamente.
        """
        nodo = Nodo(escrito_en, lenguaje)

        self.grafo.insertar(nodo)

        # Se verifica si la máquina compila en el lenguaje de entrada:
        if self.compila_en(nodo.inicio()):
            self.grafo.eliminar(nodo)

            # Se verifica si compila en el lenguaje objetivo,
            # sino este se agrega y se recorre el grafo
            if not self.compila_en(nodo.fin()):
                self.agregar_lenguaje(nodo.fin())
                lenguajes_aprendidos = self.recorrer_grafo(nodo)

                # Se resuelven dependencias (Para los traductores)
                if len(self.dependencias) > 0:
                    self.resolver_dependencias(lenguajes_aprendidos)
        return f"Se definió un intérprete para '{lenguaje}', escrito en '{escrito_en}'"

    def traductor(self, escrito_en, lenguajeA, lenguajeB):
        """
        Define un traductor de un lenguaje A a un lenguaje B, escrito en el lenguaje especificado.

        Args:
            escrito_en (str): El lenguaje en el que está escrito el traductor.
            lenguajeA (str): El lenguaje de origen.
            lenguajeB (str): El lenguaje de destino.

        Returns:
            str: Un mensaje indicando si se definió un traductor exitosamente.
        """
        if self.lenguajes_conocidos.get(escrito_en):
            # Como la máquina entiende el lenguaje escrito_en,
            # entonces se entiende como un Intérprete desde A hasta B
            self.interprete(lenguajeB, lenguajeA)
        else:
            # Entonces, el lenguaje en el que fue escrito no es conocido
            self.dependencias[escrito_en] = Nodo(lenguajeB, lenguajeA)
        return f"Se definió un traductor de '{lenguajeA}' hacia '{lenguajeB}', escrito en '{escrito_en}'"

    def insertar_ejecutable(self, nombre, lenguaje):
        """
        Agrega un programa ejecutable al diccionario de ejecutables.

        Args:
            nombre (str): El nombre del programa.
            lenguaje (str): El lenguaje en el que se ejecuta.

        Returns:
            str: Un mensaje indicando si se definió un programa ejecutable exitosamente.
        """
        if self.ejecutables.get(nombre) is not None:
            return f"Error. Ya existe un programa con el nombre '{nombre}'"
        self.ejecutables[nombre] = lenguaje
        return f"Se definió el programa '{nombre}', ejecutable en '{lenguaje}'"

    def es_ejecutable(self, nombre):
        """
        Verifica si un programa con el nombre especificado es ejecutable y si la máquina puede compilarlo.

        Args:
            nombre (str): El nombre del programa.

        Returns:
            str: Un mensaje indicando si el programa es o no ejecutable.
        """
        lenguaje = self.ejecutables.get(nombre)

        if lenguaje != None and self.compila_en(lenguaje):
            return f"Si, es posible ejecutar el programa '{nombre}'"

        return f"No es posible ejecutar el programa '{nombre}'"

    # Inspirado en BFS
    def recorrer_grafo(self, nodo):
        """
        Realiza un recorrido del grafo para aprender lenguajes adicionales a partir de un nodo específico.

        Args:
            nodo (Nodo): El nodo inicial del recorrido.

        Returns:
            list: Una lista de lenguajes aprendidos durante el recorrido.
        """
        vertice = nodo.fin()
        cola = [nodo.fin()]
        lenguajes_aprendidos = [vertice]

        while len(cola) != 0:
            vertice = cola.pop(0)
            while len(self.grafo.adyacentes(vertice)) > 0:
                lenguaje = self.grafo.adyacentes(vertice).pop(0)
                self.agregar_lenguaje(lenguaje.fin())
                lenguajes_aprendidos.append(lenguaje.fin())
                cola.append(lenguaje.fin())

        return lenguajes_aprendidos

    def compila_en(self, lenguaje) -> bool:
        """
        Comprueba si la máquina puede compilar un lenguaje específico.

        Args:
            lenguaje (str): El lenguaje a compilar.

        Returns:
            bool: True si la máquina conoce el lenguaje, False en caso contrario.
        """
        return self.lenguajes_conocidos.get(lenguaje) is not None

    def agregar_lenguaje(self, lenguaje):
        """
        Agrega un lenguaje a la lista de lenguajes conocidos por la máquina.

        Args:
            lenguaje (str): El lenguaje a agregar.
        """
        self.lenguajes_conocidos[lenguaje] = True

    def resolver_dependencias(self, lenguajes):
        """
        Resuelve las dependencias de traducción para los lenguajes especificados en la lista.

        Args:
            lenguajes (list): Lista de lenguajes para los cuales resolver dependencias.
        """
        for lenguaje in lenguajes:
            dependencia = self.dependencias.get(lenguaje)
            if dependencia is not None:
                self.interprete(dependencia.inicio(), dependencia.fin())
