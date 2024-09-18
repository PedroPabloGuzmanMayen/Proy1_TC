from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix
from Thompson import Thompson_Algorithm
from Subconjuntos import subsets_construction
from Minimizar import minimize
from Automata import Automata
import itertools

exp = '(a|b)*abb'

exp = agregar_concatenacion_implicita(exp)

exp = infix_a_postfix(exp)





automata = Thompson_Algorithm(exp)


print(automata)

automata.to_graph('automata')

print(automata.epsilon_closure([automata.initial_state]))
dfa_n = subsets_construction(automata)

print(dfa_n)

print(dfa_n.simulate('aaabbbabb'))


part = minimize(dfa_n)

print(part)


print(part.simulate('aaabbbabb'))

