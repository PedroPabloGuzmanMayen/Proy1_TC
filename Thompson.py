from Automata import Automata
from NFA import NFA

# Función para extraer los símbolos del alfabeto de la expresión regular
def extraer_alfabeto(expresion_regular):
    # Definir los operadores comunes de expresiones regulares
    operadores = set('|()*+')
    
    # Extraer todos los caracteres que no sean operadores
    alfabeto = {char for char in expresion_regular if char not in operadores}
    
    return alfabeto

def initialize_automata(expression, state_counter):
    return NFA([(expression + str(state_counter) + '1'), (expression + str(state_counter) +'2')], {expression},expression + str(state_counter) + '1', [expression + str(state_counter) + '2'],
                    {expression + str(state_counter) + '1': {expression: [expression + str(state_counter) + '2']}})

def concat_automata(automata1, automata2):
    alphabet = automata1.alphabet.union(automata2.alphabet)
    automata2.states.remove(automata2.initial_state) #Remover el estado inicial del segundo autómata
    states = automata1.states + automata2.states #Combinar los estados de los 2 automatas
    final = automata2.transitions.pop(automata2.initial_state) #Transiciones del estado inicial del segundo automata

    if automata1.final_states[0] in automata1.transitions: #Comprobar si el estado final del primer aútomata tiene transiciones
        automata1.transitions[automata1.final_states[0]].update(final)
    else:
        automata1.transitions[automata1.final_states[0]] = final

    automata1.transitions.update(automata2.transitions) #Actualizar la lista de transiciones
    transitions = automata1.transitions
    

    return NFA(states, alphabet, automata1.initial_state, [automata2.final_states[0]], transitions)
    
def kleeneStar(automata, state_counter):
    states = automata.states
    states.insert(0, "k" + str(state_counter)) #Añadir un nuevo estado inicial
    states.append("j" + str(state_counter)) #Añadir un nuevo estado final
    transitions = {states[0]: {"ε": [automata.initial_state, states[len(states)-1]]}} #Agregar las transiciones para el estado inicial
    transitions.update(automata.transitions) #Añadir a la nueva lista de transiciones las transiciones del automata original
    transitions[automata.final_states[0]] = {"ε": [automata.initial_state, states[len(states)-1]]} #Añadir la epsilon-transición para el estado final del automata original
    return NFA(states, automata.alphabet, states[0], [states[len(states)-1]], transitions)
    

def or_operation(automata1, automata2, state_counter):

    states = automata1.states + automata2.states #Sumar los estados de ambos automatas
    states.insert(0, "i" + str(state_counter)) #Añadir un nuevo estado inicial
    states.append("h" + str(state_counter)) #Añadir un nuevo estado final
    transitions = {states[0]: {"ε":[automata1.initial_state, automata2.initial_state]}} #Agregar transiciones al estado inicial
    transitions.update(automata1.transitions) #Añadir las transiciones del primer automata
    transitions.update(automata2.transitions) #Añadir transiciones del segundo automata
    transitions[automata1.final_states[0]] = {"ε": [states[len(states)-1]]} #Agregar la epsilon transicion al estado final del primer automata
    transitions[automata2.final_states[0]] = {"ε": [states[len(states)-1]]} #Agregar la epsilon transicion al estado final del srgundo automata

    return NFA(states, automata1.alphabet.union(automata2.alphabet), states[0],[states[len(states)-1]], transitions )



def Thompson_Algorithm(regex):
    alphabet = extraer_alfabeto(regex)
    operators = ['|', '.', '*', '(', ')']
    automata_stack = []
    state_counter = 1

    for i in regex:
        if i not in operators: #verificar si es un operador a una expresión
            automata_stack.append(initialize_automata(i, state_counter)) #Si es una operación, creamos un autómata para dicha expresión y lo agregamos al stack
            state_counter += 1
        else:

            if i == ".": #Si la operación es concatenación
                automata2 = automata_stack.pop()
                automata1 = automata_stack.pop() #Sacamos los dos últimos autómatas en el stack
                automata_stack.append(concat_automata(automata1, automata2)) #Añadimos al stack la concatenación de los dos autómatas inciales
            elif i == "|": #Si la operación es un or
                automata2 = automata_stack.pop()
                automata1 = automata_stack.pop() #Sacamos del stack los últimos 2 autómatas
                automata_stack.append(or_operation(automata1, automata2, state_counter)) #Realizamos la operación or en los autómatas
            elif i == "*": #Si la operación es la estrella de Kleene
                automata = automata_stack.pop() #Sacamos el útlimo autómata del stack
                automata_stack.append(kleeneStar(automata, state_counter)) #Hacemos la operación de la estrella de Kleene y añadimos el resultado al stack
    return automata_stack.pop() #Devolvemos el último autómata en el stack


