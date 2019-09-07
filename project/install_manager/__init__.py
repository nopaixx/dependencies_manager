from project.command_parser import CommandParser


class Manager():
""" ALORDAN

This is main class can manage all the action
is a minimalistic code thanks to POO
"""

    def __init__(self, args):

        self.parser_json(args)

    def parse_json(self, file):
        with open(file) as json_file:
          self.file_actionsdata = json.load(json_file)

    def run():

        for action in self.file_actions:
            command = CommandParser(action)
            commnad.run()

        # code end
