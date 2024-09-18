from Automata import Automata
from graphviz import Digraph
class NFA(Automata):

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop() 
        # Si el estado tiene transiciones epsilon seguimos
            if 'ε' in self.transitions.get(state, {}):
                for next_state in self.transitions[state]['ε']:
                    if next_state not in closure:
                        closure.add(next_state) 
                        stack.append(next_state)
        return closure  # Devuelve el conjunto de estados alcanzables por ε-transiciones
    def move(self, states, symbol):
        next_states = set() 
        for state in states:
        # Si hay una transición con el símbolo, se añaden los estados alcanzados
            if symbol in self.transitions.get(state, {}):
                next_states.update(self.transitions[state][symbol])
        return next_states 
    def simulate(self, input_string):

        current_states = self.epsilon_closure({self.initial_state})
        register = [] #Almacena los estados por los que pasa el automata
        for symbol in input_string:
            register.append(f"Desde los estados {current_states} con caracter '{symbol}'")
            next_states = set()
            
            for state in current_states:
                if symbol in self.transitions.get(state, {}):
                    for next_state in self.transitions[state][symbol]:
                        next_states.update(self.epsilon_closure({next_state}))
            
            current_states = next_states
            register[-1] += f" A los estados {current_states}"
            
            if not current_states:
                return False , register
        
        
        return any(state in self.final_states for state in current_states), register
    
    def to_graph(self, filename):
            
        dot = Digraph(comment='Automaton')
    
        #Definimos los atributos del grafo
        dot.attr('node', shape='circle')
        dot.attr(rankdir = 'LR', size = '15.0')
        
        for state in self.states:
            if state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)
    
    
        dot.node('', shape='none', width='0', height='0', label='')  
        dot.edge('', self.initial_state)
    
        for from_state, trans_dict in self.transitions.items():
            for symbol, to_states in trans_dict.items():
                for to_state in to_states:
                    dot.edge(from_state, to_state, label=symbol)
    
    # Renderizar el autómata generado en un png
        dot.render(filename, format='png', view=False)

