from abc import ABC

class BaseCommand(ABC):
    def __init__(self, verb, synonyms, description):
        super().__init__()
        self.verb = verb
        self.synonyms = synonyms
        self.description = description

    def execute(self, command_string):
        pass