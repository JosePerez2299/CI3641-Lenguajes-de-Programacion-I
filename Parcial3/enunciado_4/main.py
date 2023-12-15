import re
from Clase import Clase
from Manejador import Manejador


def main():
    manejador = Manejador()
    print("\tBienvenido!")
    print("Opciones disponibles: ")
    print("1. CLASS <tipo> [<nombre>]")
    print("2. DESCRIBIR <nombre>")
    print("3. SALIR")

    while True:
        user_input = input(
            "Ingrese una acción: ")

        # Expresión regular para identificar las acciones
        pattern = re.compile(
            r'\s*(SALIR|DESCRIBIR\s+\w+|CLASS (\w+)(?: : (\w+))?(?:\s*([a-zA-Z ]+))?)\s*$')

        match = pattern.match(user_input)

        if match:
            action = match.group(1)
            if action == 'SALIR':
                break
            elif action.startswith('DESCRIBIR'):
                nombre_clase = re.search(r'DESCRIBIR\s+(\w+)', action)
                print()
                print(manejador.describir(nombre_clase.group(1)))
                print()
            elif action.startswith('CLASS'):
                nombre_clase = match.group(2)
                nombre_padre = match.group(3)
                metodos = [] if match.group(
                    4) is None else match.group(4).split()
                print()
                print(manejador.definir(nombre_clase, metodos, nombre_padre))
                print()

        else:
            print("\nEntrada no válida. Intente de nuevo.\n")


if __name__ == "__main__":

    main()
