# Algoritmo Shunting Yard para convertir una expresión regular de infix a postfix
import re
def remove_epsilon(expression):
    result = re.sub(r'ε', '', expression)
    return result
def agregar_concatenacion_implicita(expresion_regular):
    """
    Inserta el operador de concatenación (.) implícito en la expresión regular.
    Por ejemplo, convierte "ab" en "a.b" si hay una concatenación implícita.
    """
    resultado = []
    operadores = set(['*', '|', '(', ')'])

    for i in range(len(expresion_regular)):
        char = expresion_regular[i]
        resultado.append(char)

        # Verificar si necesitamos insertar un operador de concatenación
        if i + 1 < len(expresion_regular):
            next_char = expresion_regular[i + 1]

            # Insertar concatenación implícita entre:
            # - símbolo y símbolo (ab => a.b)
            # - símbolo y paréntesis abierto (a( => a.( )
            # - cierre de kleene (*) y símbolo/parentesis abierto (*a => * . a)
            if (char not in operadores or char == ')' or char == '*') and (next_char not in operadores or next_char == '('):
                resultado.append('.')
    
    return ''.join(resultado)

# Algoritmo Shunting Yard para convertir una expresión regular de infix a postfix
def infix_a_postfix(expresion_regular):
    # Definir la precedencia de los operadores regulares
    precedencia = {'|': 1, '.': 2, '*': 3}
    operadores = set(['|', '.', '*', '(', ')'])  # Los operadores posibles
    postfix = []  # Lista para la expresión en postfix
    pila = []  # Pila para los operadores

    # Recorremos cada símbolo de la expresión regular
    for char in expresion_regular:
        # Si el carácter es un operando (número o letra), lo añadimos a la salida
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



