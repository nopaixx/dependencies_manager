from project.system_commands import DEPEND, INSTALL, REMOVE, LIST, END
from project.constants import c_DEPEND, c_INSTALL, c_REMOVE, c_LIST, c_END

class CommandParser():

    def __init__(self, actions):
        """ALORDAN
        recibe one line from the json file
        and this parser manage with system action need to do each
        at the end save in self.action and object of class ACTION (DEPEND, INSTALL...)
        """

        system_action = actions.split(' ')

        if system_action[0] == c_DEPEND:
            self.action = DEPEND(system_action[1:])

        elif system_action[0] == c_INSTALL:
            self.action = INSTALL(system_action[1:])

        elif system_action[0] == c_REMOVE:
            self.action = REMOVE(system_action[1:])

        elif system_action[0] == c_LIST:
            self.action = LIST()

        elif system_action[0] == c_END:
            self.action = END()
            


    def run(self):
        """
        ALORDAN
        Command parser save and object of type DEPEND, INSTALL, etc.
        Each class implement a method run()
        """


        self.action.run()
