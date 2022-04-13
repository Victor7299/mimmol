from calendar import IllegalMonthError
import re

from mylang.tokens import (
    Token,
    TokenType,
)

class Lexer:
    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        match self._character:
            case '=':
                token = Token(TokenType.ASSIGN, self._character)
            case '+':
                token = Token(TokenType.PLUS, self._character)
            case '(':
                token = Token(TokenType.LPAREN, self._character)
            case ')':
                token = Token(TokenType.RPAREN, self._character)
            case '{':
                token = Token(TokenType.LBRACE, self._character)
            case '}':
                token = Token(TokenType.RBRACE, self._character)
            case ';':
                token = Token(TokenType.SEMICOLON, self._character)
            case ',':
                token = Token(TokenType.COMMA, self._character)
            case 'a':
                literal = self._read_identifier()
                token_type = looukp_token_identifier(literal)
                return Token(token_type, literal)
            case '':
                token = Token(TokenType.EOF, self._character)
            case _:
                token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token
    
    def _is_letter(self):
        'a'
        return 

    def _read_character(self) -> None:

        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]


        self._position = self._read_position
        self._read_position += 1