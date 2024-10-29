import unittest
from parser import p_condition, tokens

import ply.lex as lex
import ply.yacc as yacc

class TestDartParser(unittest.TestCase):
    def setUp(self):
        self.lexer = lex.lex(module=lexer)
        self.parser = yacc.yacc(module=lexer)

    def test_condition_eq(self):
        result = self.parser.parse("a == b", lexer=self.lexer)
        self.assertEqual(result, ('==', 'a', 'b'))

    def test_condition_ne(self):
        result = self.parser.parse("a != b", lexer=self.lexer)
        self.assertEqual(result, ('!=', 'a', 'b'))

    def test_condition_lt(self):
        result = self.parser.parse("a < b", lexer=self.lexer)
        self.assertEqual(result, ('<', 'a', 'b'))

    def test_condition_gt(self):
        result = self.parser.parse("a > b", lexer=self.lexer)
        self.assertEqual(result, ('>', 'a', 'b'))

    def test_condition_le(self):
        result = self.parser.parse("a <= b", lexer=self.lexer)
        self.assertEqual(result, ('<=', 'a', 'b'))

    def test_condition_ge(self):
        result = self.parser.parse("a >= b", lexer=self.lexer)
        self.assertEqual(result, ('>=', 'a', 'b'))

if __name__ == '__main__':
    unittest.main()