import os
import subprocess
from project.constants import c_INSTALL
from project.system_commands import DEPEND

class INSTALL():

    def __init__(self, action):
        self.action = action
        self.system_action_name = c_INSTALL

    def get_dependencies_need(self, package):
        """ALORDAN
        This method recibe a package and ask with dependencies need
        and install if need
        apt-cache rdepends mysql-client
        """
        result = subprocess.run(['apt-cache', 'rdepends', 'mysql-client'], stdout=subprocess.PIPE)
        # TODO parser apt-cache to well formated python
        return ['TCPIP']

    def run(self):
        """ALORDAN
        this class know how to install 
        self.actions is and array of package to install
        """

        # as requirement say if some dependencie not installed we done
        # DEPEND class DONE for you
        for package in self.action:
            dependencies = self.get_dependencies_need(package)
            dep_installer = DEPEND(dependencies)
            dep_installer.run()
                

        print ("{} {}".format(self.system_action_name, " ".join(self.action)))
        pass
