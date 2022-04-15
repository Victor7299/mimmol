from jal.lexer import Lexer
from jal.tokens import Token, TokenType

EOF_TOKEN: Token = Token(TokenType.EOF, '')

def start_repl() -> None:
    while (source := input('jal >> ')) != 'exit()':
        lexer: Lexer = Lexer(source)

        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)