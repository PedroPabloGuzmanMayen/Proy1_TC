from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix

from NFA import NFA

from DFA import DFA

from Automata import Automata

from Thompson import Thompson_Algorithm

from Subconjuntos import subsets_construction

from Minimizar import minimize


import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()

expression = "(a|b)*accb(a|b)*"

word = 'aaabc'
expression = agregar_concatenacion_implicita(expression)
postfix_expression = infix_a_postfix(expression)

auto = Thompson_Algorithm(postfix_expression)

print(auto)


auto = subsets_construction(auto)

auto = minimize(auto)

print(auto)

print(auto.simulate(word))


