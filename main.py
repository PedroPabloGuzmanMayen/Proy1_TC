# expresión regular (r): (b|b)*abb(a|b)*
# la cadena (w): babbaaaaa
#  símbolo para representar epsilon (ε): ε

# Función para leer la entrada del usuario
# Importar la función desde el archivo shunting_yard.py
# Importar las funciones desde los archivos correspondientes

from shunting_yard import infix_a_postfix

# Función para leer la entrada del usuario
def leer_entrada():
    # Solicitar la expresión regular y la cadena
    expresion_regular = input("Ingresa la expresión regular (r): ")
    cadena = input("Ingresa la cadena (w): ")
    
    # Solicitar el símbolo para representar epsilon
    epsilon = input("Ingresa el símbolo que representará a epsilon (ε): ")
    
    # Extraer el alfabeto de la expresión regular
    alfabeto = extraer_alfabeto(expresion_regular)
    
    # Mostrar la información ingresada
    print("\nInformación ingresada:")
    print("Expresión regular: " + str(expresion_regular))
    print("Cadena: " + str(cadena))
    print("Símbolo para epsilon: " + str(epsilon))
    print("Alfabeto: " + str(alfabeto))
    
    return expresion_regular, cadena, epsilon, alfabeto

# Función para extraer los símbolos del alfabeto de la expresión regular
def extraer_alfabeto(expresion_regular):
    # Definir los operadores comunes de expresiones regulares
    operadores = set('|()*+')
    
    # Extraer todos los caracteres que no sean operadores
    alfabeto = {char for char in expresion_regular if char not in operadores}
    
    return alfabeto

# Función principal para ejecutar el programa
if __name__ == "__main__":
    # Llamar a la función para leer la entrada
    expresion_regular, cadena, epsilon, alfabeto = leer_entrada()
    
    # Convertir la expresión regular a postfix
    expresion_postfix = infix_a_postfix(expresion_regular)
    
    # Mostrar la expresión en notación postfix
    print(f"\nExpresión regular en postfix: {expresion_postfix}")
