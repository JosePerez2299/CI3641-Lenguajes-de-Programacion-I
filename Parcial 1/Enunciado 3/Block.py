""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""
class Block:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = end - start + 1

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"({self.start}, {self.end})"
