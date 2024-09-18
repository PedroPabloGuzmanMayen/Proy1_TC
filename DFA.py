from Automata import Automata
from graphviz import Digraph
class DFA (Automata):
    def simulate(self, expression):
        state = self.initial_state
        register = [] #Almacena los estados por los que pasa el automata
        for i in expression:
            register.append(f"From state {state} with character '{expression}'")
            
            # Verificar si el caacter es parte del alfabeto
            if i not in self.alphabet:
                return False, ["Error"]
            

            
            # Verficiar el siguiente estado en la tabla de transiciones
            if i in self.transitions[state]:
                state = self.transitions[state][i]
                register[-1] += f" to state {state}"
            else:
                # Si no hay transición válida para el caracter actual, retornar falso
                return False, ["Error"]

        # Verificar si el estado final es un estado de aceptación
        if state in self.final_states:
            return True, register
        else:
            return False, register
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