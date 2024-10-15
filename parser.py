import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'CREATE', 'TABLE', 'INSERT', 'INTO', 'VALUES', 'SELECT', 'FROM',
    'WHERE', 'ID', 'COMMA', 'LPAREN', 'RPAREN', 'SEMICOLON', 'STRING',
    'NUMBER', 'INT', 'VARCHAR', 'EQUALS'
)

# Token regex patterns
t_CREATE = r'CREATE'
t_TABLE = r'TABLE'
t_INSERT = r'INSERT'
t_INTO = r'INTO'
t_VALUES = r'VALUES'
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_STRING = r"'[^']*'"
t_NUMBER = r'\d+'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INT = r'INT'
t_VARCHAR = r'VARCHAR'
t_EQUALS = r'='

# Ignoring whitespace
t_ignore = ' \t\n'

# Error handling for lexer
def t_error(t):
    print(f"Lexer error: Unexpected character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parser rules
def p_statement_create(p):
    'statement : CREATE TABLE ID LPAREN column_definitions RPAREN SEMICOLON'
    print(f"Table {p[3]} created with columns: {p[5]}")

def p_column_definitions(p):
    '''column_definitions : column_definitions COMMA column_definition
                          | column_definition'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_column_definition(p):
    'column_definition : ID type_specifier'
    p[0] = (p[1], p[2])

def p_type_specifier(p):
    '''type_specifier : INT
                      | VARCHAR LPAREN NUMBER RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}({p[3]})"

def p_statement_insert(p):
    'statement : INSERT INTO ID LPAREN id_list RPAREN VALUES LPAREN value_list RPAREN SEMICOLON'
    print(f"Inserted into {p[3]}: {{ {p[5]} : {p[10]} }}")

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_value_list(p):
    '''value_list : value_list COMMA value
                  | value'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_value(p):
    '''value : STRING
             | NUMBER'''
    p[0] = p[1]

def p_statement_select(p):
    'statement : SELECT id_list FROM ID WHERE ID EQUALS value SEMICOLON'
    print(f"Selected rows from {p[4]} where {p[6]} = {p[8]}")

# Error handling for parser
def p_error(p):
    if p:
        print(f"Parser error: Unexpected token '{p.type}' with value '{p.value}' at line {p.lineno}")
    else:
        print("Parser error: Unexpected end of input")

# Build the parser
parser = yacc.yacc()

# Main execution loop
if __name__ == '__main__':
    statements = [
        "CREATE TABLE students (id INT, name VARCHAR(100));",
        "INSERT INTO students (id, name) VALUES ('1', 'John Doe');",
        "SELECT id, name FROM students WHERE id = 1;"
    ]

    for statement in statements:
        print(f"Processing SQL Statement: {statement}")
        lexer.input(statement)  # Process the input through the lexer
        for tok in lexer:  # Print out the tokens for debugging
            print(f"Token: {tok.type}, Value: {tok.value}")
        parser.parse(statement)  # Parse the statement
