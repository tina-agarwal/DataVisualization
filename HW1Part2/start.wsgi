import os, sys

PROJECT_DIR = '/home/tina.agarwal/w209'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from A1Part2 import app as application
