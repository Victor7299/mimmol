from jal.ast import Program
from jal.lexer import Lexer

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer

    def parse_program(self) -> Program:
        program: Program = Program(statements=[])

        return program