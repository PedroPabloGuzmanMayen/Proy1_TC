from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix

from NFA import NFA

from DFA import DFA

from Automata import Automata

from Thompson import Thompson_Algorithm

from Subconjuntos import subsets_construction

from Minimizar import minimize

expression = "(a|b)*"

word = 'ε'
expression = agregar_concatenacion_implicita(expression)
postfix_expression = infix_a_postfix(expression)

auto = Thompson_Algorithm(postfix_expression)

print(auto)


auto = subsets_construction(auto)

auto = minimize(auto)

print(auto)

print(auto.simulate(word))


