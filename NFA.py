from Automata import Automata

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

