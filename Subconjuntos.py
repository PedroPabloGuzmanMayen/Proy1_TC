from Automata import Automata
from NFA import NFA
from DFA import DFA
# Función que calcula el cierre de un conjunto de estados.
def epsilon_closure(automata, states):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop() 
        # Si el estado tiene transiciones epsilon seguimos
        if 'ε' in automata.transitions.get(state, {}):
            for next_state in automata.transitions[state]['ε']:
                if next_state not in closure:
                    closure.add(next_state) 
                    stack.append(next_state)

    return closure  # Devuelve el conjunto de estados alcanzables por ε-transiciones

# Función que aplica la transición de un conjunto de estados bajo un símbolo dado.
def move(automata, states, symbol):
    next_states = set() 
    for state in states:
        # Si hay una transición con el símbolo, se añaden los estados alcanzados
        if symbol in automata.transitions.get(state, {}):
            next_states.update(automata.transitions[state][symbol])
    return next_states 

# Función que implementa la construcción de subconjuntos (convierte AFN a AFD).
def subsets_construction(nfa):
    # Calcula el cierre epsilon del estado inicial del AFN
    initial_closure = nfa.epsilon_closure([nfa.initial_state])
    states = [initial_closure] 
    unmarked_states = [initial_closure]
    dfa_transitions = {} 

    # Mientras haya estados sin explorar
    while unmarked_states:
        current_closure = unmarked_states.pop()
        for symbol in nfa.alphabet:
            next_closure = nfa.epsilon_closure(nfa.move(current_closure, symbol))
            if next_closure not in states: 
                states.append(next_closure)
                unmarked_states.append(next_closure)
            dfa_transitions[frozenset(current_closure)] = dfa_transitions.get(frozenset(current_closure), {})
            dfa_transitions[frozenset(current_closure)][symbol] = frozenset(next_closure)

    # Mapeamos los conjuntos de estados a índices enteros para el AFD
    state_mapping = {frozenset(state): idx for idx, state in enumerate(states)}
    dfa_states = list(state_mapping.values()) 
    dfa_initial_state = state_mapping[frozenset(initial_closure)]
    dfa_final_states = [state_mapping[frozenset(s)] for s in states if any(fs in s for fs in nfa.final_states)]

    dfa_transitions = {state_mapping[s]: {sym: state_mapping[t] for sym, t in trans.items()} for s, trans in dfa_transitions.items()}

    return DFA(dfa_states, nfa.alphabet, dfa_initial_state, dfa_final_states, dfa_transitions)

