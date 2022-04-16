from unittest import TestCase

from jal.ast import Identifier, LetStatement, Program, ReturnStatement
from jal.tokens import Token, TokenType

class TestAST(TestCase):
    
    def test_let_statement(self) -> None:
        program: Program = Program(statements=[
            LetStatement(
               token=Token(TokenType.LET, literal='let'),
               name=Identifier(
                   token=Token(TokenType.IDENT, literal='var'),
                   value='var'
               ),
               value=Identifier(
                   token=Token(TokenType.IDENT, literal='another_var'),
                   value='another_var'
               ) 
            ),
        ])

        program_str = str(program)

        self.assertEqual(program_str, 'let var = another_var;')

    def test_return_statement(self) -> None:
        program: Program = Program(statements=[
            ReturnStatement(
                token=Token(TokenType.RETURN, literal='return'),
                return_value=Identifier(
                    token=Token(TokenType.ASSIGN, literal='var'),
                    value='var',
                ),
            ),
        ])
        program_str: str = str(program)
        self.assertEqual(program_str, 'return var;')