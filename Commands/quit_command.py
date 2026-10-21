from Commands.base_command import BaseCommand

class QuitCommand(BaseCommand):
    def __init__(self, name, synonyms, description):
        super().__init__(name, synonyms, description)

    def execute(self, engine_ref):
        engine_ref.running = False