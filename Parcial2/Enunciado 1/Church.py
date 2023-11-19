class Church:
    def __init__(self, n=None):
        """
        Inicializa un objeto Church, recibe como argumento opcional un objeto instancia de Church (None por defecto).
        """
        self.number = n

    succ = lambda self: Church(self)
    """
    Devuelve una nueva instancia de Church que representa el número siguiente al número representado por la instancia actual.
    """

    def toInt(self):
        """
        Devuelve el número natural representado por la instancia actual.
        """
        integer = 0
        aux = self.number
        while aux is not None:
            integer += 1
            aux = aux.number
        return integer

    def intToChurch(n):
        """
        Toma un número natural n y devuelve una instancia de Church que representa ese número.
        """
        church = Church()
        while n > 0:
            church = church.succ()
            n -= 1
        return church

    def __add__(self, m):
        """
        Sobrecarga el operador + para que pueda ser utilizado con instancias de Church.
        Utiliza la recursión para calcular la suma de dos números representados por instancias de Church.
        """
        if m.number is None:
            return self
        else:
            return self.__add__(m.number).succ()

    def __mul__(self, m):
        """
        Sobrecarga el operador * para que pueda ser utilizado con instancias de Church.
        Utiliza la recursión para calcular el producto de dos números representados por instancias de Church.
        """
        if m.number is None:
            return m
        else:
            return self.__add__(self.__mul__(m.number))

if __name__== "__main__":
    # Ejemplo:
    diez = Church.intToChurch(10)
    dos = Church.intToChurch(2)

    # Sumamos 10 + 2. Retorna 12 en Church, y lo convertimos a entero para mostrarlo en consola
    print((diez + dos).toInt())

    # Multiplicamos 10*2. Retorna 20 en Church, y lo convertimos a entero para mostrarlo en consola
    print((diez * dos).toInt())
