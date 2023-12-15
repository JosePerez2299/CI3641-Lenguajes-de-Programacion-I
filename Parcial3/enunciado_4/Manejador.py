from Clase import Clase


class Manejador:
    def __init__(self) -> None:
        self.clases_definidas = {}

    def definir(self, nombre_clase, metodos, nombre_padre):
        padre = self.get_clase(nombre_padre)
        if nombre_padre is not None and padre is None:
            return f"La super clase '{nombre_padre}' no esta definida"

        if self.clases_definidas.get(nombre_clase) is not None:
            return f"La clase '{nombre_clase}' ya esta definida"

        self.insertar(Clase(nombre_clase, metodos, padre))

        return f"Se creo exitosamente la clase {nombre_clase}"

    def insertar(self, clase):
        self.clases_definidas[clase.get_nombre()] = clase

    def describir(self, clase_nombre):
        clase = self.get_clase(clase_nombre)
        if clase is None:
            return f"La clase '{clase_nombre}' no esta definida"

        resultado = ""

        for key, value in clase.metodos().items():
            resultado += f"{key} -> {value} :: {key}\n"

        return resultado.strip()

    def get_clase(self, clase_nombre):
        return self.clases_definidas.get(clase_nombre)

    def __repr__(self) -> str:
        return str((self.clases_definidas))
