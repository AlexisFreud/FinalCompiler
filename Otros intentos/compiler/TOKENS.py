TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_STRING = "STRING"
TT_IDENTIFIER = "IDENTIFIER"
TT_KEYWORD = "KEYWORD"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_EXP = "EXP"
TT_EQ = "EQ"
TT_EE = "EE"
TT_NE = "NE"
TT_LT = "LT"
TT_LTE = "LTE"
TT_GT = "GT"
TT_GTE = "GTE"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_EOF = "EOF"

KEYWORDS = [
    'Int',
    'Float',
    'String',
    'Boolean',
    'if',
    'else',
    'elif',
    'while',
    'do',
    'for',
    'and',
    'or'
]


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        """
        Es la manera 'pythonica' de hacer un toString()
        :return:
        """
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'
