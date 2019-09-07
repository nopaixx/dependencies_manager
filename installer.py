import json
import os
import sys
import getopt
from project.install_manager import Manager

if __name__ == "__main__":
    app = Manager(sys.argv[1])
    app.run()
