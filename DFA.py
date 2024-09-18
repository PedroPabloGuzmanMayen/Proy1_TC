from Automata import Automata

class DFA (Automata):
    def simulate(self, expression):
        state = self.initial_state
        for i in expression:
            print(f'Estado actual: {state}')
            if expression not in self.alphabet and expression != 'ε':
                return False
            else:
                print(f'Caracter actual: {i}')
                if expression == 'ε':
                    continue
                else:
                    state = self.transitions[state][i]
                    print(f'Siguiente estado: {state}')

        if state in self.final_states:
            return True
        else:
            return False