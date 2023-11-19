import re

class ExpresionesAritmeticas:
    def __init__(self):
        pass

    def evaluar_expresion(self, orden, expresion):
        """
        Evalúa una expresión aritmética en notación prefija o postfija.

        Parameters:
        - orden (str): El orden de la notación ("PRE" para prefijo o "POST" para postfijo).
        - expresion (str): La expresión aritmética.

        Returns:
        - int: El resultado de la evaluación de la expresión.
        """
        if orden == "PRE":
            return self.evaluar_prefijo(expresion)
        elif orden == "POST":
            return self.evaluar_postfijo(expresion)
        else:
            return "Orden no válido."

    def mostrar_expresion(self, orden, expresion):
        """
        Muestra la expresión aritmética en notación infija.

        Parameters:
        - orden (str): El orden de la notación ("PRE" para prefijo o "POST" para postfijo).
        - expresion (str): La expresión aritmética.

        Returns:
        - str: La expresión en notación infija.
        """
        if orden == "PRE":
            return self.mostrar_infijo(self.convertir_prefijo_infijo(expresion))
        elif orden == "POST":
            return self.mostrar_infijo(self.convertir_postfijo_infijo(expresion))
        else:
            return "Orden no válido."

    def evaluar_prefijo(self, expresion):
        """
        Evalúa una expresión en notación prefija.

        Parameters:
        - expresion (str): La expresión en notación prefija.

        Returns:
        - int: El resultado de la evaluación de la expresión.
        """
        pila = []
        operadores = {"+", "-", "*", "/"}

        for token in reversed(expresion.split()):
            if token.isdigit():
                pila.append(int(token))
            elif token in operadores:
                operando1 = pila.pop()
                operando2 = pila.pop()
                if token == "+":
                    pila.append(operando1 + operando2)
                elif token == "-":
                    pila.append(operando1 - operando2)
                elif token == "*":
                    pila.append(operando1 * operando2)
                elif token == "/":
                    pila.append(operando1 // operando2)

        return pila[0]

    def evaluar_postfijo(self, expresion):
        """
        Evalúa una expresión en notación postfija.

        Parameters:
        - expresion (str): La expresión en notación postfija.

        Returns:
        - int: El resultado de la evaluación de la expresión.
        """
        pila = []
        operadores = {"+", "-", "*", "/"}

        for token in expresion.split():
            if token.isdigit():
                pila.append(int(token))
            elif token in operadores:
                operando2 = pila.pop()
                operando1 = pila.pop()
                if token == "+":
                    pila.append(operando1 + operando2)
                elif token == "-":
                    pila.append(operando1 - operando2)
                elif token == "*":
                    pila.append(operando1 * operando2)
                elif token == "/":
                    pila.append(operando1 // operando2)

        return pila[0]

    def convertir_prefijo_infijo(self, expresion):
        """
        Convierte una expresión en notación prefija a notación infija.

        Parameters:
        - expresion (str): La expresión en notación prefija.

        Returns:
        - str: La expresión en notación infija.
        """
        pila = []
        for token in reversed(expresion.split()):
            if token.isdigit():
                pila.append([token])
            else:
                operand1 = pila.pop()
                operand2 = pila.pop()

                # Si el operand1 es una expresion, entonces convertirlo a string
                if len(operand1) > 1:

                    # Aplanar
                    if (token == "*" and operand1[1] in "+-/") or (
                        token == "/" and operand1[1] in "+-*"
                    ):
                        # Colocar parentesis
                        operand1 = [f"({operand1[0]} {operand1[1]} {operand1[2]})"]
                    else:
                        # No requiere parentesis
                        operand1 = [f"{operand1[0]} {operand1[1]} {operand1[2]}"]

                # Si el operand2 es una expresion, entonces convertirlo a string
                if len(operand2) > 1:
                    if (token == "*" and operand2[1] in "+-/") or (
                        token == "/" and operand2[1] in "+-*"
                    ):
                        operand2 = [f"({operand2[0]} {operand2[1]} {operand2[2]})"]
                    else:
                        operand2 = [f"{operand2[0]} {operand2[1]} {operand2[2]}"]

                nueva_expresion = [operand1[0], token, operand2[0]]
                pila.append(nueva_expresion)

        return f"{' '.join(pila[0])}"

    def convertir_postfijo_infijo(self, expresion):
        """
        Convierte una expresión en notación postfija a notación infija.

        Parameters:
        - expresion (str): La expresión en notación postfija.

        Returns:
        - str: La expresión en notación infija.
        """
        pila = []

        for token in expresion.split():
            if token.isdigit():
                pila.append([token])
            else:
                operand2 = pila.pop()
                operand1 = pila.pop()

                if len(operand1) > 1 and isinstance(operand1, list):

                    # Aplanar
                    if (token == "*" and operand1[1] in "+-/") or (
                        token == "/" and operand1[1] in "+-*"
                    ):
                        # Colocar parentesis
                        operand1 = [f"({operand1[0]} {operand1[1]} {operand1[2]})"]
                    else:
                        # No requiere parentesis
                        operand1 = [f"{operand1[0]} {operand1[1]} {operand1[2]}"]

                # Si el operand2 es una expresion, entonces convertirlo a string
                if len(operand2) > 1 and isinstance(operand2, list):

                    if (token == "*" and operand2[1] in "+-/") or (
                        token == "/" and operand2[1] in "+-*"
                    ):
                        operand2 = [f"({operand2[0]} {operand2[1]} {operand2[2]})"]
                    else:
                        operand2 = [f"{operand2[0]} {operand2[1]} {operand2[2]}"]

                nueva_expresion = [operand1[0], token, operand2[0]]
                pila.append(nueva_expresion)

        return f"{' '.join(pila[0])}"

    def mostrar_infijo(self, expresion):
        """
        Muestra la expresión en notación infija.

        Parameters:
        - expresion (str): La expresión en notación infija.

        Returns:
        - str: La expresión en notación infija.
        """
        return expresion

def main():
    expresiones = ExpresionesAritmeticas()

    print("Bienvenido!")
    print("Opciones disponibles: ")
    print("1. EVAL <orden> <expr>")
    print("2. MOSTRAR <orden> <expr>")
    print("3. SALIR")

    while True:
        accion_input = input("Ingrese una acción: ").upper()

        if accion_input == "SALIR":
            print("Programa finalizado con éxito :D")
            break

        accion_match = re.match(
            r"^\s*(EVAL|MOSTRAR)\s+(PRE|POST)\s+([0-9+\-*/\s]+)\s*$", accion_input
        )

        if accion_match:
            comando = accion_match.group(1)
            orden = accion_match.group(2)
            expr = accion_match.group(3)
            if comando == "EVAL":
                resultado = expresiones.evaluar_expresion(orden, expr)
                print(f"Resultado: {resultado}")
            elif comando == "MOSTRAR":
                resultado = expresiones.mostrar_expresion(orden, expr)
                print(f"Resultado: {resultado}")
        else:
            print(
                "Error al analizar la entrada. Vuelva a intentarlo.\nUso: EVAL|MOSTRAR PRE|POST <expr>"
            )
            continue

        continuar = input("¿Desea realizar otra acción? (Sí/No): ").upper()
        if continuar != "SI":
            break

if __name__ == "__main__":
    expresiones = ExpresionesAritmeticas()
    main()
