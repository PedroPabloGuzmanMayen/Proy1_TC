# Importar las funciones desde los archivos correspondientes
from shunting_yard import infix_a_postfix, agregar_concatenacion_implicita

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


# Función principal para ejecutar el programa
if __name__ == "__main__":
    # Llamar a la función para leer la entrada
    expresion_regular, cadena, epsilon, alfabeto = leer_entrada()
    
    # Convertir la expresión regular a postfix
    expresion_postfix = infix_a_postfix(expresion_regular)
    
    # Mostrar la expresión en notación postfix
    print(f"\nExpresión regular en postfix: {expresion_postfix}")

#entrada: (5*4+3*)-1
#salida: 54*3*+1-

