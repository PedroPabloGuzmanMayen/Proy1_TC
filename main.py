# Importar las funciones desde los archivos correspondientes
from shunting_yard import infix_a_postfix, agregar_concatenacion_implicita
from Thompson import Thompson_Algorithm


expression = input("Ingresa la expresión regular: ")
expression = agregar_concatenacion_implicita(expression)
expression = infix_a_postfix(expression)
print(expression)
NFA = Thompson_Algorithm(expression)

print(NFA)

print(len(NFA.states))

