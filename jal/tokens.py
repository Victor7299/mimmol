from enum import (
    auto,
    Enum,
    unique,
)
from telnetlib import AUTHENTICATION
from typing import Dict, NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DIV = auto()
    ELSE =  auto()
    EOF = auto()
    EQ = auto()
    FALSE =  auto()
    FUNCTION = auto()
    GT = auto()
    IDENT = auto()
    IF =  auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT =  auto()
    MINUS = auto()
    MULT = auto()
    NEGATION = auto()
    NOT_EQ = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN =  auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE =  auto()

    
class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'

    
def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'let': TokenType.LET,
        'false': TokenType.FALSE,
        'func': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'true': TokenType.TRUE,
    }
    return keywords.get(literal, TokenType.IDENT)