from LEXER import Lexer
from PARSER import Parser

def run(text):
    # Tokens
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Arbol sintactico
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.error