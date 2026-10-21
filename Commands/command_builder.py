from Commands.base_command import BaseCommand

class CommandBuilder:
    _commands:dict[str, BaseCommand] = {}

    @classmethod
    def register_command(cls, command:BaseCommand):
        cls._commands[command.verb] = command
        for synonym in command.synonyms:
            cls._commands[synonym] = command

    @classmethod
    def get_command(cls, verb): return cls._commands[verb]