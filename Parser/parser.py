class Lexer:
    @classmethod
    def lex(cls, command_str:str):
        return command_str.split()

class Parser:
    @classmethod
    def parse(cls, command_str:str):
        lexed_command_str = Lexer.lex(command_str)