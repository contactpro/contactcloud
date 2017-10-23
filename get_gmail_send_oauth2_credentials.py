##########################################################################
#
# Author: Michael Hughes
#
# Program: get_gmail_send_oauth2_credentials.py 
#
# Version: 1.0 
#    
# Date: October 23, 2017 
#
# Description:
#
# Creates a Gmail API service object for gmail send scope.
# CLIENT or SYSTEM ADMIN must first register the Application
# in the Gmail API Google Console GUI to create the JSON File
# and then download and rename the JSON File to client_secret.json
# and place that JSON File in the local directory where this
# get_gmail_send_oauth2_credentials.py script is run once each
# time we need to authorize a new GMAIL API CLIENT. This script
# then stores the oauth2 authorization so that future GMAIL API
# client access is automated. 
#
# Running this get_gmail_send_oauth2_credentials.py GETS and STORES
# the JSON File used for Gmail send scope oauth2 credentials (authorization).
#
# Note that CM-CLIENT-NAME-1 is the client name below that you would change
# to correspond to the client name you create when setting up your
# project's oauth2client NAME to acquire credentials.
#
# Important Note: To implement or Integrate this script within a
# Python 3 tkinter App, we would or could acquire the following
# inputs utilizing the tkinter
# OptionsMenu Dropdown, config.ini, and/or  Entry Widget input techniques:
#
# SCOPES = 'https://www.googleapis.com/auth/gmail.send'
# CLIENT_SECRET_FILE = 'client_secret.json'
# APPLICATION_NAME = 'CM-CLIENT-NAME-1'
#
# Note that we would still be required to first register the Application
# in the Gmail API Google Console GUI to create the JSON File
# and then download and rename the JSON File to client_secret.json
# and place that JSON File in the local directory where this
# get_gmail_send_oauth2_credentials.py script is run once each
# time we need to authorize a new GMAIL API CLIENT. This script
# then stores the oauth2 authorization so that future GMAIL API
# client access is automated. 
# 
# Language: Python 3.6.2 
#
########################################################################## 

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

##############################################################################
#
# If modifying these scopes, delete your previously saved credentials
# created at path .... HOME_DIR.credentials.gmail-python-quickstart.json
#
# re:  SCOPES = 'https://www.googleapis.com/auth/gmail.send'
#
# re:  APPLICATION_NAME = 'CM-CLIENT-NAME-1'
#
##############################################################################

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'CM-CLIENT-NAME-1'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object for gmail send scope.

    Running this Creates JSON File used for Gmail send scope.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)


if __name__ == '__main__':
    main()

    
