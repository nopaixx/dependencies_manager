import os
import subprocess
from project.constants import c_DEPEND

class DEPEND():
    
    def __init__(self, action):
        self.action = action
        self.system_action_name = c_DEPEND

    def check(self, depend_name):
        """
        ALORDAN
        this method recibe a dependencie and check if installed on system
        """
        result = subprocess.run(['which', depend_name], stdout=subprocess.PIPE)
        if len(result.stdout)>0:
            return True
        else:
            return False

    def run(self):
        """ALORDAN
        this class know how to check dependencies
        self.actions is and array of dependencies to install
        """

        # DEPEND is only a CHECK or need install also?
        self.check(self.action[0])
        ret = "{} {}".format(self.system_action_name, " ".join(self.action))
        print(ret)
        return ret

