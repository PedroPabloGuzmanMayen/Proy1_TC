from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix
from Thompson import Thompson_Algorithm
from Subconjuntos import subsets_construction
from Minimizar import minimization
from Automata import Automata
import itertools

exp = 'aa(bb)*c'

exp = agregar_concatenacion_implicita(exp)

exp = infix_a_postfix(exp)

automata = Thompson_Algorithm(exp)


dfa1 = subsets_construction(automata)



dfa2 = minimization(dfa1)


dfa2.to_graph()

auto2 = Automata(['A', 'B', 'C', 'D', 'E', 'F', 'G'], {'r', 'b'}, 'A', ['F', 'G'], 
                 {'A': {'r':'B', 'b':'C'},
                  'B': {'r': 'D', 'b':'E'},
                  'C':{'r':'D', 'b':'F'},
                  'D': {'r':'D', 'b':'G'},
                  'E':{'r':'D', 'b':'G'},
                  'F':{'r':'D', 'b':'C'},
                  'G':{'r':'D', 'b':'G'}})

print(auto2)

state = auto2.simulate('rbb')

print(state)