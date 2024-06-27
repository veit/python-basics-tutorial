class MacroCommand:
    """A command that executes a list of command."""

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()
