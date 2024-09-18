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
        for symbol in input_string:
            next_states = set()
            
            for state in current_states:
                if symbol in self.transitions.get(state, {}):
                    for next_state in self.transitions[state][symbol]:
                        next_states.update(self.epsilon_closure({next_state}))
            
            current_states = next_states
            
            if not current_states:
                return False  
        
        
        return any(state in self.final_states for state in current_states)
    
    def to_graph(self, filename):
            # Create a new directed graph
        dot = Digraph(comment='Automaton')
    
    # Set node attributes
        dot.attr('node', shape='circle')
        dot.attr(rankdir = 'LR', size = '15.0')
        # Add states to the graph, final states are double-circled
        for state in self.states:
            if state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state)
    
    # Mark the initial state with a special arrow
        dot.node('', shape='none', width='0', height='0', label='')  # Invisible start node
        dot.edge('', self.initial_state)
    
    # Add transitions between states
        for from_state, trans_dict in self.transitions.items():
            for symbol, to_states in trans_dict.items():
                for to_state in to_states:
                    dot.edge(from_state, to_state, label=symbol)
    
    # Renderizar el autómata generado en un png
        dot.render(filename, format='png', view=False)

