import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = (
    'SELECT', 'DELETE', 'DROP', 'FROM', 'WHERE', 'AS', 'AND', 'OR', 
    'NAME', 'NUMBER', 'LP', 'RP', 'COMMA', 'EQ', 'LT', 'GT', 
    'ALTER', 'TABLE', 'ADD', 'COUNT', 'SUM', 'AVG', 'MIN', 'MAX'
)

# Token definitions
t_SELECT = r'SELECT'
t_DELETE = r'DELETE'
t_DROP = r'DROP'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_AS = r'AS'
t_AND = r'AND'
t_OR = r'OR'
t_LP = r'\('
t_RP = r'\)'
t_COMMA = r','
t_EQ = r'='
t_LT = r'<'
t_GT = r'>'
t_ALTER = r'ALTER'
t_TABLE = r'TABLE'
t_ADD = r'ADD'
t_COUNT = r'COUNT'
t_SUM = r'SUM'
t_AVG = r'AVG'
t_MIN = r'MIN'
t_MAX = r'MAX'

# Reserved words - to prevent conflicts with NAME tokens
reserved = {
    'alter': 'ALTER',
    'table': 'TABLE',
    'add': 'ADD',
    'drop': 'DROP',
    'delete': 'DELETE'
}

# Modified NAME token to ignore keywords
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'NAME')  # Check if it's a keyword
    print(f"{t.type} token recognized: {t.value}")
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    print(f"NUMBER token recognized: {t.value}")
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Node class for parse tree representation
class Node:
    def __init__(self, type):
        self.type = type
        self.children = []

    def add(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.type) + "\n"
        for child in self.children:
            if isinstance(child, Node):
                ret += child.__repr__(level + 1)
            else:
                ret += "\t" * (level + 1) + repr(child) + "\n"
        return ret

# Parsing rules
def p_error(t):
    if t:
        print(f"Syntax error at '{t.value}'")
    else:
        print("Syntax error at EOF")

def p_query(t):
    '''query : delete
             | select
             | alter_table
             | drop_table'''
    t[0] = t[1]

def p_delete(t):
    '''delete : DELETE FROM NAME WHERE condition
              | DELETE FROM NAME'''
    t[0] = Node('QUERY')
    t[0].add(Node('[DELETE]'))
    t[0].add(Node('[FROM]'))
    t[0].add(Node(t[3]))
    if len(t) == 6:
        t[0].add(Node('[WHERE]'))
        t[0].add(t[5])

def p_select(t):
    '''select : SELECT NAME FROM NAME WHERE condition
              | SELECT NAME FROM NAME'''
    t[0] = Node('QUERY')
    t[0].add(Node('[SELECT]'))
    t[0].add(Node(t[2]))
    t[0].add(Node('[FROM]'))
    t[0].add(Node(t[4]))
    if len(t) == 6:
        t[0].add(Node('[WHERE]'))
        t[0].add(t[5])

def p_alter_table(t):
    '''alter_table : ALTER TABLE NAME ADD NAME NAME'''
    t[0] = Node('QUERY')
    t[0].add(Node('[ALTER]'))
    t[0].add(Node('[TABLE]'))
    t[0].add(Node(t[3]))  # table_name
    t[0].add(Node('[ADD]'))
    t[0].add(Node(t[5]))  # column_name
    t[0].add(Node(t[6]))  # datatype

def p_drop_table(t):
    '''drop_table : DROP TABLE NAME'''
    t[0] = Node('QUERY')
    t[0].add(Node('[DROP]'))
    t[0].add(Node('[TABLE]'))
    t[0].add(Node(t[3]))  # table_name

def p_condition(t):
    '''condition : NAME EQ NUMBER
                 | NAME LT NUMBER
                 | NAME GT NUMBER
                 | condition AND condition
                 | condition OR condition'''
    if len(t) == 4:
        if t[2] == 'AND' or t[2] == 'OR':
            t[0] = Node(f'[CONDITION_{t[2]}]')
            t[0].add(t[1])
            t[0].add(t[3])
        else:
            t[0] = Node(f'[CONDITION]')
            t[0].add(Node(f"{t[1]} {t[2]} {t[3]}"))
    else:
        t[0] = Node(f'[CONDITION]')
        t[0].add(Node(f"{t[1]} {t[2]} {t[3]}"))

# Aggregation functions rule
def p_agg(t):
    '''agg : COUNT LP NAME RP
           | SUM LP NAME RP
           | AVG LP NAME RP
           | MIN LP NAME RP
           | MAX LP NAME RP'''
    t[0] = Node('[AGGREGATE]')
    t[0].add(Node(t[1]))
    t[0].add(Node(t[3]))

# Build the parser
parser = yacc.yacc()

# Testing the parser with an ALTER TABLE statement
test_inputs = [
    "ALTER TABLE table_name ADD column_name datatype",
    "DELETE FROM table_name WHERE id = 5",
    "DROP TABLE table_name"
]

for test_input in test_inputs:
    lexer.input(test_input)
    print("Tokens:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    print("\nParse Tree:")
    result = parser.parse(test_input)
    print(result)
