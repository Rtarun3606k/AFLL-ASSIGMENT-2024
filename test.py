import unittest
from PnewParser import yacc

class TestNewParser(unittest.TestCase):

    def setUp(self):
        self.parser = yacc

    def test_lst_condition(self):
        result = self.parser.parse("name > 5")
        self.assertEqual(result.children[0].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[1].value, 'name > 5')

    def test_lst_and_condition(self):
        result = self.parser.parse("name > 5 AND age < 10")
        self.assertEqual(result.children[0].value, '[CONDITIONS]')
        self.assertEqual(result.children[1].value, '[AND]')
        self.assertEqual(result.children[0].children[0].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[0].children[1].value, 'name > 5')
        self.assertEqual(result.children[0].children[2].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[2].children[1].value, 'age < 10')

    def test_lst_or_condition(self):
        result = self.parser.parse("name > 5 OR age < 10")
        self.assertEqual(result.children[0].value, '[CONDITIONS]')
        self.assertEqual(result.children[1].value, '[OR]')
        self.assertEqual(result.children[0].children[0].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[0].children[1].value, 'name > 5')
        self.assertEqual(result.children[0].children[2].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[2].children[1].value, 'age < 10')

    def test_lst_between_condition(self):
        result = self.parser.parse("age BETWEEN 5 AND 10")
        self.assertEqual(result.children[0].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[1].value, 'age >= 5 & age <= 10')

    def test_lst_in_condition(self):
        result = self.parser.parse("name IN (SELECT name FROM table)")
        self.assertEqual(result.children[0].children[0].value, 'name')
        self.assertEqual(result.children[0].children[1].value, '[IN]')
        self.assertEqual(result.children[0].children[2].value, '[QUERY]')

    def test_lst_agg_condition(self):
        result = self.parser.parse("name < SUM(age)")
        self.assertEqual(result.children[0].children[0].value, '[TERM]')
        self.assertEqual(result.children[0].children[1].value, 'name < SUM(age)')

if __name__ == '__main__':
    unittest.main()