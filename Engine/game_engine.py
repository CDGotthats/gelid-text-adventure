from Commands.command_builder import CommandBuilder
from Commands.quit_command import QuitCommand

class GameEngine:
    running = False
    player_input = ""

    @classmethod
    def init(cls):
        cls.running = True
        CommandBuilder.register_command(QuitCommand("quit", ["q"], "quits the game"))
        print("Hello world!")

    @classmethod
    def tick(cls):
        cls.player_input = input(">_ ")

    @classmethod
    def update(cls):
        CommandBuilder.get_command(cls.player_input).execute(cls)

    @classmethod
    def run(cls):
        cls.init()
        while cls.running:
            cls.tick()
            cls.update()
        print("Goodbye world!")