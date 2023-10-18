""" 
 Universidad Simon Bolivar
 Autor: Jose Perez, Carnet 16-10882
"""

from BuddySystem import BuddySystem


def main():
    memory_size = int(input("Tamaño de la memoria en bytes: "))
    buddy_system = BuddySystem(memory_size)

    while True:
        print("Acciones disponibles:")
        print("1. RESERVAR <cantidad> <nombre>")
        print("2. LIBERAR <nombre>")
        print("3. MOSTRAR")
        print("4. SALIR")

        action = input("Seleccione una acción: ").strip().split()

        if len(action) == 0:
            continue

        # Convertir a mayúsculas para ser case-insensitive
        action[0] = action[0].upper()

        if action[0] == "RESERVAR":
            if len(action) != 3:
                print("Formato incorrecto. Debe ser: RESERVAR <cantidad> <nombre>")
                continue

            try:
                cantidad = int(action[1])
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue

            nombre = action[2]

            result = buddy_system.allocate(nombre, cantidad)
            print()
            print(result)
            print()

        elif action[0] == "LIBERAR":
            if len(action) != 2:
                print("Formato incorrecto. Debe ser: LIBERAR <nombre>")
                continue

            nombre = action[1]

            result = buddy_system.deallocate(nombre)
            print()
            print(result)
            print()

        elif action[0] == "MOSTRAR":
            print()
            buddy_system.printm()
            print()

        elif action[0] == "SALIR":
            break

        else:
            print("Acción no reconocida. Intente nuevamente.")


if __name__ == "__main__":
    main()
