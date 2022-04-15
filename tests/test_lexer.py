from unittest import TestCase
from typing import List

from jal.tokens import (
    Token,
    TokenType,
)
from jal.lexer import Lexer

class TestLexer(TestCase):
    
    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+-/*<>!'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.DIV, '/'),
            Token(TokenType.MULT, '*'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NEGATION, '!'),
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_delimiters(self) -> None:
        source: str = '(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS,'+'),
            Token(TokenType.EOF, '')
        ]
        
        self.assertEqual(tokens, expected_tokens)

    def test_assignement(self) -> None:
        source: str = 'let five = 5'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(4):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'five'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
        ]
        
        self.assertEqual(tokens, expected_tokens)

    def test_function_declaration(self) -> None:
        source: str = '''
            let add = func(x, y) {
                x + y
            }
        '''
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(14):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'add'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.FUNCTION, 'func'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RBRACE, '}'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_function_call(self) -> None:
        source: str = 'let result = suma(dos,tres)'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(9):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'result'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
        ]

        self.assertEqual(tokens, expected_tokens)


    def test_control_statement(self) -> None:
        source: str = '''
            if (5 < 10){
                return true
            } else{
                return false
            }
        '''
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(15):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.TRUE, 'true'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.FALSE, 'false'),
            Token(TokenType.RBRACE, '}'),
        ]
        self.assertEqual(tokens, expected_tokens)
    
    def test_two_character_operator(self) -> None:
        source = '''
            10 == 10
            10 != 9
        '''
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(6):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.INT, '10'),
            Token(TokenType.EQ, '=='),
            Token(TokenType.INT, '10'),
            Token(TokenType.INT, '10'),
            Token(TokenType.NOT_EQ, '!='),
            Token(TokenType.INT, '9'),
        ]

        self.assertEqual(tokens, expected_tokens)