# -*- coding: utf-8 -*-
# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# contact_management_python.py is a Contact Management Tkinter application.
#
# PLEASE FOLLOW THESE DIRECTIONS:
#
# STEP #1:
#
# Edit this script to adjust the path names of these two lines in the
# script to match your specific PYTHON Library paths for tcl and tk:
#  
# os.environ['TCL_LIBRARY'] = "C:/Users/chipcoder4972/AppData/Local/Programs/Python/Python36/tcl/tcl8.6"
# os.environ['TK_LIBRARY'] = "C:/Users/chipcoder4972/AppData/Local/Programs/Python/Python36/tcl/tk8.6"
#
# Note: Be sure to use forward slashes to avoid a common build error locating these libraries. 
#
# STEP #2:
#
# Locate your PYTHON tcl and tk DLL files installed with Python (i.e. Python Version 3.6.2):
# These two DLL files, tcl86t.dll and tk86t.dll, are at a path similar to this:
# C:\Users\chipcoder4972\AppData\Local\Programs\Python\Python36\DLLs
# COPY these two files, tcl86t.dll and tk86t.dll, to the directory
# where you are running this setup.py script. (so they are local files
# that the script finds easily). 
# 
# STEP #3:    python setup.py build 
# 
# Run the build process by running this setup.py script with
# the command: 'python setup.py build'
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/script.html 
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application,
# which runs by double clicking "contact_management_python.exe". 
#
# Thus, in the subdirectory .... \build\exe.win-amd64-3.6   look for the executable
# called "contact_management_python.exe" and double click on it to verify
# that the executable runs ok.
#
# STEP #4:
#
# Resolve any BUILD errors that may appear
# as a POP-UP BOX by googling the solution, typically on stackoverflow. 
#
# Once this contact_management_python.exe runs successfully (with no error box popup),
# then the setup.py script has generated a CLEAN BUILD or a GOOD BUILD,
# by creating the "contact_management_python" executable, which you then verifyied
# by observing the application runs without errors, the next step is to:
#
# STEP #5:    python setup.py bdist_msi 
# 
# Next, Generate the MSI Installer script to enable you to install and distribute
# your executable by running the this same setup.py script with
# the command 'python setup.py bdist_msi' which will create
# a directory called /dist where you will see the MSI installer
# script called "contact_Management_python-1.0-amd64.msi"
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/distutils.html 
#
# Note that the executable to double click to run this
# contact management application is "contact_management_python".
# Create a shortcut to this "contact_management_python" executable
# that the installer places in the install path you specified, and/or
# left click on the "contact_management_python" executable and
# select "add to start menu" on Windows.

import sys
import os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('contact_management_python.py', base=base)
]

os.environ['TCL_LIBRARY'] = "C:/Users/chipcoder4972/AppData/Local/Programs/Python/Python36/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Users/chipcoder4972/AppData/Local/Programs/Python/Python36/tcl/tk8.6"

setup(name='cx_Freeze_Script_Tkinter_CM',
      version='1.0',
      description='cx_Freeze Tkinter script for contact_management_python.py',
      executables=executables
      )
