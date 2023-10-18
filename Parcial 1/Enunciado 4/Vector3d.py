""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""
import math


class Vector3d:
    def __init__(self, x, y, z):
        """
        Constructor de la clase Vector3d que inicializa un vector en 3D.

        Args:
            x (float): Componente en el eje x.
            y (float): Componente en el eje y.
            z (float): Componente en el eje z.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        """
        Representación del vector como una cadena.

        Returns:
            str: Una cadena que representa el vector en el formato (x, y, z).
        """
        return str((self.x, self.y, self.z))

    def __eq__(self, otroVector) -> bool:
        """
        Sobrecarga del operador de igualdad para comparar dos objetos del tipo Vector3d.

        Args:
            otroVector (Vector3d): El otro vector que se compara.

        Returns:
            bool: True si los dos vectores son iguales, False en caso contrario.
        """
        if not isinstance(otroVector, Vector3d):
            raise TypeError(
                f"Unsupported operand type(s) for ==: 'Vector3D' and '{type(otroVector)}'"
            )

        return (
            math.isclose(self.x, otroVector.x)
            and math.isclose(self.y, otroVector.y)
            and math.isclose(self.z, otroVector.z)
        )

    def __add__(self, otroObjeto):
        """
        Sobrecarga del operador de suma (+) para objetos de tipo Vector3d.

        Args:
            otroObjeto (Vector3d, int, float): El otro objeto con el que se realiza la suma.

        Returns:
            Vector3d: Un nuevo objeto Vector3d que representa la suma.
        """
        if isinstance(otroObjeto, Vector3d):
            return Vector3d(
                self.x + otroObjeto.x, self.y + otroObjeto.y, self.z + otroObjeto.z
            )
        elif isinstance(otroObjeto, (int, float)):
            return Vector3d(
                self.x + otroObjeto, self.y + otroObjeto, self.z + otroObjeto
            )
        else:
            raise TypeError(
                f"Unsupported operand type(s) for +: 'Vector3D' and '{(type(otroObjeto))}'"
            )

    def __sub__(self, otroObjeto):
        """
        Sobrecarga del operador de resta (-) para objetos de tipo Vector3d.

        Args:
            otroObjeto (Vector3d, int, float): El otro objeto con el que se realiza la resta.

        Returns:
            Vector3d: Un nuevo objeto Vector3d que representa la resta.
        """
        if isinstance(otroObjeto, Vector3d):
            return Vector3d(
                self.x - otroObjeto.x, self.y - otroObjeto.y, self.z - otroObjeto.z
            )
        elif isinstance(otroObjeto, (int, float)):
            return Vector3d(
                self.x - otroObjeto, self.y - otroObjeto, self.z - otroObjeto
            )
        else:
            raise TypeError(
                f"Unsupported operand type(s) for -: 'Vector3D' and '{(type(otroObjeto))}'"
            )

    def __mul__(self, otroObjeto):
        """
        Sobrecarga del operador de multiplicación (*) para objetos de tipo Vector3d.
        Representa producto cruz o multiplicacion por un escalar

        Args:
            otroObjeto (Vector3d, int, float): El otro objeto con el que se realiza la multiplicación.

        Returns:
            Vector3d: Un nuevo objeto Vector3d que representa el resultado de la multiplicación.
        """
        if isinstance(otroObjeto, Vector3d):
            a = self.y * otroObjeto.z - self.z * otroObjeto.y
            b = -(self.x * otroObjeto.z - self.z * otroObjeto.x)
            c = self.x * otroObjeto.y - self.y * otroObjeto.x
            return Vector3d(a, b, c)
        elif isinstance(otroObjeto, (int, float)):
            return Vector3d(
                self.x * otroObjeto, self.y * otroObjeto, self.z * otroObjeto
            )
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Vector3D' and '{(type(otroObjeto))}'"
            )

    def __mod__(self, otroVector):
        """
        Sobrecarga del operador módulo (%) para objetos de tipo Vector3d. Representa producto punto

        Args:
            otroVector (Vector3d): El otro vector con el que se realiza la operación módulo.

        Returns:
            float: Un valor que representa el resultado de la operación módulo.
        """
        if not isinstance(otroVector, Vector3d):
            raise TypeError(
                f"Unsupported operand type(s) for %: 'Vector3D' and '{(type(otroVector))}'"
            )

        return self.x * otroVector.x + self.y * otroVector.y + self.z * otroVector.z

    def __invert__(self):
        """
        Sobrecarga del operador unario ~ para objetos de tipo Vector3d.

        Returns:
            float: La magnitud (módulo) del vector.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
