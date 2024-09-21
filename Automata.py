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
    def to_json(self, filename):
        automata = {
            "Q": self.states,
            "Σ": list(self.alphabet),
            "q0": self.initial_state,
            "F": self.final_states,
            "δ": self.transitions
        }

        if filename:
            with open(filename, 'w') as json_file:
                json_file.write(json.dumps(automata, indent=4))
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
        return (f"Automaton(\n"
            f"  states={self.states},\n"
            f"  alphabet={self.alphabet},\n"
            f"  initial_state={self.initial_state},\n"
            f"  final_states={self.final_states},\n"
            f"  transitions={self.transitions}\n"
            f")")

    

