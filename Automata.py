import json
from graphviz import Digraph
class Automata:

    def __init__(self, states, alphabet, initial_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
    #Escribe un automata a formato json
    def to_json(self):
        automata = {
            "Q": self.states,
            "Σ": self.alphabet,
            "q0": self.initial_state,
            "F": self.final_states,
            "δ": self.transitions
        }
        return json.dumps(automata, indent=4)

    #Escribe un nuevo automata a partir de un archivo json
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(
            states=data["Q"],
            alphabet=data["Σ"],
            initial_state=data["q0"],
            final_states=data["F"],
            transitions=data["δ"]
        )
    #Imprime la información del automata
    def __repr__(self):
        return (f"Automaton(states={self.states}, alphabet={self.alphabet}, "
                f"initial_state={self.initial_state}, final_states={self.final_states}, "
                f"transitions={self.transitions})")
    
    def to_graph(self, filename):
        dot = Digraph()
        dot.attr(rankdir = 'LR', size = '15.0')
    # Añadimos los estados
        for state in self.states:
            #Si el estado es un estado de aceptación, dibujamos un doble ciírculo
            if state in self.final_states:
                dot.node(str(state), shape='doublecircle')
            else:
                dot.node(str(state), shape='circle')

    # Marcamos el estado inicial con una flecha
        dot.node("", shape="none")  
        dot.edge("", str(self.initial_state)) 

    # Agregamos las transiciones
        for state, paths in self.transitions.items():
            for symbol, next_states in paths.items():
                for next_state in str(next_states):
                    dot.edge(str(state), str(next_state), label=symbol)

        dot.render(filename, format='png', view=False)

    def simulate(self, expression):
        state = self.initial_state
        for i in expression:
            state = self.transitions[state][i]

        if state in self.final_states:
            return True
        else:
            return False

