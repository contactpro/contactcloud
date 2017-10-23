######################################################################################
#
# Author: Michael Hughes 
#
# Program: send_gmail_from_oauth2_CM-CLIENT.py 
#
# Version: 1.0
#    
# Date: October 23, 2017 
#
# Description: Sends Gmail that has previously
# acquired oauth2 (JSON FILE) credentials as a
# registered GMAIL API CLIENT Application.
#
# Sends an email message from the user's gmail account.
#
# The Gmail API Client Name is CM-CIENT and this
# will should be modified to match the Gmail API
# CLIENT NAME you register with oauth2 credentials
# on the Google Gmail API web console.
# 
# This, Gmail API CM_CLIENT is the service:
# An oauth2 Authorized Gmail API service instance.
#
# Language: Python 3.6.2 
#
######################################################################################
#
# INTEGRATING THIS CODE INTO A PYTHON 3 tkinter Application: 
#
# If modifying these scopes, delete your previously saved credentials
# created at path .... HOME_DIR.credentials.gmail-python-quickstart.json
#
# re:  SCOPES = 'https://www.googleapis.com/auth/gmail.send'
#
# Important: If integrating this to a Python 3 tkinter App, modify the 
# credential_dir and credential_path in the application code to a folder 
# in APPDATA where you create to store the credentials: The JSON FILE
# called client_secret.json that you downloaded when you registered your
# Gmail API CLIENT with the Google Gmail API web console.
#
# re:  credential_dir and credential_path   (in the code below)
#
# The CLIENT NAME (APPLICATION NAME) below should be modified to match the
# client name that you created when acquiring credentials (and a JSON File Download)
# per the Gmail API CLIENT NAME you register with oauth2 credentials
# on the Google Gmail API web console.
#
# re:  APPLICATION_NAME = 'CM-CLIENT'
#
# Note that to integrate this into a Python 3 tkinter App, we would
# change the print statements in the try-except code to feed a
# status window (a Python tkinter TEXT or ENTRY Widget).
#
#######################################################################################

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

########################################################

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'CM-CLIENT'



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
                                   'client_secret.json')

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



def SendMessage(service, user_id, message):
      """Send an email message.

      Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

      Returns:
        Sent Message.
      """
      try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: ' + str(message['id'] ) )
        return message
      except Exception as ex:
        print("..... An error occurred while executing ...... SendMessage .......")
        print(ex)


def CreateMessage(sender, to, subject, message_text):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEText(message_text)
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def CreateMessageWithAttachment(sender, to, subject, message_text, file_dir, filename):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        file_dir: The directory containing the file to be attached.
        filename: The name of the file to be attached.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEMultipart()
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject

      msg = MIMEText(message_text)
      message.attach(msg)

      path = os.path.join(file_dir, filename)
      content_type, encoding = mimetypes.guess_type(path)

      if content_type is None or encoding is not None:
          content_type = 'application/octet-stream'
          main_type, sub_type = content_type.split('/', 1)
      if main_type == 'text':
          fp = open(path, 'rb')
          msg = MIMEText(fp.read(), _subtype=sub_type)
          fp.close()
      elif main_type == 'image':
          fp = open(path, 'rb')
          msg = MIMEImage(fp.read(), _subtype=sub_type)
          fp.close()
      elif main_type == 'audio':
          fp = open(path, 'rb')
          msg = MIMEAudio(fp.read(), _subtype=sub_type)
          fp.close()
      else:
          fp = open(path, 'rb')
          msg = MIMEBase(main_type, sub_type)
          msg.set_payload(fp.read())
          fp.close()

      msg.add_header('Content-Disposition', 'attachment', filename=filename)
      message.attach(msg)

      return {'raw': base64.urlsafe_b64encode(message.as_string())}



def main():

      try:

            credentials = get_credentials()
            http = credentials.authorize(httplib2.Http())
            service = discovery.build('gmail', 'v1', http=http)


            # Send Gmail Message 

            #SendMessage(service, "me", CreateMessage("send@gmail.com", "receive@gmail.com", "Test Gmail API Automation", "GMAIL SENT FROM APP ..."))
            
            SendMessage(service, "me", CreateMessage(sender@gmail.com", "receiver_email_address", "Test the CM-CLIENT oauth2client Gmail API Implementation", "Testing the CM-CLIENT oauth2client Gmail API Implementation ......"))

      except Exception as e:
            print ("ERROR !! - The Error is ..... " + str(e) )
            raise


if __name__ == '__main__':
    main()




