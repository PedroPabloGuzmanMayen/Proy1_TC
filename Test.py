from shunting_yard import agregar_concatenacion_implicita, infix_a_postfix

from NFA import NFA

from DFA import DFA

from Automata import Automata

from Thompson import Thompson_Algorithm

from Subconjuntos import subsets_construction

from Minimizar import minimize


import unittest

class TestExample(unittest.TestCase):
    def test_algorithms(self):
        expression = "(a|b)*accb(a|b)*"
        word = 'aaabc'
        postfix_expression = infix_a_postfix(expression)

        auto = Thompson_Algorithm(postfix_expression)
        result, lista = auto.simulate(word)
        self.assertEqual(len(auto.states), 10)
        self.assertEqual(len(auto.transitions), 8)
        self.assertEqual(len(auto.final_states), 1)
        self.assertEqual(result, False)

    def test_subsets_construction(self):
        expression = "(a|b)*accb(a|b)*"
        word = 'accba'
        postfix_expression = infix_a_postfix(expression)

        auto1 = Thompson_Algorithm(postfix_expression)

        auto = subsets_construction(auto1)
        result, lista = auto.simulate(word)
        self.assertEqual(len(auto.states), 3)
        self.assertEqual(len(auto.transitions), 3)
        self.assertEqual(len(auto.final_states), 3)
        self.assertEqual(result, False)

    def test_minimize(self):
        expression = "(a|b)*accb(a|b)*"
        word = 'aaaabbbbbbbbaabbbacbaaaaaaabbbba'
        postfix_expression = infix_a_postfix(expression)

        auto1 = Thompson_Algorithm(postfix_expression)
        auto2 = subsets_construction(auto1)
        auto = minimize(auto2)
        result, lista = auto.simulate(word)
        self.assertEqual(len(auto.states), 1)
        self.assertEqual(len(auto.transitions), 1)
        self.assertEqual(len(auto.final_states), 1)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
