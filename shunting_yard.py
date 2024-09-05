# Algoritmo Shunting Yard para convertir una expresión regular de infix a postfix
def infix_a_postfix(expresion_regular):
    # Definir la precedencia de los operadores
    precedencia = {'*': 3, '.': 2, '|': 1}
    operadores = set(['*', '|', '(', ')', '.'])  # Los operadores posibles
    postfix = []  # Lista para la expresión en postfix
    pila = []  # Pila para los operadores

    # Recorremos cada símbolo de la expresión regular
    for char in expresion_regular:
        # Si el carácter es un símbolo (no un operador), lo añadimos a la salida
        if char not in operadores:
            postfix.append(char)
        # Si es un paréntesis abierto, lo empujamos a la pila
        elif char == '(':
            pila.append(char)
        # Si es un paréntesis cerrado, sacamos operadores hasta el paréntesis abierto
        elif char == ')':
            while pila and pila[-1] != '(':
                postfix.append(pila.pop())
            pila.pop()  # Quitamos el '(' de la pila
        # Si es un operador, procesamos según su precedencia
        else:
            while pila and pila[-1] != '(' and precedencia[char] <= precedencia.get(pila[-1], 0):
                postfix.append(pila.pop())
            pila.append(char)

    # Añadimos todos los operadores que quedan en la pila
    while pila:
        postfix.append(pila.pop())

    return ''.join(postfix)

# Prueba simple para verificar que el algoritmo funciona
if __name__ == "__main__":
    expresion = "(b|b)*abb(a|b)*"
    print("Infix: ", expresion)
    print("Postfix: ", infix_a_postfix(expresion))
