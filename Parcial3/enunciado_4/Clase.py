class Clase:
    def __init__(self, class_nombre: str, metodos: [str], padre_class = None ):
        self.nombre = class_nombre
        self.list_metodos = {}
        self.padre_class = padre_class

        # Agregar metodos, y validar si no hay metodos repetidos
        for metodo in metodos:
            if self.list_metodos.get(metodo) is not None:
                print(f"La clase {self.nombre} ya tiene creado un metodo {metodo}")
                continue
            
            self.list_metodos[metodo] = self.nombre
            
        if padre_class is not None:
            for metodo, heredadoDe in padre_class.metodos().items():
                if self.list_metodos.get(metodo) is None:
                    self.list_metodos[metodo] = heredadoDe                
           
    def metodos(self):
        return self.list_metodos
    
    def get_nombre(self):
        return self.nombre
    
    def padre(self):
        return self.padre_class

    def __str__(self):
        
        return f"CLASS {self.nombre} {self.list_metodos}"
        
        
    def __repr__(self) -> str:
        return self.__str__()
    
    