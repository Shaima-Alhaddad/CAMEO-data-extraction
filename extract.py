#!/usr/bin/env python3
import os
import shutil
from glob import glob

source_directory = '/YOUR PATH/CAMEO/example2026.02.21/*/servers/server#/model-1/scores/'
destination_directory = '/YOUR PATH/CAMEO/example2026.02.21/result/'

for number, filename in enumerate(glob(os.path.join(source_directory, 'complex.json'))):
    try:
        new_filename = "complex_{0}".format(number)
        new_filepath = os.path.join(destination_directory, new_filename)
        os.rename(filename, new_filepath)
    except OSError as e:
        print('Something happened:', e)
