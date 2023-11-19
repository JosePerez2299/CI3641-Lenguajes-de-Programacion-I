"""
Carnet 16-10882
X = 8
Y = 8
Z = 2

alfa = ((8 + 8) mod 5)+ 3 = 4
beta = ((8 + 2) mod 5)+ 3 = 3
"""
import functools

alfa = 4
beta = 3

@functools.cache
def f_recursiva(n: int) -> int:
    """Versión recursiva de la función F.

    Parameters:
    - n (int): Valor de entrada para la función.

    Returns:
    - int: Resultado de la función F para el valor de entrada n.
    """
    if 0 <= n < alfa * beta:
        return n

    # Caso recursivo: se utiliza la recursividad para calcular el resultado de F
    return sum(f_recursiva(n - beta * i) for i in range(1, alfa + 1))

def f_recursiva_cola(n: int) -> int:
    """Versión recursiva de cola de la función F.

    Parameters:
    - n (int): Valor de entrada para la función.

    Returns:
    - int: Resultado de la función F para el valor de entrada n.
    """

    def f_aux(acc: list, i: int) -> int:
        """Función auxiliar recursiva para calcular los valores de F.

        Parameters:
        - acc (list): Lista que almacena los valores de F ya calculados.
        - i (int): Contador para seguir calculando valores.

        Returns:
        - int: Resultado de la función F para el valor de entrada n.
        """

        # Caso base de la recursión
        if 0 <= n < alfa * beta:
            return n

        elif n == i:
            return sumatoria(acc)

        # Caso recursivo: se actualiza la lista acc y se llama recursivamente a f_aux
        acc = acc[1:] + [sumatoria(acc)]
        return f_aux(acc, i + 1)

    casos_bases = [x for x in range(0, alfa * beta)]
    return f_aux(casos_bases, alfa * beta)


def f_iterativa(n: int) -> int:
    """Versión iterativa de la función F.

    Parameters:
    - n (int): Valor de entrada para la función.

    Returns:
    - int: Resultado de la función F para el valor de entrada n.
    """
    
    # Caso base cuando 0 <= n < alfa * beta
    if 0 <= n < alfa * beta:
        return n

    # Inicialización de variables para el caso iterativo
    acc = [x for x in range(0, alfa * beta)]
    i = alfa * beta

    # Componente del caso recursivo: se actualiza la lista acc hasta que n sea igual a i
    while n != i:
        acc = acc[1:] + [sumatoria(acc)]
        i += 1
    return sumatoria(acc)


def sumatoria(lista: list) -> int:
    """Función usada para calcular la suma de la lista.

    Parameters:
    - lista (list): Lista de valores a sumar.

    Returns:
    - int: Suma de los valores en la lista.
    """
    sublista = [lista[alfa * beta - i * beta] for i in range(1, alfa + 1)]
    return sum(sublista)
