import ply.lex as lex

# Reserved words
reserved = {
    'create': 'CREATE',
    'table': 'TABLE',
    'insert': 'INSERT',
    'into': 'INTO',
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'values': 'VALUES',
    'primary': 'PRIMARY',
    'key': 'KEY',
}

# List of token names (including reserved words)
tokens = [
    'IDENTIFIER', 'NUMBER', 'STRING',
    'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON',
    'GT', 'LT', 'EQ'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_GT = r'>'
t_LT = r'<'
t_EQ = r'='

# Regular expressions for identifiers and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value.strip("'")  # Strip the quotes
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Function to test lexer output
def debug_lexer(input_string):
    lexer.input(input_string)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Example SQL statements
sql_statements = [
    "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(100));",
    "INSERT INTO students (id, name) VALUES (1, 'John Doe');",
    "SELECT id, name FROM students WHERE id > 0;"
]

# Test the lexer on the SQL statements
for statement in sql_statements:
    print(f"Lexing statement: {statement}")
    debug_lexer(statement)
