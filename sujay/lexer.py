import ply.lex as lex

class Lexer:
    tokens = (
        'DO', 'WHILE', 'IF', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON', 'IDENTIFIER', 'NUMBER',
        'EQUALS', 'MULTIPLY', 'MINUS', 'MODULO', 'PLUS'
    )

    t_DO = r'\bdo\b'
    t_WHILE = r'\bwhile\b'
    t_IF = r'\bif\b'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_SEMICOLON = r';'
    t_IDENTIFIER = r'[A-Za-z_]\w*'
    t_EQUALS = r'='
    t_MULTIPLY = r'\*'
    t_MINUS = r'-'
    t_MODULO = r'%'
    t_PLUS = r'\+'
    t_ignore = ' \t'

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMMENT(self, t):
        r'//.*'
        pass

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' on line {t.lexer.lineno}")
        t.lexer.skip(1)

    def __init__(self, source_code):
        self.source_code = source_code
        self.lexer = lex.lex(module=self)

    def tokenize(self):
        self.lexer.input(self.source_code)
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value, tok.lineno))
        return tokens

# Example usage
source_code = '''
do {
    i = i *3 - 6% 2;
} while (condition);

if (condition) {
    x = x+3
}

while (condition) {
    x = 3+3;
}
'''

lexer = Lexer(source_code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
