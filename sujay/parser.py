import ply.yacc as yacc
import ply.lex as lex

# Define tokens
tokens = (
    'IF', 'ELSE', 'WHILE', 'DO', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
    'IDENTIFIER', 'NUMBER', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 'SEMI', 'ASSIGN', 'PLUS'
)

# Define token regex patterns
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_DO = r'do'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_SEMI = r';'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_ignore = ' \t'  # Ignore whitespace and tabs

# Define identifier and number tokens
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in ('if', 'else', 'while', 'do'):
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Handle errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parsing rules
def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN block else_block'''
    p[0] = ('if', p[3], p[5], p[6])

def p_else_block(p):
    '''else_block : ELSE block
                  | empty'''
    p[0] = p[2] if len(p) > 2 else None

def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN block'''
    p[0] = ('while', p[3], p[5])

def p_do_while_statement(p):
    '''do_while_statement : DO block WHILE LPAREN condition RPAREN SEMI'''
    p[0] = ('do-while', p[2], p[5])

def p_condition(p):
    '''condition : expression EQ expression
                 | expression NE expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression'''
    p[0] = (p[2], p[1], p[3])

def p_block(p):
    '''block : LBRACE statements RBRACE'''
    p[0] = p[2]

def p_statements(p):
    '''statements : statement statements
                  | statement
                  | if_statement statements
                  | if_statement
                  | while_statement statements
                  | while_statement
                  | do_while_statement statements
                  | do_while_statement'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression SEMI
                 | IDENTIFIER ASSIGN expression SEMI'''
    if len(p) == 5:
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = p[1]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression'''
    if len(p) == 4:
        p[0] = ('+', p[1], p[3])
    else:
        p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# test the code
data = '''
if (x == 1) {
    y = 2;
} else {
    y = 3;
}

while (x < 10) {
    x = x + 1;
}

do {
    x = x + 1;
} while (x < 20);
'''
result = parser.parse(data, lexer=lexer)
print(result)