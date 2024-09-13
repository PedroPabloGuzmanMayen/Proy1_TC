from Automata import Automata

# Función que minimiza un AFD usando el algoritmo de particiones (Hopcroft).
def minimization(dfa):
    # Inicializa las particiones en estados finales y no finales
    P = [set(dfa.final_states), set(dfa.states) - set(dfa.final_states)]
    W = [set(dfa.final_states)]  # Conjunto de estados para explorar/refinar

    # Mientras haya particiones por refinar
    while W:
        A = W.pop() 
        for symbol in dfa.alphabet: 
            X = {state for state in dfa.states if symbol in dfa.transitions.get(state, {}) and dfa.transitions[state][symbol] in A}
            for Y in P.copy():  # Para cada partición en P
                intersection = X & Y
                difference = Y - X 
                if intersection and difference:
                    P.remove(Y) 
                    P.append(intersection)
                    P.append(difference)
                    if Y in W:
                        W.remove(Y)
                        W.append(intersection)
                        W.append(difference)
                    else:
                        W.append(intersection if len(intersection) <= len(difference) else difference)

    # Mapeamos las nuevas particiones a estados enteros del AFD
    new_states = {frozenset(part): idx for idx, part in enumerate(P)}
    # Los estados finales serán aquellos que contienen algún estado final original
    new_final_states = [new_states[frozenset(part)] for part in P if any(fs in part for fs in dfa.final_states)]
    new_transitions = {}

    # Reasigna las transiciones del AFD según las nuevas particiones
    for part in P:
        state_rep = list(part)[0]  # Escoge un estado representante de la partición
        new_state = new_states[frozenset(part)] 
        new_transitions[new_state] = {}
        for symbol in dfa.alphabet:
            if symbol in dfa.transitions.get(state_rep, {}):
                target_state = dfa.transitions[state_rep][symbol]
                new_transitions[new_state][symbol] = new_states[frozenset(next(p for p in P if target_state in p))]
    return Automata(list(new_states.values()), dfa.alphabet, new_states[frozenset([dfa.initial_state])], new_final_states, new_transitions)

