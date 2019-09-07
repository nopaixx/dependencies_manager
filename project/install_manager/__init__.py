import json
from project.command_parser import CommandParser


class Manager():
    """ ALORDAN

    This is main class can manage all the action
    is a minimalistic code thanks to POO
    """

    def __init__(self, args):
        self.parse_json(args)

    def parse_json(self, file):
        with open(file) as json_file:
          self.file_actions = json.load(json_file)

    def run(self):

        for action in self.file_actions:
            command = CommandParser(action['command'])
            command.run()

        # code end
