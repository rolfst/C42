import os
import glob
from os import path


stubs = dict()

__dir = path.dirname(os.path.realpath(__file__))
__files = glob.glob(__dir + path.sep + '*.json')
for file in __files:
    base = os.path.basename(file)
    filename = os.path.splitext(base)[0]
    with open(file) as jsonfile:
        stubs[filename] = jsonfile.read().replace('\n', '')
