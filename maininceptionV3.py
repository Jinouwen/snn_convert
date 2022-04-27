"""End-to-end example for SNN Toolbox.

This script sets up a small CNN using Keras and tensorflow, trains it for one
epoch on MNIST, stores model and dataset in a temporary folder on disk, creates
a configuration file for SNN toolbox, and finally calls the main function of
SNN toolbox to convert the trained ANN to an SNN and run it using Brian2
simulator.
"""

import os
import time
import numpy as np

from snntoolbox.bin.run import main
from snntoolbox.utils.utils import import_configparser


#main(config_filepath)
main('/tmp/pycharm_project_498/snntoolbox_applications/models/inceptionV3/config')
