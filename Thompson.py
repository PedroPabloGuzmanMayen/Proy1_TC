from Automata import Automata

state_counter = 1
# Función para extraer los símbolos del alfabeto de la expresión regular
def extraer_alfabeto(expresion_regular):
    # Definir los operadores comunes de expresiones regulares
    operadores = set('|()*+')
    
    # Extraer todos los caracteres que no sean operadores
    alfabeto = {char for char in expresion_regular if char not in operadores}
    
    return alfabeto

def initialize_automata(expression, state_counter):
    return Automata([(expression + str(state_counter) + '1'), (expression + str(state_counter) +'2')], {expression},expression + str(state_counter) + '1', [expression + str(state_counter) + '2'],
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
    

    return Automata(states, alphabet, automata1.initial_state, [automata2.final_states[0]], transitions)
    
def kleeneStar(automata, state_counter):
    states = automata.states
    states.insert(0, "k" + str(state_counter)) #Añadir un nuevo estado inicial
    states.append("j" + str(state_counter)) #Añadir un nuevo estado final
    transitions = {states[0]: {"ε": [automata.initial_state, states[len(states)-1]]}} #Agregar las transiciones para el estado inicial
    transitions.update(automata.transitions) #Añadir a la nueva lista de transiciones las transiciones del automata original
    transitions[automata.final_states[0]] = {"ε": [automata.initial_state]} #Añadir la epsilon-transición para el estado final del automata original
    return Automata(states, automata.alphabet, states[0], [states[len(states)-1]], transitions)
    

def or_operation(automata1, automata2):
    pass




def Thompson_Algorithm(regex):
    alphabet = extraer_alfabeto(regex)
    operators = ['|', '.', '*', '(', ')']

    for i in regex:
        if i not in operators:
            pass



auto = initialize_automata('a', state_counter)
auto2 = initialize_automata('b', state_counter)
auto3 = concat_automata(auto, auto2)
auto4 = kleeneStar(auto3, state_counter)



print(auto4)