from Automata import Automata

class DFA (Automata):
    def simulate(self, expression):
        state = self.initial_state
        
        for i in expression:
            print(f'Estado actual: {state}')
            
            # Verificar si el caacter es parte del alfabeto
            if i not in self.alphabet:
                return False
            
            print(f'Caracter actual: {i}')
            
            # Verficiar el siguiente estado en la tabla de transiciones
            if i in self.transitions[state]:
                state = self.transitions[state][i]
                print(f'Siguiente estado: {state}')
            else:
                # Si no hay transición válida para el caracter actual, retornar falso
                return False

        # Verificar si el estado final es un estado de aceptación
        if state in self.final_states:
            return True
        else:
            return False