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


print(dfa2)

print(dfa2.initial_state)