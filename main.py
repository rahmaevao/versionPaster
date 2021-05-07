import subprocess
import os

start_cwd = os.getcwd()
os.chdir(r'C:\Users\RahmaevAO\STM32CubeIDE\workspace_1.6.0\stm32CanBootloader')

version_string = subprocess.check_output(["git", "describe", "--always"]).strip().decode()

uncommitted_data = subprocess.check_output(["git", "status", "--short"]).strip().decode()

if uncommitted_data != '':
    print('WARNING: There are uncommitted changes.')
    version_string += ' but not quite'

print('Version name:', version_string)

os.chdir(start_cwd)
f = open('version.h', 'w')
f.write('// This file contains the version of the last commit.\n')
f.write('// This file is generated automatically by the \n// '+ start_cwd + 'main.py' + ' script.\n')
f.write('// This script should be run before building.\n\n')
f.write('#define VERSION ' + version_string)
