""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""
from Diagrama import Diagrama


class ProgramaCliente:
    def __init__(self):
        self.diagrama = Diagrama()

    def ejecutar_comando(self, comando):
        comando = comando.split()
        tamano = len(comando)
        if tamano == 0:
            return "Por favor escriba un comando"
        if comando[0] == "DEFINIR":
            if tamano == 4:
                if comando[1] == "PROGRAMA":
                    nombre = comando[2]
                    lenguaje = comando[3]
                    return self.diagrama.insertar_ejecutable(nombre, lenguaje)
                elif comando[1] == "INTERPRETE":
                    lenguaje_base = comando[2]
                    lenguaje = comando[3]
                    return self.diagrama.interprete(lenguaje_base, lenguaje)
            elif tamano == 5:
                if comando[1] == "TRADUCTOR":
                    lenguaje_base = comando[2]
                    lenguaje_origen = comando[3]
                    lenguaje_destino = comando[4]
                    return self.diagrama.traductor(
                        lenguaje_base, lenguaje_origen, lenguaje_destino
                    )
        elif comando[0] == "EJECUTABLE":
            if tamano == 2:
                nombre = comando[1]
                return self.diagrama.es_ejecutable(nombre)
        return "Comando no reconocido."

    def run(self):
        print(
            "Acciones disponibles:\n1. DEFINIR <tipo> [<argumentos>]\n2. EJECUTABLE <nombre>\n3. SALIR"
        )
        while True:
            comando = input("$> ")
            if comando == "SALIR":
                break
            resultado = self.ejecutar_comando(comando)
            print(resultado)


if __name__ == "__main__":
    cliente = ProgramaCliente()
    cliente.run()
