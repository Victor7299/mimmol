from unittest import TestCase

from jal.lexer import Lexer
from jal.parser import Parser
from jal.ast import Program, LetStatement



class TestParser(TestCase):
    def test_parse_program(self) -> None:
        source: str = 'let x = 5'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)

    def test_let_statement(self) -> None:
        source: str = '''
            let x = 5
            let y = 10
            let foo = 20
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 3)

        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'let')
            self.assertIsInstance(statement, LetStatement)