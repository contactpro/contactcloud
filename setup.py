# -*- coding: utf-8 -*-
# A setup.py script to create an executable of a Python Contact Manager Tkinter App.
# contact_management_python.py is the Contact Management Tkinter application source code.
# This also demonstrates the method for creating a Windows executable that
# does not have an associated console. This setup.py script is also used
# to create the MSI install file.
#
# This setup.py script is typically run with the following commands:
#
# COMMAND to BUILD and create the EXECUTABLE:   python setup.py build
#
# COMMAND to DISTRIBUTE and create the MSI INSTALLER:   python setup.py bdist_msi
#
# PLEASE FOLLOW THESE DIRECTIONS ......
#
# STEP #1:    python setup.py build 
# 
# Run the build process by running this setup.py script with
# the command: 'python setup.py build'
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/script.html 
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application.
#
# STEP #2:
#
# Check the \build directory to verify a successful BUILD was executed
# by looking for the contact_management_python.exe that was created
# in \build\exe.win-amd64-3.6 directory.
#
# Verify the application runs by typing contact_management_python.exe
# or by double clicking "contact_management_python.exe". 
#
# STEP #3:
#
# Resolve any BUILD errors that may appear
# as a POP-UP BOX by googling the solution, typically on stackoverflow. 
#
# Once the contact_management_python.exe runs successfully (with no error box popup),
# then the setup.py script has generated a CLEAN BUILD or a GOOD BUILD,
# by creating the "contact_management_python" executable, which you verified
# by observing that the application runs as expected. 
#
# STEP #4:    python setup.py bdist_msi 
# 
# Next, Generate the MSI Installer script to enable you to install and distribute
# your executable by running the this same setup.py script with
# the command "python setup.py bdist_msi" which will create
# a directory called /dist where you will see the MSI installer
# script called "CM-1.0-amd64.msi"
#
# COMMAND OPTIONS: http://cx-freeze.readthedocs.io/en/latest/distutils.html 
#
# Note that the MSI Installer executable that installs this contact management
# application is named CM-1.0-amd64.msi and is located in the /dist folder
# below where you just ran the setup.py script.
#
# STEP #5:
#
# Copy the MSI installer, CM-1.0-amd64.msi, to a new Folder named something like
# C:/...... /CM_MSI_INSTALLER_SAVE/ and then double click on the CM-1.0-amd64.msi
# installer to verify the install script presents a pop-up window asking you
# which directory you want to install the application in.
#
# IMPORTANT: Modify the /Programs path in the installer window to be at the C-Drive
# level as follows:  C:/CM_APP_AREA/ and then click NEXT to install the application
# and then click FINISH.
#
# This step of modifying the path is very important because the application must
# be installed in a Folder or Directory Path where it has write permission to
# create the application's data files.
#
# STEP #6:
#
# Once the Installer is finished, locate the EXECUTABLE called "contact_management_python.exe"
# and right click on the EXECUATBLE "contact_management_python.exe" and select PIN-TO-START-MENU.
# Then go to your WINDOWS 10 Start Menu and Click on the contact_management Icon to run
# the Contact Management Application.
#
# STEP #7:
#
# Verify that the "contact_management_python" application runs by creating
# a new CONTACT LIST and adding some data and SAVING the data and then VIEW the DATA
# using the buttons on the Contact Management Application. 
#
######################################################################################

import sys
import os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('contact_management_python.py', base=base)
]

print("\n" + "..... BUILD and DIST Executable = contact_management_python.py")
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
print("\n" + "..... PYTHON_INSTALL_DIR = " + str(PYTHON_INSTALL_DIR) )
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
print("\n" + "..... TCL_LIBRARY = " + str(os.environ['TCL_LIBRARY']) )
print("\n" + "..... TK_LIBRARY = " + str(os.environ['TK_LIBRARY']) )
print("\n")

options = {'build_exe': {'include_files':[os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), \
                                          os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),],},}

setup(name='CM',
      version='1.0',
      description='cx_Freeze Tkinter script for contact_management_python.py - v1 - 64Bit',
      options = options,
      executables=executables
      )


