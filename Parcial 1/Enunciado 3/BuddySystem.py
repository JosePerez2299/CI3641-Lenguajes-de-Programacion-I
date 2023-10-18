""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""
import math
from Block import Block


class BuddySystem:
    def __init__(self, memory_size: int):
        """Inicializa el sistema de asignación de bloques de memoria.

        Args:
            memory_size (int): El tamaño total de la memoria en bytes.
        """
        # Diccionario para almacenar los bloques ocupados
        self.block_dict = {}

        # Cantidad de bloques en la memoria (log2 del tamaño de la memoria)
        self.num_blocks = math.floor(math.log2(memory_size))

        # Lista de listas vacías para bloques libres de diferentes tamaños
        self.free_blocks = [[] for _ in range(self.num_blocks + 1)]

        # Agregar el bloque inicial a la lista de bloques libres más grandes
        self.free_blocks[self.num_blocks] = [Block(0, 2**self.num_blocks - 1)]

    def allocate(self, block_name: str, size: int) -> str:
        """Asigna un bloque de memoria del tamaño especificado.

        Args:
            block_name (str): El nombre del bloque a asignar.
            size (int): El tamaño requerido en bytes.

        Returns:
            str: Un mensaje que indica si la asignación se realizó con éxito o si hubo un error.
        """
        # Verificar si ya existe una asignacion para ese nombre
        if self.block_dict.get(block_name):
            return f"Ya existe una asignación para este nombre: {block_name}"

        # Determinar el tamaño requerido en términos de bloques
        block_position = math.ceil(math.log2(size))

        # Verificar si el tamano excede a la capacidad de memoria
        if block_position > self.num_blocks:
            return "El tamaño solicitado excede la capacidad de la memoria"

        # En caso de que la memoria se cuente con espacio, se realiza la asignacion
        if len(self.free_blocks[block_position]) > 0:
            block = self.free_blocks[block_position].pop(0)
            self.block_dict[block_name] = block
            return f"Se ha asignado memoria exitosamente para '{block_name}' en el bloque '{str(block)}'"

        # Se procede a comprobar la existencia de bloques de mayor tamano
        index = block_position + 1
        while index <= self.num_blocks:
            if len(self.free_blocks[index]) > 0:
                break
            index += 1

        # En este caso, no se consigue un bloque disponible y termina la ejecucion
        if index == self.num_blocks + 1:
            return "El tamaño solicitado excede la capacidad de la memoria"

        # Se elimina el bloque de la lista, y se procede a particionar
        block = self.free_blocks[index].pop(0)
        while index > block_position:
            division = block.start + (block.end - block.start) // 2
            partition0 = Block(block.start, division)
            partition1 = Block(division + 1, block.end)
            self.free_blocks[index - 1].append(partition1)
            block = partition0
            index -= 1

        # Finalmente, se le asigna el bloque encontrado y se retorna
        self.block_dict[block_name] = block
        return f"Se ha asignado memoria exitosamente para '{block_name}' en el bloque '{str(block)}'"

    def deallocate(self, block_name: str) -> str:
        """Libera un bloque de memoria previamente asignado.

        Args:
            block_name (str): El nombre del bloque a liberar.

        Returns:
            str: Un mensaje que indica si se ha liberado correctamente o si no se encontró el bloque.
        """
        # Se comprueba la existencia de un bloque con ese nombre
        block_to_deallocate = self.block_dict.get(block_name)

        if not block_to_deallocate:
            return f"No se encontró un bloque con el nombre: {block_name}"

        # Se calcula la posicion del bloque, y se anade ese bloque a la lista de bloques disponibles
        block_position = math.ceil(math.log2(block_to_deallocate.size))
        self.free_blocks[block_position].append(block_to_deallocate)

        # Se procede a fusionar recursivamente los bloques
        self.merge_blocks(block_to_deallocate)

        # Se Elimina la asignacion y termina
        self.block_dict.pop(block_name)
        return f"Se ha liberado el bloque de memoria '{block_name}' : '{block_to_deallocate}'"

    def merge_blocks(self, block_to_merge):
        """Función recursiva para unir bloques siempre que sea posible.

        Args:
            block_to_merge (Block): El bloque que se intenta fusionar con su bloque compañero.
        """

        # Termina la recursion cuando el block es null
        if block_to_merge == None:
            return

        # Posicion y buddyNumber
        block_position = math.ceil(math.log2(block_to_merge.size))
        buddy_number = block_to_merge.start / block_to_merge.size

        if buddy_number % 2 != 0:
            buddy_start = block_to_merge.start - block_to_merge.size
        else:
            buddy_start = block_to_merge.start + block_to_merge.size

        # Se procede a hacer merge de los bloques con igual tamano y contiguos
        merged_block = None
        for index, block in enumerate(self.free_blocks[block_position]):
            if block.start == buddy_start:
                if buddy_number % 2 == 0:
                    merged_block = Block(block_to_merge.start, block.end)
                    self.free_blocks[block_position + 1].append(merged_block)
                else:
                    merged_block = Block(block.start, block_to_merge.end)
                    self.free_blocks[block_position + 1].append(merged_block)

                self.free_blocks[block_position].pop()
                self.free_blocks[block_position].pop(index)
                break

        # Se verifican los proximos bloques mas grandes
        self.merge_blocks(merged_block)

    def printm(self):
        """Muestra una representación en texto de los bloques libres y ocupados en el sistema de asignación de bloques de memoria.

        Esta función imprime una descripción visual de los bloques libres y los bloques ocupados en la memoria, junto con sus respectivos tamaños y nombres asociados.

        Args:
            No recibe argumentos, ya que utiliza datos almacenados en el objeto BuddySystem actual.

        Returns:
            None
        """
        
        print()
        print("Bloques libres:")
        for i, blocks in enumerate(self.free_blocks):
            if blocks:
                print(f"Tamaño {2**i} bytes: {', '.join([str(block) for block in blocks])}")

        print("Bloques ocupados:")
        for nombre, block in self.block_dict.items():
            print(f"{nombre}: {block}")

