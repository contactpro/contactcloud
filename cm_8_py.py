################################################################
#
# Author: Michael Hughes
#
# Program: contact_management_python.py 
#
# Version: 8.0
#   
# Date: November 1, 2017 
#
# Description: Simple Contact Management Software Program.
# This Contact Management Software Program is implemented
# with very large FONT (Letter Sizes) to improve productivity.
#
# Language: Python 3.6.2 
#
################################################################ 

# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

from __future__ import print_function
import httplib2
import os
import shutil
import platform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email.utils import make_msgid
from email.utils import formatdate
import csv
import sys
import traceback
import threading
import time
import datetime
import random
import configparser
import xlsxwriter
import numpy
import pandas as pd

import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from tkinter.messagebox import *

from configparser import ConfigParser

from openpyxl import workbook

# integration of gmail send scope oauth2 json

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

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

##############################################################################
# 
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
#
SCOPES = "https://mail.google.com"
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

gmail_oauth2_json_file_test_global = None
gmail_oauth2_status_global = None
gmail_oauth2_exceptions_status_global = None
gmail_oauth2_SPECIFIC_EXCEPTION_global = "Specific_OAUTH2_Exception"
gmail_smtp_allow_less_secure_apps_global = None
gmail_smtp_status_global = None
gmail_smtp_exceptions_status_global = None
gmail_smtp_SPECIFIC_EXCEPTION_global = "Specific_SMTP_Exception"
gmail_logged_in_global = None
cm_dict_file_startup_test_global = None
cm_csv_file_startup_test_global = None
cm_notes_file_startup_test_global = None
insert_first_contact_global = False
gmail_mode_global = "gmail_mode_global NOT SET"
fullpath_gmail_oauth2_credentials_global = "PATH NOT SET for client_secret.json"
fullpath_exception_logfile_global = "EXCEPTION LOGFILE PATH NOT SET"
credential_home_dir_global = "PATH NOT SET for credential_home_dir_global"
credential_appdata_dir_global = "PATH NOT SET for credential_appdata_dir_global"
credential_home_path_global = "PATH NOT SET for credential_home_path_global"
credential_appdata_path_global = "PATH NOT SET for credential_appdata_path_global"
client_secret_path_global = "PATH NOT SET for client_secret_path_global"
valid_client_secret_key_format_global = False
mode_select_global = "MODE Not Set"
request_mainscreen_config_update_global = False
textbox_edit_mode_select_global = "TEXTBOX EDIT MODE NOT SET"
listbox_color_value_global = "COLOR CONFIGURATION LISTBOX INITIALIZATION"
listbox_color_moment_global = "LISTBOX COLOR MOMENT INITIALIZATION"
selected_dictionary_loaded_global = {}
selected_dictionary_record_index_global = 1
selected_dictionary_record_index_focus_global = 1
kick_thread_to_update_main_entry_widgets = False
num_of_dictionary_data_records_global = 0
username_global = "USERNAME Path Not Set"
appdata_path_global = "APPDATA Path Not Set"
cm_appdatafiles_path_global = "CM_APPDATAFILES Path Not Set"
fullpath_app_config_ini_global = "APPDATA_CONFIG_INI Path Not Set"
mainscreen_bg_color_val_global = "ivory4"
viewscreen_bg_color_val_global = "ivory4"
selectlist_bg_color_val_global = "ivory4"
newlist_bg_color_val_global = "ivory4"
usermanual_bg_color_val_global = "ivory4"
config_bg_color_val_global = "ivory4"
mainscreen_fg_color_val_global = "ivory4"
viewscreen_fg_color_val_global = "ivory4"
selectlist_fg_color_val_global = "ivory4"
newlist_fg_color_val_global = "ivory4"
usermanual_fg_color_val_global = "ivory4"
config_fg_color_val_global = "ivory4"
app_config_ini_val_global = "app_config.ini"
app_config_request_global = False
fullpath_fn_cm_listbox_file_global = "FULLPATH_FN_CM_LISTBOX_FILE Not Set"
fullpath_fn_dict_filename_global = "FULLPATH_FN_DICT_FILENAME Not Set"
fullpath_cnotes_dict_file_global = "FULLPATH_CNOTES_DICT_FILE Not Set"
fullpath_fn_cm_sw_app_logfile_global = "FULLPATH_FN_CM_SW_APP_LOGFILE Not Set"
export_csv_excel_userprofile_global = "EXPORT CSV TO EXCEL USERPROFILE DIR Not Set"
export_csv_excel_cm_appdata_global = "EXPORT CSV TO EXCEL APPDATA DIR Not Set"
export_to_excel_listbox_select_fn_global = "EXPORT CSV TO EXCEL LISTBOX FILE Not Set"
new_excel_file_created_global = "NEW EXCEL FILE CREATED GLOBAL Not Set"
listbox_file_capture_global = False
cm_listbox_file_global = "No Contact List Selected"
dict_filename_global = "No Contact Dictionary"
cnotes_dict_file_global = "CNOTES_DICT_FILE Not Set"
prepend_cnotes_dict_file_global = "PREPEND_CNOTES_DICT_FILE Not Set"
master_cm_list_name_global = "SELECT or Create NEW Contact List"
textbox_newfile_capture_global = False
cm_textbox_newfile_global = "No New Contact List Created"
first_insert_data_entry = 0


####################################################################################
""" Description: Contact Management Software Program.
    This Contact Management Software Program is implemented
    with very large FONT (Letter Sizes) to improve productivity. """ 
####################################################################################



class App(object):
      """
      This is the App Class. 

      The App Class is defined by the statement:  class App(object): 

      The App Class has the following attributes:

      List App Class Attributes here. 

      """       
      def __init__(self, master):
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_logged_in_global
            global cm_dict_file_startup_test_global
            global cm_csv_file_startup_test_global
            global cm_notes_file_startup_test_global
            global insert_first_contact_global
            global fullpath_gmail_oauth2_credentials_global
            global credential_home_dir_global
            global credential_appdata_dir_global
            global credential_home_path_global
            global credential_appdata_path_global
            global client_secret_path_global
            global valid_client_secret_key_format_global
            global gmail_mode_global
            global mode_select_global
            global request_mainscreen_config_update_global
            global textbox_edit_mode_select_global
            global selected_dictionary_loaded_global
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets
            global num_of_dictionary_data_records_global
            global listbox_file_capture_global
            global cm_listbox_file_global
            global dict_filename_global
            global cnotes_dict_file_global
            global master_cm_list_name_global
            global cm_appdatafiles_path_global
            global listbox_color_value_global
            global listbox_color_moment_global
            global fullpath_app_config_ini_global
            global mainscreen_bg_color_val_global
            global mainscreen_bg_color_val_global
            global viewscreen_bg_color_val_global
            global selectlist_bg_color_val_global
            global newlist_bg_color_val_global
            global usermanual_bg_color_val_global
            global config_bg_color_val_global
            global mainscreen_fg_color_val_global
            global viewscreen_fg_color_val_global
            global selectlist_fg_color_val_global
            global newlist_fg_color_val_global
            global usermanual_fg_color_val_global
            global config_fg_color_val_global
            global app_config_ini_val_global
            global app_config_request_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            global fullpath_cnotes_dict_file_global
            global fullpath_fn_cm_sw_app_logfile_global
            global export_csv_excel_userprofile_global
            global export_csv_excel_cm_appdata_global
            global export_to_excel_listbox_select_fn_global
            global new_excel_file_created_global

            self.master = master

            self.frame = tk.Frame(self.master)

            # Set Messagebox Font
            self.master.option_add('*Dialog.msg.font', 'Helvetica 16')

            self.master.configure(background=str(mainscreen_bg_color_val_global) )
            
            self.session_index = 1

            self.session_review_index = 1

            contactList = []

            # self.this_person = []

            gfn = ''
            gln = ''
            gsa = ''
            gct = ''
            gst = ''
            gzc = ''
            gpn = ''
            gem = ''
            gws = ''
 
            count_inserts = 0 

            this_contacts = {}
            
            large_font = ('Verdana',20)
            minilarge_font = ('Verdana',16)
            medium_font = ('Verdana',12,'bold')
            small_font = ('Verdana',10)
            menubar_font = ('Helvetica', '12')
            
            self.master.title("Contact Management Application Software")

            # Max Screen Size with the Title Bar - BEST Choice 
            self.master.wm_state('zoomed')   
            
            self.mybutton = Button(self.master, text = "SAVE\nContact\nEntry", \
                  width=8,height=4, font=minilarge_font, \
                  background="light sea green", command = self.finished_Data_Entry)
            
            self.mybutton.grid(row=10, column=1, sticky=E)

            self.export_csv_button = Button(self.master, text = "Export to EXCEL", \
                  width=15,height=2, font=('Helvetica', '12'), \
                  background="light sea green", command = self.export_CSV_for_Excel)

            self.export_csv_button.grid(row=1, column=0, sticky=W)

            #############################################################################
            #
            # Implement Options Menu Drop Down to Select Entry Mode or Browse Mode
            #  
            # Use OptionsMenu to set mode_select_global = "Browse Mode" or "Entry Mode"
            #
            #############################################################################
            #
            # OPTION MENU WIDGET for MODE SELECT - selects from OptionMenu and
            # sets MODE SELECT GLOBAL which is utilized to set 
            # MODE SELECT INDICATOR WIDGET value as Entry Mode or Browse Mode
            #
            # Note that default is mode_select_global = "Browse Mode" because
            # if we are switching screens back and forth, we want to maintain
            # workflow speed and the "index_focus_global" dictionary pointer.
            #
            #############################################################################
            #
            List_of_Program_Modes = ["Entry Mode", "Browse Mode"]

            mode_select_global = "Browse Mode"

            self.mode_select_opt_menu_select = StringVar()
            self.mode_select_opt_menu_select.set(str(mode_select_global) )   # initialize OptionMenu for Mode Select
            self.mode_select_optionsmenu_inst = OptionMenu(self.master, self.mode_select_opt_menu_select, \
            *List_of_Program_Modes, command=self.func_set_mode_select_global)
            self.mode_select_optionsmenu_inst.grid(sticky = E, row=1, column=0)
            self.mode_select_optionsmenu_inst.config(borderwidth=5, background="light sea green", font=('Helvetica', 14 ) )

            menu_mode_select = self.mode_select_optionsmenu_inst.nametowidget(self.mode_select_optionsmenu_inst.menuname) 
            menu_mode_select.configure(font=("Helvetica", 18), bg="light sea green")
            

            self.sort_contact_list_button = Button(self.master, text = "SORT Contacts", \
                  width=15,height=2, font=('Helvetica', '12'), \
                  background="light sea green", command = self.sort_Contact_List)

            self.sort_contact_list_button.grid(row=2, column=0, sticky=W)

            self.insert_button = Button(self.master, text = "CONTACT NOTES\nEMAIL   ( Gmail )", \
                  width=30,height=3, font=('Helvetica', '12'), \
                  background="ivory4", command = self.email_Gmail_Feature)
            
            self.insert_button.grid(row=12, column=2, sticky=W)

            self.config_button = Button(self.master, text = "CONFIGURE APP SETTINGS", \
                  width=30,height=3, font=('Helvetica', '12'), \
                  background="ivory4", command = self.config_App_Settings)
            
            self.config_button.grid(row=12, column=2, sticky=E)
            

            self.new_window_button = Button(self.master, text = "SELECT\nContact\nList", \
                  width = 8, height = 4, font=minilarge_font, background="ivory4", \
                  fg = "gray25", command = self.new_window)

            self.new_window_button.grid(row=10, column=1, sticky=W)
  

############################################################################################
         
            scroll_label = ['','','','','','']

            r = 3
            for c in scroll_label:
                  if r > 2 and r < 9:
                       if r == 3:
                             bindto = "forward_fast"
                             self.speedbutton_1 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.forward_fast)
                             self.speedbutton_1.grid(row=r,column=0, sticky=W)
                             #self.speedbutton_1.bind("<Enter>", self.forward_fast)
                             #self.speedbutton_1.bind("<Leave>", self.forward_fast)
                             #self.speedbutton_1.bind("<Button-1>", self.forward_fast)
                       elif r == 4:
                             bindto = "forward_scroll"
                             speedbutton_2 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.forward_scroll)
                             speedbutton_2.grid(row=r,column=0, sticky=W)
                             #speedbutton_2.bind("<Enter>", self.forward_scroll)
                             #speedbutton_2.bind("<Leave>", self.forward_scroll)
                       elif r == 5:
                             bindto = "forward_tick"
                             speedbutton_3 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.forward_tick)
                             speedbutton_3.grid(row=r,column=0, sticky=W)
                             #speedbutton_3.bind("<Enter>", self.forward_tick)
                             #speedbutton_3.bind("<Leave>", self.forward_tick)
                             ############################################################################
                             speedbutton_3_click = Button(self.master, text = "Forward Click", \
                             width=15,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.forward_click)
                             speedbutton_3_click.grid(row=r,column=0, sticky=E)
                             ############################################################################
                       elif r == 6:
                             bindto = "backward_tick"
                             speedbutton_4 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.backward_tick)
                             speedbutton_4.grid(row=r,column=0, sticky=W)
                             #speedbutton_4.bind("<Enter>", self.backward_tick)
                             #speedbutton_4.bind("<Leave>", self.backward_tick)
                             ############################################################################
                             speedbutton_4_click = Button(self.master, text = "Backward Click", \
                             width=15,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.backward_click)
                             speedbutton_4_click.grid(row=r,column=0, sticky=E)
                             ############################################################################
                       elif r == 7:
                             bindto = "backward_scroll"
                             speedbutton_5 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.backward_scroll)
                             speedbutton_5.grid(row=r,column=0, sticky=W)
                             #speedbutton_5.bind("<Enter>", self.backward_scroll)
                             #speedbutton_5.bind("<Leave>", self.backward_scroll)
                       elif r == 8:
                             bindto = "backward_fast"
                             speedbutton_6 = Button(self.master, text = "Test Entry", \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.insert_Data_Entry)
                             speedbutton_6.grid(row=r,column=0, sticky=W)
                             #speedbutton_6.bind("<Enter>", self.backward_fast)
                             #speedbutton_6.bind("<Leave>", self.backward_fast)


                  r = r + 1


######################################################################################

            self.quitbutton = Button(self.master, text = "CLICK HERE\nto EXIT", \
                                   width=30,height=3, font=('Helvetica', '12'), \
                                     background="IndianRed1", command = self.exit_Handler)
            
            self.quitbutton.grid(row=12, column=0, sticky=W)

######################################################################################

            self.user_manual_button = Button(self.master, text = "USERS MANUAL\nand System Administration", \
                  width=30,height=3, font=('Helvetica', '12'), \
                  background="ivory4", command = self.user_manual_View)
            
            self.user_manual_button.grid(row=12, column=1, sticky=W)

###################################################################################### 

            self.app_status_display_select_button = Button(self.master, \
                text = "APP STATUS", width=14, height=1, command = self.select_App_Status_Display)
            
            self.app_status_display_select_button.grid(row=2, column=0, sticky=E)
            self.app_status_display_select_button.config(borderwidth=5, background="light sea green", font=('Helvetica', 14 ) )

######################################################################################

            self.buildlistbutton = Button(self.master, text = "NEW\nContact\nList", \
                                   width=8, height=4, font=minilarge_font, \
                                   background="ivory4", fg = "gray25", command = self.new_list_window)
            
            self.buildlistbutton.grid(row=10, column=0, sticky=E)

###################################################################################### 

            self.view_mode_button = Button(self.master, text = "VIEW\nContact\nList", \
                                   width=8, height=4, font=minilarge_font, \
                                   background="ivory4", fg = "gray25", command = self.view_mode)
            
            self.view_mode_button.grid(row=10, column=0, sticky=W)
 
######################################################################################
           
            self.label_first = "First Name:"
            self.mylabel = Label(self.master, text = self.label_first, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=1, column=1)

            self.label_last = "Last Name:"
            self.mylabel = Label(self.master, text = self.label_last, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=2, column=1)
                       
            self.label_streetadd = "Street Address:"
            self.mylabel = Label(self.master, text = self.label_streetadd, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=3, column=1)

            self.label_citytown = "Town or City:"
            self.mylabel = Label(self.master, text = self.label_citytown, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=4, column=1)

            self.label_state = "State:"
            self.mylabel = Label(self.master, text = self.label_state, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=5, column=1)

            self.label_zipcode = "Zip Code:"
            self.mylabel = Label(self.master, text = self.label_zipcode, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=6, column=1)

            self.label_phonenum = "Phone Number:"
            self.mylabel = Label(self.master, text = self.label_phonenum, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=7, column=1)

            self.label_email = "EMail:"
            self.mylabel = Label(self.master, text = self.label_email, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=8, column=1)

            self.label_website = "Website:"
            self.mylabel = Label(self.master, text = self.label_website, font=large_font)
            self.mylabel.config(height = 1, width=15, anchor = E)
            self.mylabel.config(bg='ivory4', fg='gray25')  
            self.mylabel.grid(row=9, column=1)


###########################################################################################################
            
            self.entry_first = StringVar()
            self.myentry1 = Entry(self.master, textvariable = self.entry_first, font=large_font, width=35)
            self.myentry1.grid(sticky = W, row=1, column=2)
            self.myentry1.config(borderwidth=5, background="light sea green")

            self.entry_last = StringVar()
            self.myentry2 = Entry(self.master, textvariable = self.entry_last, font=large_font, width=35)
            self.myentry2.grid(sticky = W, row=2, column=2)
            self.myentry2.config(borderwidth=5, background="light sea green")

            self.entry_streetadd = StringVar()
            self.myentry3 = Entry(self.master, textvariable = self.entry_streetadd, font=large_font, width=35)
            self.myentry3.grid(sticky = W, row=3, column=2)
            self.myentry3.config(borderwidth=5, background="light sea green")

            self.entry_citytown = StringVar()
            self.myentry4 = Entry(self.master, textvariable = self.entry_citytown, font=large_font, width=35)
            self.myentry4.grid(sticky = W, row=4, column=2)
            self.myentry4.config(borderwidth=5, background="light sea green")

            self.entry_state = StringVar()
            self.myentry5 = Entry(self.master, textvariable = self.entry_state, font=large_font, width=35)
            self.myentry5.grid(sticky = W, row=5, column=2)
            self.myentry5.config(borderwidth=5, background="light sea green")

            self.entry_zipcode = StringVar()
            self.myentry6 = Entry(self.master, textvariable = self.entry_zipcode, font=large_font, width=35)
            self.myentry6.grid(sticky = W, row=6, column=2)
            self.myentry6.config(borderwidth=5, background="light sea green")

            self.entry_phonenum = StringVar()
            self.myentry7 = Entry(self.master, textvariable = self.entry_phonenum, font=large_font, width=35)
            self.myentry7.grid(sticky = W, row=7, column=2)
            self.myentry7.config(borderwidth=5, background="light sea green")

            self.entry_email = StringVar()
            self.myentry8 = Entry(self.master, textvariable = self.entry_email, font=large_font, width=35)
            self.myentry8.grid(sticky = W, row=8, column=2)
            self.myentry8.config(borderwidth=5, background="light sea green")

            self.entry_website = StringVar()
            self.myentry9 = Entry(self.master, textvariable = self.entry_website, font=large_font, width=35)
            self.myentry9.grid(sticky = W, row=9, column=2)
            self.myentry9.config(borderwidth=5, background="light sea green")
  
            self.contact_dict_count_status = StringVar()
            self.myentry10 = Entry(self.master, textvariable = self.contact_dict_count_status, font=large_font, width=18)
            self.myentry10.grid(sticky = W, row=9, column=0)
            self.myentry10.config(borderwidth=5, background="light sea green")
 
            self.entry_buildlist = StringVar()
            self.myentry11 = Entry(self.master, textvariable = self.entry_buildlist, font=large_font, width=35)
            self.myentry11.grid(sticky = W, row=10, column=2)
            self.myentry11.config(borderwidth=5, background="light sea green")

            # Initialize Program with the First Contact List
            self.create_first_contact_list_on_startup()

            ###################################################################
            #
            # ENTER FIRST RECORD of Contact Data to Initialize Databases
            # and provide an example for Users. This First Data Record
            # is required so that other Classes and Methods that use the
            # database will avoid the KeyError Exception when encountering
            # an EMPTY Contact List Dictionary. 
            # 
            ###################################################################
            #
            # Load the current DICTIONARY Contact List File - dict_file_cm_listbox_file_global
            # which is stored in APPDATA at fullpath_fn_dict_filename_global

            self.textFile = open(fullpath_fn_dict_filename_global, 'r')

            # This command takes the file object opened with the open() and reads it
            # into a string which we can now use to count the RECORDS in the Dictionary
            # because upon prograam startup we only want ONE INITIAL RECORD to be
            # in the CONTACT-LIST-ONE Contact List. 
            # 
            self.textString = self.textFile.read()

            # Count the DATA RECORDS in the string by counting the
            # number of "DATA_RECORD_DELIMITER:" patterns 
            self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")
            #
            # ONLY If the number of DATA RECORDS in CONTACT-LIST-ONE is ZERO (less than 1),
            # do we execute:  self.first_Contact_Data_Entry() 
            #
            if self.num_data_records < 1:
                self.first_Contact_Data_Entry()

            ###########################################################################################
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
            # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

            inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

            # NOTE:
            # selected_dictionary_record_index_global = 1
            # selected_dictionary_record_index_focus_global = 1

            kick_thread_to_update_main_entry_widgets = True
                   
            ###########################################################################################
            #  
            #     *****  END OF APP INITIALIZATION  *****
            #
            ###########################################################################################



      ######################################################################################
      #
      # Method to Create the First Contact List so the User begins with an initial
      # Contact List and all the associated Database Files. 
      #
      # This method is called at the end of the init of the App Class (above)
      #
      # Method:  create_first_contact_list_on_startup()
      #     
      ######################################################################################

      def create_first_contact_list_on_startup(self):
          global cm_listbox_file_global
          global dict_filename_global
          global cnotes_dict_file_global
          global prepend_cnotes_dict_file_global
          global master_cm_list_name_global
          global listbox_file_capture_global
          global cm_textbox_newfile_global
          global textbox_newfile_capture_global
          global fullpath_fn_cm_listbox_file_global
          global fullpath_fn_dict_filename_global
          global fullpath_cnotes_dict_file_global
          global fullpath_prepend_cnotes_dict_file_global
          global selected_dictionary_record_index_global

          ###########################################################################
          #
          # This method names the FIRST (or initial) contact list name
          # and sets the cm_textbox_newfile_global
          # and cm_textbox_newfile_global used in THREAD to 
          # set the CONTACT LIST ENTRY BOX in the App Class
          # USING THE GLOBAL VARIABLE cm_listbox_file_global. 
          #
          ###########################################################################
          #
          #  textbox_newfile_capture_global = False
          #
          #  will be set to True to trigger update of the Contact List name
          #  in the MAIN SCREEN by the thread in main. 
          #
          #  cm_textbox_newfile_global = "CONTACT-LIST-ONE" 
          #
          ###########################################################################

          self.entry_first.set(str("") )
          self.entry_first.set(str("") )
          self.entry_last.set(str("") )
          self.entry_streetadd.set(str("") )
          self.entry_citytown.set(str("") )
          self.entry_state.set(str("") )
          self.entry_zipcode.set(str("") )
          self.entry_phonenum.set(str("") )
          self.entry_email.set(str("") )
          self.entry_website.set(str("") )
          self.contact_dict_count_status.set(str("") )

          # initialize the dictionary index global
          selected_dictionary_record_index_global = 0

          cm_textbox_newfile_global = "CONTACT-LIST-ONE"
          master_cm_list_name_global = "CONTACT-LIST-ONE"
          textbox_newfile_capture_global = True

          # Create NEW FILES for the cm_list_CONTACT_LIST_NAME 
          # and dict_file_CONTACT_LIST_NAME and the
          # cnotes_CONTACT_LIST_NAME Globals filenames.
          cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
          dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
          cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

          # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
          # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
          # which gives us the FULL PATH NAME to our contact_management.py data files. 
       
          fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
          fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

          fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

          fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        
       
          # Create the new Contact List File and add Titles 
          with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
                wf_titles.flush()
                wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "," + "\n")


        
          # Create the File for Contact DICTIONARY Filename dict_filename_global
          with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
                new_wdictf.flush()
                new_wdictf.write("\n")


          # Create the File for Contact NOTES DICTIONARY Filename cnotes_dict_file_global
          with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
                new_notes_wdictf.flush()
                new_notes_wdictf.write("\n")


          # write a new logfile to update the logfile items each time a new Contact List is Created
          inst_Write_Main_Logfile_first_contact_list = Write_Main_Logfile()
          inst_Write_Main_Logfile_first_contact_list.write_update_logfile()
        
          return
    
           
            
      ######################################################################################
      #
      # Mode Select Optons Menu StringVar setting ...
      #  
      # if mode_select_global == "Browse Mode":
      # then insert a check for existance of DICTIONARY FILE here ...... if not then messagebox 
      #  
      # Set Contact Textbox StringVar Values from STORED DICTIONARY FILE 
      #    
      # First disable Contact Textbox Entry and clear Contact Textbox 
      #     
      ######################################################################################
      #
      def func_set_mode_select_global(self, mode_select_opt_menu_select):
             global mode_select_global
             global selected_dictionary_record_index_global
             global selected_dictionary_record_index_focus_global
             global kick_thread_to_update_main_entry_widgets

             mode_select_global = str(mode_select_opt_menu_select)
             
             self.entry_first.set(str("") )
             self.entry_first.set(str("") )
             self.entry_last.set(str("") )
             self.entry_streetadd.set(str("") )
             self.entry_citytown.set(str("") )
             self.entry_state.set(str("") )
             self.entry_zipcode.set(str("") )
             self.entry_phonenum.set(str("") )
             self.entry_email.set(str("") )
             self.entry_website.set(str("") )
             self.contact_dict_count_status.set(str("") )

             # Verify there is a DICTIONARY Selected 
             if (str(dict_filename_global) == "No Contact Dictionary") and (mode_select_global == "Browse Mode"):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nBrowse Mode requires that you\nfirst SELECT an existing Contact List\nto Browse Contacts\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

             elif (str(dict_filename_global) == "No Contact Dictionary") and (mode_select_global == "Entry Mode"):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nEntry Mode requires that you\nfirst create a NEW Contact List\nto Enter Contacts\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

             elif (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary"):
                   
                   # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
                   # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

                   inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
                   loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

                   #selected_dictionary_record_index_global = 1
                   #selected_dictionary_record_index_focus_global = 1
                   
                   kick_thread_to_update_main_entry_widgets = True

             elif  (mode_select_global == "Entry Mode") and (str(dict_filename_global) != "No Contact Dictionary"):

                   pass

             else:
                   pass


                  

      ######################################################################################
      # 
      #  METHOD TO CLICK OR SCROLL THROUGH CONTACTS USING  
      # 
      #  selected_dictionary_loaded_global and selected_dictionary_record_index_global
      #  
      #  if mode_select_global == "Browse Mode":  
      #  then insert a check for existance of DICTIONARY FILE here ...... if not then messagebox 
      #  
      #  Set Contact Textbox StringVar Values from STORED DICTIONARY FILE 
      #      
      #  First disable Contact Textbox Entry and clear Contact Textbox 
      #     
      ######################################################################################
      #                   
      def emulate_the_scroll_method(self):
          global kick_thread_to_update_main_entry_widgets
          # Verify there is a DICTIONARY Selected
          if str(dict_filename_global) == "No Contact Dictionary":
              messagebox.showinfo("Contact Manager Guide ...", \
              "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
              return

          elif mode_select_global == "Browse Mode":

              # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
              # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

              inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
              loaded_contact_dict_acquired_SETS_A_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()
                
              kick_thread_to_update_main_entry_widgets = True



      #####################################################################################
      # 
      #   VIEW Users Manual and System Administration Info in TEXTBOX   
      #
      #####################################################################################
      # Method to open new window with TEXTBOX to VIEW Users Manual
      # and System Administration Information.
      def user_manual_View(self):
            global fullpath_fn_cm_sw_app_logfile_global
            self.user_manual_View = tk.Toplevel(self.master)
            self.cm_app = Demo1(self.user_manual_View)
            return


      #####################################################################################
      # 
      #   Gmail Feature Method  
      #
      #####################################################################################
      #
      # Method execute Email (Gmail) functionality.
      # Open new window and add Email (Gmail) functionality.
      # 
      def email_Gmail_Feature(self):
            #global some_global_here
            #
            # Before we launch a new window, be sure we have a DICTIONARY LOADED.
            #
            # Note that OAUTH2 Credentials will have to be acquired from a Google Console
            # to operate the secure GMAIL API. Here are the Instructions:
            #
            # https://developers.google.com/gmail/api/quickstart/python
            #
            # https://console.developers.google.com/flows/enableapi?apiid=gmail
            #
            # Verify there is a DICTIONARY Selected.
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen.\n\n..... Press OK to Continue .....\n")
                  
                  return

            self.email_Gmail_Feature = tk.Toplevel(self.master)
            self.cm_app = Email_Gmail_Class(self.email_Gmail_Feature)
            return


      
      
      #####################################################################################
      # 
      #   SELECT CONTACT LIST from LISTBOX    
      #
      #####################################################################################
      # Method to open new window with LISTBOX of cm_list_ files to select a CONTACT LIST.
      def new_window(self):
             global selected_dictionary_record_index_global
             global selected_dictionary_record_index_focus_global
             self.entry_first.set(str("") )
             self.entry_first.set(str("") )
             self.entry_last.set(str("") )
             self.entry_streetadd.set(str("") )
             self.entry_citytown.set(str("") )
             self.entry_state.set(str("") )
             self.entry_zipcode.set(str("") )
             self.entry_phonenum.set(str("") )
             self.entry_email.set(str("") )
             self.entry_website.set(str("") )
             self.contact_dict_count_status.set(str("") )
             selected_dictionary_record_index_global = 1
             selected_dictionary_record_index_focus_global = 1
             
             self.newWindow = tk.Toplevel(self.master)
             self.cm_app = Demo2(self.newWindow)



      #####################################################################################
      #
      #   APPLICATION STATUS DISPLAY
      #
      ##################################################################################### 
      # 
      def select_App_Status_Display(self):
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_logged_in_global
            global cm_dict_file_startup_test_global
            global cm_csv_file_startup_test_global
            global cm_notes_file_startup_test_global
            global valid_client_secret_key_format_global

            self.select_App_Status_Display = tk.Toplevel(self.master)
            self.cm_app = App_Status_Class(self.select_App_Status_Display)



      #####################################################################################
      #
      #   CONFIGURE APP SETTINGS 
      #
      ##################################################################################### 
      # Method to read app_config.ini file and CONFIGURE APP SETTINGS.
      def config_App_Settings(self):
            global fullpath_app_config_ini_global
            global mainscreen_bg_color_val_global
            global viewscreen_bg_color_val_global

            self.config_App_Settings = tk.Toplevel(self.master)
            self.cm_app = Config_Setting_Class(self.config_App_Settings)



      #######################################################################
      #
      #   CREATE NEW CONTACT LIST FILE and new DICTIONARY FILE from TEXTBOX
      #
      #######################################################################
      # Method to open new window with TEXTBOX to ENTER a CONTACT LIST NAME
      # that is then used to update the GLOBALS :
      # cm_textbox_newfile_global,
      # cm_listbox_file_global,
      # dict_filename_global,
      # and then CREATE the FILES for
      # cm_list_  and  dict_file_
      def new_list_window(self):
            global selected_dictionary_record_index_global
            self.entry_first.set(str("") )
            self.entry_first.set(str("") )
            self.entry_last.set(str("") )
            self.entry_streetadd.set(str("") )
            self.entry_citytown.set(str("") )
            self.entry_state.set(str("") )
            self.entry_zipcode.set(str("") )
            self.entry_phonenum.set(str("") )
            self.entry_email.set(str("") )
            self.entry_website.set(str("") )
            self.contact_dict_count_status.set(str("") )
            selected_dictionary_record_index_global = 0
            
            self.newLISTWindow = tk.Toplevel(self.master)
            self.cm_app = Demo3(self.newLISTWindow)

      ######################################################3333#################
      #
      #   VIEW CONTACTS extracted from CONTACT DICTIONARY FILE in LARGE TEXTBOX
      #
      #######################################################3333################
      # Method to open a new window to VIEW CONTACTS by  
      # extracting them with a read() from the dict_file_
      # into a string variable, and then splitting that
      # string variable by searching for DATA_RECORD_DELIMITER 
      # and KEY_SYNC strings to process data and display the
      # data to a LARGE TEXTBOX. 
      def view_mode(self):
            global dict_filename_global
            global viewscreen_bg_color_val_global
            global selected_dictionary_record_index_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            self.entry_first.set(str("") )
            self.entry_first.set(str("") )
            self.entry_last.set(str("") )
            self.entry_streetadd.set(str("") )
            self.entry_citytown.set(str("") )
            self.entry_state.set(str("") )
            self.entry_zipcode.set(str("") )
            self.entry_phonenum.set(str("") )
            self.entry_email.set(str("") )
            self.entry_website.set(str("") )
            self.contact_dict_count_status.set(str("") )
            selected_dictionary_record_index_global = 0
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
            # WHICH UPDATES and SETS THE selected_dictionary_loaded_global GLOBAL.   

            inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            loaded_contact_dict_acquired = inst_loaded_Process_Dict_File.read_target_dict_file()
            
            self.view_Window = tk.Toplevel(self.master)
            self.cm_app = Demo4(self.view_Window)


      ###################################################
      #
      # SORT AND RE-WRITE DATA FILES 
      #
      ###################################################
      #
      def sort_Contact_List(self):
            global dict_filename_global
            global fullpath_fn_dict_filename_global
            global selected_dictionary_record_index_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            self.entry_first.set(str("") )
            self.entry_first.set(str("") )
            self.entry_last.set(str("") )
            self.entry_streetadd.set(str("") )
            self.entry_citytown.set(str("") )
            self.entry_state.set(str("") )
            self.entry_zipcode.set(str("") )
            self.entry_phonenum.set(str("") )
            self.entry_email.set(str("") )
            self.entry_website.set(str("") )
            self.contact_dict_count_status.set(str("") )
            selected_dictionary_record_index_global = 0
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES 

            inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

            messagebox.showinfo("Contact Manager Guide ...", \
            "ATTENTION: \n\nSTATUS UPDATE:\nYour Contact Data\nhas been SORTED\nby LAST NAME\n..... Press OK to Continue .....")

            return



      def forward_fast(self):
          pass

            
      def forward_scroll(self):
            # (self, event)
            pass
            ## #print("Executing - forward_scroll METHOD")
            #self.report_event(event)

            
      def forward_tick(self):
            # (self, event)
            pass
            ## #print("Executing - forward_tick METHOD")
            #self.report_event(event)  


      #################################################################
      #
      #  Implement Forward Click Button Control
      #  to SCROLL through selected DICTIONARY
      #
      #################################################################
      #
      def forward_click(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global num_of_dictionary_data_records_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            elif mode_select_global == "Browse Mode":
                  test_forward_count = selected_dictionary_record_index_global + 1
                  if test_forward_count <= num_of_dictionary_data_records_global:
                        selected_dictionary_record_index_global +=1
                        selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global
                        self.emulate_the_scroll_method()
                  elif test_forward_count > num_of_dictionary_data_records_global:
                        return
            elif mode_select_global == "Entry Mode":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select BROWSE MODE\nto Scroll the Contact List.\nSee BROWSE MODE\nand ENTRY MODE\nMenu Widget\nat Top of Screen.")
                  return
                  
      #################################################################
      #
      #  Implement Backward Click Button Control
      #  to SCROLL through selected DICTIONARY   
      #
      #################################################################
      #
      def backward_click(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global num_of_dictionary_data_records_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            elif mode_select_global == "Browse Mode":
                  test_backward_count = selected_dictionary_record_index_global - 1
                  if test_backward_count >= 1:
                        selected_dictionary_record_index_global -=1
                        selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global
                        self.emulate_the_scroll_method()
                  elif test_backward_count < 1:
                        return
            elif mode_select_global == "Entry Mode":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select BROWSE MODE\nto Scroll the Contact List.\nSee BROWSE MODE\nand ENTRY MODE\nMenu Widget\nat Top of Screen.")
                  return

            
      def backward_tick(self):
            # (self, event)
            pass
            ## #print("Executing - backward_tick METHOD")
            #self.report_event(event)

            
      def backward_scroll(self):
            # (self, event)
            pass
            ## #print("Executing - backward_scroll METHOD")
            #self.report_event(event)

            
      def backward_fast(self):
            # (self, event)
            pass
            ## #print("Executing - backward_fast METHOD")
            #self.report_event(event)

      #
      # KEEP THESE HERE FOR IMPLEMENTING HOVER SCROLL
      #
      #def report_event(self,event):   
      #      # print ("Event Time: " + str(event.time) + "  EventType: " + str(event.type) + \
      #             "  EventWidgetId: " + str(event.widget) + "  EventKeySymbol: " + str(event.keysym) )

                  

      def exit_Handler(self):
            
            if askyesno('Verify', 'Do you really want to EXIT ?'):
                 self.master.destroy()
                 self.master.quit()
                 sys.exit()
            else:
                 showinfo('No', 'EXIT Cancelled - Continue to Enter Contact Data ...')


      #######################################################################
      #   
      #   INSERT CONTACT DATA with INCREMENTING DATA TAGS 
      #   to each of the CONTACT TEXTBOX ENTRY WIDGETS 
      #
      def insert_Data_Entry(self):
            global first_insert_data_entry
            global dict_filename_global
            global master_cm_list_name_global
            if mode_select_global == "Browse Mode":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select ENTRY MODE\nto Enter Data to Contact List.\nSee ENTRY MODE\nand BROWSE MODE\nMenu Widget\nat Top of Screen.")
                  return
            
            elif str(dict_filename_global) == "No Contact Dictionary":
                   messagebox.showinfo("Contact Manager Guide ...", \
                   "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                   return

            ##############################################################
            #
            # Create Lists to Test Database Random Generator Functions
            #
            ##############################################################
            #
            fn_list = ["Mike", "Dave", "Elliot", "Bill", "Pete", "Tim", "John", "Karl", "Frank", "Jim", "Adam", "Janet",\
                       "Brad", "Mary", "Sally", "Kim", "Janet", "Christian", "Susan", "Laura", "Tricia", "Kelly"]
            ln_list = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III", "JJJ", "KKK", "LLL",\
                       "MMM", "NNN", "OOO", "PPP", "QQQ", "RRR", "SSS", "TTT", "UUU", "VVV", "XXX", "YYY", "ZZZ"]
            sa_list = ["24 Driftwood Ave", "85 Elmer Street", "18 Redman Drive", "56 Holmes Road", "32 Wiley Ave", "94 Intrepid Drive"]
            ct_list = ["Someport", "Middlewaretown", "Portsentry", "Newcinna", "OverKinsell", \
                       "Livingnice", "Harvidian", "Boxbathio", "Rochelleview", "Elcina", "Rocklowland"]
            st_list = ["RI", "MA", "CT", "VA", "FL", "NH", "VT", "ME", "NY", "PA", \
                       "SC", "NC", "TN", "CA", "TX", "NM", "CO", "WY", "MI", "IL", "OH"]
            zc_list = ["02840", "04865", "24523", "54978", "03496", "02910", "04655", "42077", "90210", "90588", "72143", "40211"]
            pn_list = ["000-000-0000"]
            em_list = ["thismail@gmail.com", "thatmail@gmail.com", "yourmail@gmail.com", "theirmail@gmail.com", "othermail@gmail.com"]
            ws_list = ["http://www.google.com", "http://www.linkedin.com", "http://www.monster.com", "http://www.indeed.com"]
             
            ran_fn = random.choice(fn_list)
            ran_ln = random.choice(ln_list)
            ran_sa = random.choice(sa_list)
            ran_ct = random.choice(ct_list)
            ran_st = random.choice(st_list)
            ran_zc = random.choice(zc_list)
            ran_pn = random.choice(pn_list)
            ran_em = random.choice(em_list)
            ran_ws = random.choice(ws_list)
             
            first_insert_data_entry += 1
            data_tag = str(first_insert_data_entry)
            self.entry_first.set(str(ran_fn) + str(data_tag) )
            self.entry_last.set(str(ran_ln) + str(data_tag) )
            self.entry_streetadd.set(str(ran_sa) + str(data_tag) )
            self.entry_citytown.set(str(ran_ct) + str(data_tag) )
            self.entry_state.set(str(ran_st) + str(data_tag) )
            self.entry_zipcode.set(str(ran_zc) + str(data_tag) )
            self.entry_phonenum.set(str(ran_pn) + str(data_tag) )
            self.entry_email.set(str(ran_em) + str(data_tag) )
            self.entry_website.set(str(ran_ws) + str(data_tag) )
            return 
            


      ####################################################################### 
      #    
      #   EXPORT CSV DATA for EXCEL SPREADHSEET and EXCEL WORKBOOKS. 
      #
      def export_CSV_for_Excel(self):
            global username_global
            global appdata_path_global
            global cm_appdatafiles_path_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            global cm_listbox_file_global
            global dict_filename_global
            global master_cm_list_name_global
            global export_csv_excel_userprofile_global
            global export_csv_excel_cm_appdata_global
            global export_to_excel_listbox_select_fn_global
            global new_excel_file_created_global
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return

            # Open Window for Export to Excel LISTBOX Selection - DEMO5 
            self.excel_export_select_Window = tk.Toplevel(self.master)
            self.cm_app = Demo5(self.excel_export_select_Window)




      ###################################################################
      #
      # ENTER FIRST RECORD of Contact Data to Initialize Databases
      # and provide an example for Users. This First Data Record
      # is required so that other Classes and Methods that use the
      # database will avoid the KeyError Exception when encountering
      # an EMPTY Contact List Dictionary. 
      # 
      ###################################################################
      #
      def first_Contact_Data_Entry(self):
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global

            # write data record to object/class/method 

            # write data records to cm_list_file
            # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global

            with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                  for x in range(0, 10):
                        if x == 0: wf.flush()
                        #------------------------------------------------------------------------
                        if x == 1: wf.write("First Name" + ",")
                        elif x == 2: wf.write("Last Name" + ",")
                        elif x == 3: wf.write("Street Address" + ",")
                        elif x == 4: wf.write("City or Town" + ",")
                        elif x == 5: wf.write("State" + ",")
                        elif x == 6: wf.write("Zip Code" + ",")
                        elif x == 7: wf.write("Phone Number" + ",")
                        elif x == 8: wf.write("Email Address" + ",")
                        elif x == 9: wf.write("Website" + "," + "\n")
                        else: pass
            
            this_person = Person("First Name", "Last Name", "Street Address", \
                        "City or Town", "State", "Zip Code", "Phone Number", \
                        "Email Address", "Website")

            gfn = this_person.get_Firstname()
            gln = this_person.get_Lastname()
            gsa = this_person.get_Streetadd()
            gct = this_person.get_Citytown()
            gst = this_person.get_State()
            gzc = this_person.get_Zipcode()
            gpn = this_person.get_Phonenum()
            gem = this_person.get_Email()
            gws = this_person.get_Website()

            # Create DICTIONARY to store contact data
            contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                            "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                            "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }

            # Store_Contact_Dict in Store_Contact_Dict Class 
            contact_dict_instance = Store_Contact_Dict(this_contact_dict = contact_dict)
            contact_dict_instance.set_contact_dict(new_this_contact_dict = contact_dict)
            get_contact_dict_call = contact_dict_instance.get_contact_dict()


            # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
            # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
            with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                  for x in range(0, 10):
                        if x == 0:
                              wdictf.flush()
                              wdictf.write("DATA_RECORD_DELIMITER:")
                        elif x == 1: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["First_Name_KEY"] ) )
                        elif x == 2: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Last_Name_KEY"] ) )
                        elif x == 3: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Street_Address_KEY"] ) )
                        elif x == 4: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["City_Town_KEY"] ) )
                        elif x == 5: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["State_KEY"] ) )
                        elif x == 6: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Zip_Code_KEY"] ) )
                        elif x == 7: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Phone_Number_KEY"] ) )
                        elif x == 8: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["EMail_KEY"] ) )
                        elif x == 9: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Website_KEY"] ) )
                        else: pass

            self.session_index += 1

            # Now delete the ENTRY Text Fields to prepare for next ENTRY

            self.entry_first.set('')
            self.entry_last.set('')
            self.entry_streetadd.set('')
            self.entry_citytown.set('') 
            self.entry_state.set('')
            self.entry_zipcode.set('') 
            self.entry_phonenum.set('')
            self.entry_email.set('')
            self.entry_website.set('')

                  
            
      #################################################
      #
      # ENTER Contact Data .....  
      # 
      #################################################
      #
      def finished_Data_Entry(self):
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            
            if mode_select_global == "Browse Mode":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease Select ENTRY MODE\nto Enter Data to Contact List.\nSee ENTRY MODE\nand BROWSE MODE\nMenu Widget\nat Top of Screen.")
                  return

            elif str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
  
            elif (str(self.entry_first.get() ) == "" and str(self.entry_last.get() ) == ""):
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nPlease .... FIRST and LAST NAME\nare REQUIRED or MANDATORY\nEntries to the Contact List.\nPlease Type in\nFIRST and LAST NAME.")
                  return
            
            # write data record to object/class/method 

            # write data records to cm_list_file
            # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global

            with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                  for x in range(0, 10):
                        if x == 0: wf.flush()
                        #------------------------------------------------------------------------
                        if x == 1: wf.write(self.entry_first.get() + ",")
                        elif x == 2: wf.write(self.entry_last.get() + ",")
                        elif x == 3: wf.write(self.entry_streetadd.get() + ",")
                        elif x == 4: wf.write(self.entry_citytown.get() + ",")
                        elif x == 5: wf.write(self.entry_state.get() + ",")
                        elif x == 6: wf.write(self.entry_zipcode.get() + ",")
                        elif x == 7: wf.write(self.entry_phonenum.get() + ",")
                        elif x == 8: wf.write(self.entry_email.get() + ",")
                        elif x == 9: wf.write(self.entry_website.get() + "," + "\n")
                        else: pass
            
            
            this_person = Person(self.entry_first.get(), self.entry_last.get(), self.entry_streetadd.get(), \
                        self.entry_citytown.get(), self.entry_state.get(), self.entry_zipcode.get(), self.entry_phonenum.get(), \
                        self.entry_email.get(), self.entry_website.get())

         
            gfn = this_person.get_Firstname()
            gln = this_person.get_Lastname()
            gsa = this_person.get_Streetadd()
            gct = this_person.get_Citytown()
            gst = this_person.get_State()
            gzc = this_person.get_Zipcode()
            gpn = this_person.get_Phonenum()
            gem = this_person.get_Email()
            gws = this_person.get_Website()

            # Create DICTIONARY to store contact data
            contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                            "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                            "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }

            # Store_Contact_Dict in Store_Contact_Dict Class 
            contact_dict_instance = Store_Contact_Dict(this_contact_dict = contact_dict)
            contact_dict_instance.set_contact_dict(new_this_contact_dict = contact_dict)
            get_contact_dict_call = contact_dict_instance.get_contact_dict()     


            # Write contact data dictionary to dict_filename file from class method get_contact_dict_call
            # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
            with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                  for x in range(0, 10):
                        if x == 0:
                              wdictf.flush()
                              wdictf.write("DATA_RECORD_DELIMITER:")
                        elif x == 1: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["First_Name_KEY"] ) )
                        elif x == 2: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Last_Name_KEY"] ) )
                        elif x == 3: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Street_Address_KEY"] ) )
                        elif x == 4: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["City_Town_KEY"] ) )
                        elif x == 5: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["State_KEY"] ) )
                        elif x == 6: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Zip_Code_KEY"] ) )
                        elif x == 7: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Phone_Number_KEY"] ) )
                        elif x == 8: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["EMail_KEY"] ) )
                        elif x == 9: wdictf.write("KEY_SYNC:" + str(get_contact_dict_call["Website_KEY"] ) )
                        else: pass
                                       

            self.session_index += 1

 
            # Now delete the ENTRY Text Fields to prepare for next ENTRY

            self.entry_first.set('')
            self.entry_last.set('')
            self.entry_streetadd.set('')
            self.entry_citytown.set('') 
            self.entry_state.set('')
            self.entry_zipcode.set('') 
            self.entry_phonenum.set('')
            self.entry_email.set('')
            self.entry_website.set('')



class Email_Gmail_Class(object):
      def __init__(self, master, **kw):
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            global gmail_smtp_allow_less_secure_apps_global
            global gmail_smtp_status_global
            global gmail_smtp_exceptions_status_global
            global gmail_smtp_SPECIFIC_EXCEPTION_global
            global gmail_mode_global
            global credential_home_dir_global
            global credential_appdata_dir_global
            global credential_home_path_global
            global credential_appdata_path_global
            global client_secret_path_global
            global textbox_edit_mode_select_global
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global
            global kick_thread_to_update_main_entry_widgets
            global fullpath_prepend_cnotes_dict_file_global
            global prepend_cnotes_dict_file_global
            global fullpath_cnotes_dict_file_global
            self.master = master
            self.frame = tk.Frame(self.master)

            self.master.grid_rowconfigure(0, weight=1)
            self.master.grid_columnconfigure(0, weight=1)

            self.email_title = "INITIALIZE EMAIL TITLE"
            self.email_content = "INITIALIZE EMAIL CONTENT"
            self.source_email_address = "INITIALIZE SOURCE EMAIL ADDRESS"
            self.source_email_password = "INITIALIZE SOURCE EMAIL PASSWORD"
            self.destination_1_email_address = "INITIALIZE DESTINATION EMAIL ADDRESS"

            #######################################################################################
            #
            # Create variables associated with the Email Attachment:
            #
            # We will get a LIST of OBJECTS for the Email Attachment from the Dialog Method:
            #
            #      self.dialog_to_get_file_attachment()    which has a 
            #
            # return_object_list = [data, file_full_path, just_the_file_name]
            #
            # and then we Extract objects from the self.dialog_to_get_file_attachment() method
            #
            # return list as follows: 
            #
            # self.file_email_attachment_BYTES_TYPE_OBJECT = self.dialog_to_get_file_attachment()[0]
            #
            # self.file_email_attachment_FULL_PATH = self.dialog_to_get_file_attachment()[1]
            #
            # self.file_email_attachment_FILE_NAME = self.dialog_to_get_file_attachment()[2]
            #
            # self.file_email_attachment_FILE_TYPE = self.dialog_to_get_file_attachment()[3]
            #
            # Note: This Email Attachment self.dialog_to_get_file_attachment() Method is
            #
            # initiated or triggered by pressing the EMAIL ATTACHMENTS tk Button, which will
            #
            # run the self.dialog_to_get_file_attachment() METHOD and generate the
            #
            # EMAIL ATTACHMENT FILE OBJECT LIST with the help of Dialog Windows user selections.
            #
            # CREATE the OBJECTS for the EMAIL Attachment:

            self.EMAIL_MESSAGE = "EMAIL_MESSAGE_VALUE_NOT_YET_SET"

            self.EMAIL_base64_urlsafe_b64encode_message = "EMAIL_base64_urlsafe_b64encode_message_VALUE_NOT_SET"

            self.file_email_attachment_BYTES_TYPE_OBJECT = b"INITIALIZE_THIS_AS_A_BYTES_TYPE_OBJECT"

            self.file_email_attachment_FULL_PATH = "file_email_attachment_FULL_PATH_NOT_YET_SET"

            self.file_email_attachment_FILE_NAME = "file_email_attachment_FILE_NAME_NOT_YET_SET"

            self.file_email_attachment_FILE_TYPE = "self.file_email_attachment_FILE_TYPE_NOT_YET_SET"

            self.file_email_attachment_CONTENT_TYPE = "self.file_email_attachment_CONTENT_TYPE_NOT_YET_SET"            

            self.file_email_attachment_MAIN_TYPE = "self.file_email_attachment_MAIN_TYPE_NOT_YET_SET"

            self.file_email_attachment_SUB_TYPE = "self.file_email_attachment_SUB_TYPE_NOT_YET_SET"

            self.file_email_attachment_ENCODING = "self.file_email_attachment_ENCODING_NOT_YET_SET"

            self.EMAIL_ATTACHMENT_OPTION_FLAG = False
            
            #
            # 
            #######################################################################################
            
            huge_font = ('Verdana',32)
            large_font = ('Verdana',20)
            minilarge_font = ('Verdana',16)
            medium_font = ('Verdana',12,'bold')
            small_font = ('Verdana',10)
            menubar_font = ('Helvetica', '12')

            # Max Screen Size with the Title Bar - BEST Choice 
            self.master.wm_state('zoomed')

            # Another way to set screen size (other than BEST Choice above
            # self.master.geometry("900x550") 

            self.master.configure(background="black")

            self.master.title("Contact Management Application Software - Email and Contact Notes")

            ################################################################################################
            #  
            # Add Drop Down Menu for Textbox Edit Modes (to create framework for Textbox Edit events) 
            #    
            ################################################################################################

            List_of_Textbox_Edit_Modes = ["EDIT MENU", "CUT Selected Text - (CNTL-X)", \
                                          "COPY Selected Text - (CNTL-C)", "PASTE to Cursor - (CNTL-V)", \
                                          "CLEAR Email or NOTES Content"]

            textbox_edit_mode_select_global = "EDIT MENU"

            self.tb_mode_select_opt_menu_select = StringVar()
            self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )   # initialize OptionMenu 
            self.tb_mode_select_optionsmenu_inst = OptionMenu(self.master, self.tb_mode_select_opt_menu_select, \
            *List_of_Textbox_Edit_Modes, command=self.func_set_textbox_edit_mode_select_global)
            self.tb_mode_select_optionsmenu_inst.grid(sticky = NW, row=0, column=1)
            self.tb_mode_select_optionsmenu_inst.config(borderwidth=10, \
                  background="light sea green", font=('Helvetica', 14) , height = 2)

            tb_menu_mode_select = self.tb_mode_select_optionsmenu_inst.nametowidget(self.tb_mode_select_optionsmenu_inst.menuname) 
            tb_menu_mode_select.configure(font=("Helvetica", 18), bg="light sea green")

            ################################################################################################ 

            self.select_file_button = Button(self.master, text = "SEND EMAIL", \
                  width=16, height=2, font=('Helvetica', '24'), background="light sea green", borderwidth=10)

            self.select_file_button.grid(row=0, column=0, sticky = NW)
            self.select_file_button.bind("<Button-1>", self.get_decision_Textbox_File)


            #self.quitButton = Button(self.master, text = 'Return to Main Screen', width = 20, height = 2, \
            #      font=('Helvetica', '16'), background="goldenrod", borderwidth=5, command = self.close_windows)

            #self.quitButton.grid(row=0, column=1, sticky = NE)

            ################################################################################################
            #
            # Add tk Button with command for method:  email_attachment_option_method() 
            #
            # to select an Email Attachment.  
            #
            ################################################################################################

            
            ################################################################################################
            #
            # Implement Options Menu Drop Down to Select OAUTH2_Gmail_Mode or SMTP_Gmail_Mode
            #  
            # Use OptionsMenu to set gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
            #
            ################################################################################################
            #
            # OPTION MENU WIDGET selects from OptionMenu and
            # sets gmail_mode_global which control email methods:
            # gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
            #
            # Note that default is gmail_mode_global = "SMTP_Gmail_Mode" because
            # it is easier for the user at this stage of development.  
            #
            ################################################################################################


            List_of_Email_Modes = ["OAUTH2_Gmail_Mode", "SMTP_Gmail_Mode"]

            gmail_mode_global = "SMTP_Gmail_Mode"

            self.email_mode_select_opt_menu_select = StringVar()
            self.email_mode_select_opt_menu_select.set(str(gmail_mode_global) )   # initialize OptionMenu 
            self.email_mode_select_optionsmenu_inst = OptionMenu(self.master, self.email_mode_select_opt_menu_select, \
                *List_of_Email_Modes, command=self.func_set_email_mode_select_global)
            self.email_mode_select_optionsmenu_inst.grid(row=0, column=1, sticky = NE)
            self.email_mode_select_optionsmenu_inst.config(borderwidth=5, background="light sea green", font=('Helvetica', 14 ), height = 2)

            email_menu_mode_select = self.email_mode_select_optionsmenu_inst.nametowidget(self.email_mode_select_optionsmenu_inst.menuname) 
            email_menu_mode_select.configure(font=("Helvetica", 18), bg="light sea green")

            # Email Attachments Button

            self.select_attachment_button = Button(self.master, text = "ATTACH TO EMAIL", \
                  width=16, height=2, font=('Helvetica', '14'), background="light sea green", borderwidth=10)

            self.select_attachment_button.grid(row=0, column=1, sticky = N)
            self.select_attachment_button.bind("<Button-1>", self.email_attachment_option_method)
            

            self.load_next_contact_Button = Button(self.master, text = "LOAD NEXT CONTACT  >>>>>>>", width = 43, height = 1, \
                  font=('Helvetica', 12, "bold"), background="light sea green", borderwidth=5, command = self.load_next_contact)

            self.load_next_contact_Button.grid(row=2, column=1, sticky = E)

            self.load_previous_contact_Button = Button(self.master, text = "<<<<<<<  LOAD PREVIOUS CONTACT", width = 43, height = 1, \
                  font=('Helvetica', 12, "bold"), background="light sea green", borderwidth=5, command = self.load_previous_contact)

            self.load_previous_contact_Button.grid(row=3, column=1, sticky = E)

            ################################################################################### 

            # INSERT LABEL FOR SOURCE EMAIL ADDRESS 
            self.label_source_email_address = "Your Gmail Address:"
            self.mylabel_seadr = Label(self.master, text = self.label_source_email_address, font=minilarge_font)
            self.mylabel_seadr.config(height = 1, width=25, anchor = E)
            self.mylabel_seadr.config(bg='ivory4', fg='gray25')  
            self.mylabel_seadr.grid(row=1, column=0, sticky = NE)

            # INSERT LABEL FOR SOURCE EMAIL PASSWORD 
            self.label_source_email_password = "Your Gmail Password:"
            self.mylabel_sepwd = Label(self.master, text = self.label_source_email_password, font=minilarge_font)
            self.mylabel_sepwd.config(height = 1, width=25, anchor = E)
            self.mylabel_sepwd.config(bg='ivory4', fg='gray25')  
            self.mylabel_sepwd.grid(row=2, column=0, sticky = NW)

            # INSERT LABEL FOR DESTINATION 1 EMAIL ADDRESS 
            self.label_destination_1_email_address = "To:"
            self.mylabel_dest_1_adr = Label(self.master, text = self.label_destination_1_email_address, font=minilarge_font)
            self.mylabel_dest_1_adr.config(height = 1, width=25, anchor = E)
            self.mylabel_dest_1_adr.config(bg='ivory4', fg='gray25')  
            self.mylabel_dest_1_adr.grid(row=3, column=0, sticky = NW)

            # INSERT LABEL FOR DESTINATION CC EMAIL ADDRESS 
            self.label_destination_cc_email_address = "Cc:"
            self.mylabel_dest_cc_adr = Label(self.master, text = self.label_destination_cc_email_address, font=minilarge_font)
            self.mylabel_dest_cc_adr.config(height = 1, width=25, anchor = E)
            self.mylabel_dest_cc_adr.config(bg='ivory4', fg='gray25')  
            self.mylabel_dest_cc_adr.grid(row=4, column=0, sticky = NW)

            # INSERT LABEL FOR EMAIL TITLE  
            self.label_email_title = "Subject:"
            self.mylabel_email_title = Label(self.master, text = self.label_email_title, font=minilarge_font)
            self.mylabel_email_title.config(height = 1, width=25, anchor = E)
            self.mylabel_email_title.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_title.grid(row=5, column=0, sticky = NW)

            # INSERT LABEL FOR EMAIL CONTENT 
            self.label_email_content = "Contact Notes / Email:"
            self.mylabel_email_content = Label(self.master, text = self.label_email_content, font=minilarge_font)
            self.mylabel_email_content.config(height = 1, width=25, anchor = E)
            self.mylabel_email_content.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_content.grid(row=6, column=0, sticky = NW)

            # INSERT BUTTONS TO SAVE AND RETRIEVE CONTACT NOTES

            self.notesButton = Button(self.master, text = "SAVE CONTACT NOTES", width = 25, height = 3, \
                  font=('Verdana',14), borderwidth=10, background="turquoise4", command = self.save_contact_notes)

            self.notesButton.grid(row=6, column=0, sticky = W)

            self.retrieve_notes_Button = Button(self.master, text = "RETRIEVE CONTACT NOTES", width = 25, height = 3, \
                  font=('Verdana',14), borderwidth=10, background="turquoise4", command = self.retrieve_contact_notes)

            self.retrieve_notes_Button.grid(row=6, column=0, sticky = SW)

            # INSERT LABEL FOR EMAIL STATUS MESSAGES ....
            self.label_email_status = "Contact / Email Status:"
            self.mylabel_email_status = Label(self.master, text = self.label_email_status, font=minilarge_font)
            self.mylabel_email_status.config(height = 1, width=25, anchor = SE)
            self.mylabel_email_status.config(bg='ivory4', fg='gray25')  
            self.mylabel_email_status.grid(row=7, column=0, sticky = NW)

            ############################################################################ 

            self.last_widget_name_clicked = "INITIALIZE LAST WIDGET NAME CLICKED"
            
            # INSERT ENTRY WIDGET FOR SOURCE EMAIL ADDRESS 
            self.entry_SOURCE_EMAIL_ADDRESS = StringVar()
            self.source_email_address_entry = Entry(self.master, \
                                                    textvariable = self.entry_SOURCE_EMAIL_ADDRESS, font = minilarge_font, width = 40)
            self.source_email_address_entry.grid(sticky = W, row=1, column=1)
            self.source_email_address_entry.config(borderwidth=5, background="light sea green")
            self.source_email_address_entry.bind("<Button-1>",lambda event: self.src_addr_widget_function(event, "self.source_email_address_entry") )

            # INSERT ENTRY WIDGET FOR CONTACT NAME LOADED BY DICTIONARY POINTER 
            self.entry_LOADED_CONTACT_NAME = StringVar()
            self.loaded_contact_name_entry = Entry(self.master, \
                  textvariable = self.entry_LOADED_CONTACT_NAME, font = minilarge_font, width = 33)
            self.loaded_contact_name_entry.grid(sticky = E, row=1, column=1)
            self.loaded_contact_name_entry.config(borderwidth=5, background="light sea green")
            self.loaded_contact_name_entry.bind("<Button-1>",lambda event: self.clistname_widget_function(event, "self.loaded_contact_name_entry") )

            # INSERT ENTRY WIDGET FOR SOURCE EMAIL PASSWORD 
            self.entry_SOURCE_EMAIL_PASSWORD = StringVar()
            self.source_email_password_entry = Entry(self.master, \
                  textvariable = self.entry_SOURCE_EMAIL_PASSWORD, font = minilarge_font, width = 40)
            self.source_email_password_entry.grid(sticky = W, row=2, column=1)
            self.source_email_password_entry.config(borderwidth=5, background="light sea green", show="*")
            self.source_email_password_entry.bind("<Button-1>",lambda event: self.pwd_widget_function(event, "self.source_email_password_entry") )

            # INSERT ENTRY WIDGET FOR DESTINATION 1 EMAIL ADDRESS 
            self.entry_DEST_1_EMAIL_ADDRESS = StringVar()
            self.destination_1_email_address_entry = Entry(self.master, \
                  textvariable = self.entry_DEST_1_EMAIL_ADDRESS, font = minilarge_font, width = 40)
            self.destination_1_email_address_entry.grid(sticky = NW, row=3, column=1)
            self.destination_1_email_address_entry.config(borderwidth=5, background="light sea green")
            self.destination_1_email_address_entry.bind("<Button-1>",lambda event: self.to_widget_function(event, "self.destination_1_email_address_entry") )

            # INSERT ENTRY WIDGET FOR DESTINATION CC EMAIL ADDRESS 
            self.entry_DEST_CC_EMAIL_ADDRESS = StringVar()
            self.destination_cc_email_address_entry = Entry(self.master, \
                  textvariable = self.entry_DEST_CC_EMAIL_ADDRESS, font = minilarge_font, width = 74)
            self.destination_cc_email_address_entry.grid(sticky = NW, row=4, column=1)
            self.destination_cc_email_address_entry.config(borderwidth=5, background="light sea green")
            self.destination_cc_email_address_entry.bind("<Button-1>",lambda event: self.cc_widget_function(event, "self.destination_cc_email_address_entry") )

            # INSERT ENTRY WIDGET FOR EMAIL TITLE 
            self.entry_EMAIL_TITLE = StringVar()
            self.email_title_entry = Entry(self.master, \
                  textvariable = self.entry_EMAIL_TITLE, font = minilarge_font, width = 74)
            self.email_title_entry.grid(sticky = W, row=5, column=1)
            self.email_title_entry.config(borderwidth=5, background="light sea green")
            self.email_title_entry.bind("<Button-1>",lambda event: self.title_widget_function(event, "self.email_title_entry") )

            # INSERT TEXTBOX WIDGET FOR EMAIL CONTENT  
            self.EMAIL_Textbox = Text(self.master, height=15, width=25, font = minilarge_font)
            self.EMAIL_Textbox.grid(row=6, column=1, sticky="nsew")
            self.EMAIL_Textbox.config(borderwidth=5, background="light sea green", wrap=WORD )
            self.EMAIL_Textbox.bind("<Button-1>",lambda event: self.content_widget_function(event, "self.EMAIL_Textbox") )
            self.master.grid_rowconfigure(0, weight=1)
            self.master.grid_columnconfigure(0, weight=1)


            # INSERT ENTRY WIDGET FOR EMAIL STATUS MESSAGES .... 
            self.entry_EMAIL_STATUS = StringVar()
            self.email_status_entry = Entry(self.master, textvariable = self.entry_EMAIL_STATUS, font = ('Verdana',18), width = 64)
            self.email_status_entry.grid(sticky = W, row=7, column=1)
            self.email_status_entry.config(borderwidth=5, bg="ivory4", fg="gray4")
            self.email_status_entry.bind("<Button-1>",lambda event: self.status_widget_function(event, "self.email_status_entry") )

            # PLACE THESE TWO LINES TO SORT AND RE-WRITE DICTIONARY DATA FILES
            # WHICH UPDATES and SETS THE selected_dictionary_loaded_global GLOBAL. 

            inst_email_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            loaded_email_contact_dict_acquired = inst_email_loaded_Process_Dict_File.read_target_dict_file()

            selected_dictionary_record_index_global = 0

            selected_dictionary_record_index_global = selected_dictionary_record_index_focus_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "Contact: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            selected_dictionary_counter_status_display = "Contact # " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )

            if gmail_mode_global == "OAUTH2_Gmail_Mode":

                status_message_info = "Note: Your Gmail Address & Password NOT required in OAUTH2_Gmail_Mode."

                source_address_info = "Your Gmail NOT required - OAUTH2_Gmail_Mode"

                source_password_info = "Your Passward NOT required - OAUTH2_Gmail_Mode"
                 
                self.entry_EMAIL_STATUS.set(str(status_message_info) )
                self.entry_SOURCE_EMAIL_ADDRESS.set(str(source_address_info) )
                self.entry_SOURCE_EMAIL_PASSWORD.set(str(source_password_info) )

            elif gmail_mode_global == "SMTP_Gmail_Mode":

                status_message_info = "Gmail Address/Password REQUIRED and Set ALLOW LESS SECURE APPS (ON)"

                self.entry_EMAIL_STATUS.set(str(status_message_info) )
                self.entry_SOURCE_EMAIL_ADDRESS.set("")
                self.entry_SOURCE_EMAIL_PASSWORD.set("")

            else:
                pass



            
      ######################################################################################
      #
      # Email Mode Select Optons Menu StringVar setting ...
      #  
      # if gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
      # 
      # then choose the corresponding messagebox to display to the operator.
      #
      # Default setting is gmail_mode_global = "SMTP_Gmail_Mode"
      #      
      ######################################################################################
      #
      def func_set_email_mode_select_global(self, email_mode_select_opt_menu_select):
             global gmail_mode_global

             gmail_mode_global = str(email_mode_select_opt_menu_select)

             if gmail_mode_global == "OAUTH2_Gmail_Mode":

                 status_message_info = "Note: Your Gmail Address & Password NOT required in OAUTH2_Gmail_Mode."

                 source_address_info = "Your Gmail NOT required - OAUTH2_Gmail_Mode"

                 source_password_info = "Your Passward NOT required - OAUTH2_Gmail_Mode"
                 
                 self.entry_EMAIL_STATUS.set(str(status_message_info) )
                 self.entry_SOURCE_EMAIL_ADDRESS.set(str(source_address_info) )
                 self.entry_SOURCE_EMAIL_PASSWORD.set(str(source_password_info) )

             elif gmail_mode_global == "SMTP_Gmail_Mode":

                 status_message_info = "Gmail Address/Password REQUIRED and Set ALLOW LESS SECURE APPS (ON)"

                 self.entry_EMAIL_STATUS.set(str(status_message_info) )
                 self.entry_SOURCE_EMAIL_ADDRESS.set("")
                 self.entry_SOURCE_EMAIL_PASSWORD.set("")

             else:
                 pass

  
   

      def save_contact_notes(self):
            global fullpath_prepend_cnotes_dict_file_global
            global prepend_cnotes_dict_file_global
            global fullpath_cnotes_dict_file_global

            # GET the Contact Notes from the Text Widget
            # and add a contact info section at the end
            # by building a new string called: str(build_a_string) 

            contact_notes_get = ""
            contact_notes_get = self.EMAIL_Textbox.get("1.0",END)
            two_line_space = "\n\n"
            one_line_space = "\n"
            contact_notes_date_time_label = "CONTACT NOTES DATE - TIME - "
            # Create a Time Stamp
            temp_time_string = str(datetime.datetime.now() )
            contact_notes_info_label = "CONTACT NOTES INFORMATION:"
            fn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )
            contact_notes_line = str("_____________________________________________________________")
            contact_notes_info_line1 = str(fn_info) + " " + str(ln_info) + "\n"
            contact_notes_info_line2 = str(sa_info) + ", " + str(ct_info) + ", " + str(st_info) + ", " + str(zc_info) + "\n"
            contact_notes_info_line3 = "Phone: " + str(pn_info) + "\n"
            contact_notes_info_line4 = "Email: " + str(em_info) + "\n"
            contact_notes_info_line5 = "Website: " + str(ws_info) + "\n"

            build_a_string = []
            
            build_a_string.append(str(contact_notes_line) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_date_time_label) )
            build_a_string.append(str(temp_time_string) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_info_label) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_info_line1) )
            build_a_string.append(str(contact_notes_info_line2) )
            build_a_string.append(str(contact_notes_info_line3) )
            build_a_string.append(str(contact_notes_info_line4) )
            build_a_string.append(str(contact_notes_info_line5) )
            build_a_string.append(str(contact_notes_line) )
            build_a_string.append(str(two_line_space) )
            build_a_string.append(str(contact_notes_get) )
            build_a_string.append(str(two_line_space) )

            final_built_string = ""
            final_built_string = ''.join(build_a_string)

            #print the string to see .......
            #print("\n" + "STRING BUILT = " + "\n" )
            #print(str(final_built_string) )

            ################################################################################## 

            # Eventually, we want to change Website to LAST FOUR OF SOCIAL SECURITY Number
            # to implement this CONTACT_ID_KEY in a more conventional industry standard way.

            CONTACT_ID_KEY = ""

            CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)

            # Write contact notes data dictionary to DICTIONARY FORMAT file  
            # Note that we use the FULLPATH - fullpath_cnotes_dict_file_global

            create_the_string_1 = "CONTACT_NOTES_DATA_RECORD_DELIMITER:"
            create_the_string_2 = str(CONTACT_ID_KEY)
            create_the_string_3 = "KEY_SYNC_TARGET_NOTES_STRING:"
            create_the_string_4 = str(final_built_string)

            complete_data_block = create_the_string_1 + create_the_string_2 + \
                                  create_the_string_3 + create_the_string_4

            
            # Prepend complete_data_block to beginning of cnotes flle 
            # using fullpath_prepend_cnotes_dict_file_global        

            with open(fullpath_cnotes_dict_file_global, 'r+') as f:
                 all_notes_content = f.read()
                 f.seek(0, 0)
                 f.write(complete_data_block.rstrip('\r\n') + '\n' + all_notes_content)




      def retrieve_contact_notes(self):
            #print("..... RETRIEVING CONTACT NOTES .....")
            # INSERT CONTACT NOTES DATA LINES into TEXTBOX to VIEW the TEXTBOX
            # after loading the current LOGFILE using the full path name:
            # fullpath_cnotes_dict_file_global.
            #
            # NOTE: This is the format of the Contact Notes Data Block:
            # 
            # create_the_string_1 = "CONTACT_NOTES_DATA_RECORD_DELIMITER:"
            # create_the_string_2 = str(CONTACT_ID_KEY)
            # create_the_string_3 = "KEY_SYNC_TARGET_NOTES_STRING:"
            # create_the_string_4 = str(final_built_string)
            #
            # where the CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)
            #
            ############################################################################

            # Clear Textbox to prepare to Retrieve Contact Notes
            self.EMAIL_Textbox.delete("1.0",END)

            fn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_info = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            # Eventually, we want to change Website to LAST FOUR OF SOCIAL SECURITY Number
            # to implement this CONTACT_ID_KEY in a more conventional industry standard way. 
            
            CONTACT_ID_KEY = ""

            CONTACT_ID_KEY = str(ln_info) + "_" + str(em_info)

            #print(".... RETRIEIVING DICTIONARY KEY:  Dict_KEY" + str(selected_dictionary_record_index_focus_global) )
            #print("  ")
            #print(".... selected_dictionary_record_index_focus_global = " + str(selected_dictionary_record_index_focus_global) )
            #print(".... First and Last Name = " + str(fn_info) + " " + str(ln_info) )
            #print(".... SPLIT STRING ON:  CONTACT_NOTES_DATA_RECORD_DELIMITER:  + str(CONTACT_ID_KEY) + KEY_SYNC_TARGET_NOTES_STRING: = ")
            #print(".... " + "CONTACT_NOTES_DATA_RECORD_DELIMITER:" + str(CONTACT_ID_KEY) + "KEY_SYNC_TARGET_NOTES_STRING:")

            create_the_sync_string_1 = str(CONTACT_ID_KEY)
            create_the_sync_string_2 = "KEY_SYNC_TARGET_NOTES_STRING:"

            complete_data_block_sync_string = create_the_sync_string_1 + create_the_sync_string_2

            #print(".... complete_data_block_sync_string = " + str(complete_data_block_sync_string) )

        
            self.textFile = open(fullpath_cnotes_dict_file_global, 'r')

            # This takes the file object opened with the open() and turns it into a string which 
            # you can now use textString in a text widget.
            self.textString = self.textFile.read()

            # Define Dictionaries here ....

            # Count the DATA RECORDS in the string by counting the
            # number of "CONTACT_NOTES_DATA_RECORD_DELIMITER:" patterns 
            self.num_data_records = self.textString.count("CONTACT_NOTES_DATA_RECORD_DELIMITER:")

            #print("..... NUMBER OF DATA RECORDS = " + str(self.num_data_records) )

            self.num_data_records_plus_one = self.num_data_records + 1

            track_text_widget_inserts = 0

            cummulative_notes_string = ""
            
            ####################################################################################
            #
            # Operate on the textString to search for complete_data_block_sync_string
            #
            # which is made up of the concatenation of these sub-strings:
            # 
            # 1. str(CONTACT_ID_KEY) string
            #
            # 2. "KEY_SYNC_TARGET_NOTES_STRING:" string
            #
            for record_index in range (1, self.num_data_records_plus_one):
                  
                self.data_record_string = self.textString.split("CONTACT_NOTES_DATA_RECORD_DELIMITER:")[record_index]

                #print("  ")
                #print(".... NOW PROCESSING record_index: " + str(record_index) + " of " + str(self.num_data_records) )
                #print(".... self.data_record_string = " + str(self.data_record_string) )
                
                try:
                      target_notes_string = self.data_record_string.split(str(complete_data_block_sync_string) )[1]

                      track_text_widget_inserts +=1

                      #print(".... str(complete_data_block_sync_string) = " + str(complete_data_block_sync_string) )
                      #print(".... target_notes_string = " + str(target_notes_string) )

                      temp_string_variable = ""

                      temp_string_variable = str(cummulative_notes_string) + str(target_notes_string)

                      cummulative_notes_string = temp_string_variable

                      #print(".... cummulative_notes_string = " + str(cummulative_notes_string) )


                except:
                      pass

            ##############    verifying append to string and append to TEXT WIDGET    ##############  
                
            try:
                  self.EMAIL_Textbox.insert("1.0", str(cummulative_notes_string) )
                  
                  #print("..... *** FINAL *** CUMMULATIVE NOTES STRING = " + str(cummulative_notes_string) )

                  #print("..... *** TOTAL NOTES LOCATED FOR PERSON *** track_text_widget_inserts = " + str(track_text_widget_inserts) )

            except:
                  pass
 


      ###############################################################################
      # 
      # Programming Note: 
      #
      # Note that the generic sequence of TEXT WIDGET Commands
      # are as follows:
      #
      # SAVE CONTACT NOTES:
      #
      # contact_notes_get = self.EMAIL_Textbox.get("1.0",END)
      #
      # RETRIEVE CONTACT NOTES:
      #
      # self.EMAIL_Textbox.delete("1.0",END)
      #
      # self.EMAIL_Textbox.insert(END, str(target_notes_string))
      #
      # self.EMAIL_Textbox.insert("1.0", str(target_notes_string))
      #
      ###############################################################################

           

      def src_addr_widget_function(self, event, src_addr_widget_name):
            self.last_widget_name_clicked = src_addr_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def clistname_widget_function(self, event, clist_widget_name):
            self.last_widget_name_clicked = clist_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def pwd_widget_function(self, event, pwd_widget_name):
            self.last_widget_name_clicked = pwd_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def cc_widget_function(self, event, cc_widget_name):
            self.last_widget_name_clicked = cc_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def to_widget_function(self, event, to_widget_name):
            self.last_widget_name_clicked = to_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def title_widget_function(self, event, title_widget_name):
            self.last_widget_name_clicked = title_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def content_widget_function(self, event, content_widget_name):
            self.last_widget_name_clicked = content_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )


      def status_widget_function(self, event, status_widget_name):
            self.last_widget_name_clicked = status_widget_name
            #print("\n")
            #print("self.last_widget_name_clicked = " + str(self.last_widget_name_clicked) )



            
      ######################################################################################
      # 
      # textbox_edit_ Mode Select Optons Menu StringVar setting ...
      #   
      # if tb_mode_select_opt_menu_select == "DROPDOWN MENU CHOICE": 
      # then execute corresponding email content textbox edit.
      #
      ######################################################################################
      #
      # IMPORTANT NOTE:  <event>  ---  Capture WIDGET NAME with print event.widget
      #
      # Update this to form and utilize a WIDGET NAME OF LAST EVENT GLOBAL
      # so that we can implement the code below with a Dynamically Changing
      # WIDGET NAME OF LAST EVENT GLOBAL where the latest curcor click happened
      # instead of the just he static self.EMAIL_Textbox implemntation.
      #           
      ######################################################################################
      #
      def func_set_textbox_edit_mode_select_global(self, tb_mode_select_opt_menu_select):
             global textbox_edit_mode_select_global

             textbox_edit_mode_select_global = str(tb_mode_select_opt_menu_select)

             self.w = self.last_widget_name_clicked

             # EDIT EMAIL DROPDOWN MENU. 
             #
             if tb_mode_select_opt_menu_select == "CLEAR Email or NOTES Content":
                   self.entry_EMAIL_STATUS.set("")
                   self.entry_EMAIL_TITLE.set("")
                   self.EMAIL_Textbox.delete('1.0', END)
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "CUT Selected Text - (CNTL-X)":
                   #print("... CUT ...")
                   
                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"
                   
                   # ORIGINAL COMMAND 1: self.EMAIL_Textbox.clipboard_clear()
                   #
                   new_command_string_CUT_1 = self.last_widget_name_clicked + ".clipboard_clear()"
                   #print("..... new_command_string__CUT_1 = " + str(new_command_string_CUT_1) )
                   exec(new_command_string_CUT_1)  # to insert self.last_widget_name_clicked

                   # ORIGINAL COMMAND 2: selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                   #
                   # but the ENTRY WIDGET does not take any arguements for GET
                   # and the TEXT WIDGET does take arguements for GET
                   # so we must do an IF statement to discern betweem ENTRY AND TEXT WIDGETS ...
                   # to format this command accordingly ... 
                   # 
                   # get(tk.SEL_FIRST, tk.SEL_LAST) for TEXT WIDGET 
                   # get() for ENTRY WIDGET 
                   # 
                   # entry class get does not take any arguments (but text class does)
                   #
                   
                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = str(self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         selected_text = str(self.source_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         selected_text = str(self.source_email_password_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.loaded_contact_name_entry":
                         selected_text = str(self.loaded_contact_name_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         selected_text = str(self.destination_1_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         selected_text = str(self.destination_cc_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         selected_text = str(self.email_title_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         selected_text = str(self.email_status_entry.get() )


                   #print("\n")
                   #print("..... selected_text = " + str(selected_text) )
                   

                   # ORIGINAL COMMAND 3: EMAIL_Textbox.master.clipboard_append(selected_text)
                   
                   new_command_string_CUT_3 = self.last_widget_name_clicked + ".master.clipboard_append(selected_text)"

                   #print("\n")
                   #print(".... new_command_string_CUT_3 = " + str(new_command_string_CUT_3) )

                   exec(new_command_string_CUT_3)  # to insert self.last_widget_name_clicked
                   
                   # ORIGINAL COMMAND 4: self.EMAIL_Textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)
                   # Now we update code to accomodate select beween TEXT Widget or ENTRY Widget 
                   # because TEXT Widget and ENTRY Widget have different commands to select text.

                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         self.EMAIL_Textbox.delete(tk.SEL_FIRST, tk.SEL_LAST)

                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         self.entry_SOURCE_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         self.entry_SOURCE_EMAIL_PASSWORD.set("")
                         
                   elif self.last_widget_name_clicked == "self.loaded_contact_name_entry":
                         self.entry_LOADED_CONTACT_NAME.set("")
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         self.entry_DEST_1_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         self.entry_DEST_CC_EMAIL_ADDRESS.set("")
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         self.entry_EMAIL_TITLE.set("")
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         self.entry_EMAIL_STATUS.set("")
                         
                   else:
                         pass

                                            
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "COPY Selected Text - (CNTL-C)":
                   #print("... COPY ...")

                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"
                   
                   # ORIGINAL COMMAND 1: self.EMAIL_Textbox.clipboard_clear()
                   new_command_string_1 = self.last_widget_name_clicked + ".clipboard_clear()"
                   #print("..... new_command_string_1 = " + str(new_command_string_1) )
                   exec(new_command_string_1)  # to insert self.last_widget_name_clicked
                   
                   # ORIGINAL COMMAND 2: selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                   # but the ENTRY WIDGET does not take any aruements for GET
                   # and the TEXT WIDGET does take argements for GET
                   # so we must do an IF statement to discern betweem ENTRY AND TEXT WIDGETS ...
                   # to format this command accordingly ... 
                   # 
                   # get(tk.SEL_FIRST, tk.SEL_LAST) for TEXT WIDGET 
                   # get() for ENTRY WIDGET 
                   # 
                   # entry class get does not take any arguments (but text class does)
                   #
                   
                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = str(self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         selected_text = str(self.source_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         selected_text = str(self.source_email_password_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.loaded_contact_name_entry":
                         selected_text = str(self.loaded_contact_name_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         selected_text = str(self.destination_1_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         selected_text = str(self.destination_cc_email_address_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         selected_text = str(self.email_title_entry.get() )
                         
                   elif self.last_widget_name_clicked == "self.email_status_entry":
                         selected_text = str(self.email_status_entry.get() )
                         

                   #print("\n")
                   #print("..... selected_text = " + str(selected_text) )


                   # ORIGINAL COMMAND 3: EMAIL_Textbox.master.clipboard_append(selected_text)
                   new_command_string_3 = self.last_widget_name_clicked + ".master.clipboard_append(selected_text)"

                   #print("\n")
                   #print(".... new_command_string_3 = " + str(new_command_string_3) )

                   exec(new_command_string_3)  # to insert self.last_widget_name_clicked

                   # ORIGINAL COMMANDS WITH ONLY THE TEXT WIDGET
                   # self.EMAIL_Textbox.clipboard_clear() 
                   # selected_text = self.EMAIL_Textbox.get(tk.SEL_FIRST, tk.SEL_LAST) 
                   # self.EMAIL_Textbox.master.clipboard_append(selected_text) 
                   
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "PASTE to Cursor - (CNTL-V)":
                   #print("... PASTE ...")  

                   selected_text = "INITIALIZE SELECTED TEXT LOCAL VARIABLE"

                   # clip_text = root.clipboard_get()
                   clip_text = self.master.clipboard_get()
                   #print("\n")
                   #print("....... clip_text = " + str(clip_text) )

                   #
                   # ORIGINAL COMMAND 1:
                   #
                   # selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                   #  

                   if self.last_widget_name_clicked == "self.EMAIL_Textbox":
                         selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                         self.EMAIL_Textbox.insert('insert', selected_text)

                   elif self.last_widget_name_clicked == "self.source_email_address_entry":
                         self.entry_SOURCE_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.source_email_password_entry":
                         self.entry_SOURCE_EMAIL_PASSWORD.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.destination_1_email_address_entry":
                         self.entry_DEST_1_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.destination_cc_email_address_entry":
                         self.entry_DEST_CC_EMAIL_ADDRESS.set(str(clip_text) )
                         
                   elif self.last_widget_name_clicked == "self.email_title_entry":
                         self.entry_EMAIL_TITLE.set(str(clip_text) )
                         
                   else:
                         pass

                   # ORIGINAL COMMANDS with TEXT Widget: 
                   # selected_text = self.EMAIL_Textbox.selection_get(selection='CLIPBOARD')
                   # self.EMAIL_Textbox.insert('insert', selected_text)
                   
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) )
                   
             elif tb_mode_select_opt_menu_select == "EDIT MENU":
                   return
             else:
                   # re-initialize OptionMenu 
                   textbox_edit_mode_select_global = "EDIT MENU"
                   self.tb_mode_select_opt_menu_select.set(str(textbox_edit_mode_select_global) ) 
                   return


                   

      def load_next_contact(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global

            test_forward_count = selected_dictionary_record_index_global + 1
            
            if test_forward_count <= num_of_dictionary_data_records_global:
                  pass
            elif test_forward_count > num_of_dictionary_data_records_global:
                  return

            # Increment Dictionary Contact Index. 

            selected_dictionary_record_index_global +=1
            selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "Contact: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            selected_dictionary_counter_status_display = "Contact # " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )



      def load_previous_contact(self):
            global selected_dictionary_record_index_global
            global selected_dictionary_record_index_focus_global

            test_backward_count = selected_dictionary_record_index_global - 1
            
            if test_backward_count >= 1:
                  pass
            elif test_backward_count < 1:
                  return
                  
            # Decrement Dictionary Contact Index.

            selected_dictionary_record_index_global -=1
            selected_dictionary_record_index_focus_global = selected_dictionary_record_index_global

            fn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
            ln_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
            sa_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
            ct_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
            st_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
            zc_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
            pn_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
            em_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
            ws_load = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] )

            first_and_last_name = "Contact: " + str(fn_load) + " " + str(ln_load)

            self.entry_LOADED_CONTACT_NAME.set(str(first_and_last_name) )

            self.entry_DEST_1_EMAIL_ADDRESS.set(str(em_load) )

            selected_dictionary_counter_status_display = "Contact # " + str(selected_dictionary_record_index_focus_global) + \
             " of " + str(num_of_dictionary_data_records_global) 

            self.entry_EMAIL_STATUS.set(str(selected_dictionary_counter_status_display) )




      def get_credentials(self):
          global credential_home_dir_global
          global credential_appdata_dir_global
          global credential_home_path_global
          global credential_appdata_path_global
          global client_secret_path_global
          global gmail_oauth2_json_file_test_global
          global gmail_oauth2_status_global
          global gmail_oauth2_exceptions_status_global
          global gmail_oauth2_SPECIFIC_EXCEPTION_global
          global gmail_smtp_allow_less_secure_apps_global
          global gmail_smtp_status_global
          global gmail_smtp_exceptions_status_global
          global gmail_smtp_SPECIFIC_EXCEPTION_global
          global gmail_mode_global
          global credential_home_dir_global
          global credential_appdata_dir_global
          global credential_home_path_global
          global credential_appdata_path_global
          global client_secret_path_global
          #
          #
          # Gets valid user credentials from storage.
          # If nothing has been stored, or if the stored credentials are invalid,
          # the OAuth2 flow is completed to obtain the new credentials.
          #
          # Returns:  
          #
          # Credentials, the obtained credential (in the client_secret.json file).
          #
          # Credentials are Stored Here to save then where http will look for them:
          # credential_home_path_global = os.path.join(credential_home_dir_global, "gmail-python-quickstart.json")
          #
          # Credentials are Stored Here to save then to APPDATA Area:
          # credential_appdata_path_global = os.path.join(credential_appdata_dir_global, "gmail-python-quickstart.json")
          #
          # NOTE the following global variables in code below: (set at top of file)
          #
          # CLIENT_SECRET_FILE, SCOPES, APPLICATION_NAME
          #
          # If modifying these scopes, delete your previously saved credentials
          # at ~/.credentials/gmail-python-quickstart.json
          #
          # SCOPES = "https://mail.google.com"
          # CLIENT_SECRET_FILE = 'client_secret.json' 
          # APPLICATION_NAME = 'Gmail API Python Quickstart' 
          # 
          ###############################################################################################

          # see if our SCOPES, CLIENT_SECRET_FILE, and APPLICATION_NAME Globals are seen here
          # YES, They are printed OK. They are visible from here. 
          # These are SET at the top of this contact_management.py file.  
          #
          # print(".... APPLICATION_NAME = " + str(APPLICATION_NAME) )
          # print(".... CLIENT_SECRET_FILE = " + str(CLIENT_SECRET_FILE) )
          # print(".... SCOPES = " + str(SCOPES) )
          
          # we store credentials here because the credentials = store.get() below looks for them here. 

          # store = Storage(credential_home_path_global)  

          home_dir = os.path.expanduser('~')
          credential_dir = os.path.join(home_dir, '.credentials')
          client_secret_dir = os.path.join(home_dir, '.credentials')
          if not os.path.exists(credential_dir):
              os.makedirs(credential_dir)
              
          credential_path = os.path.join(credential_dir, 'gmail-python-quickstart.json')
          client_secret_path = os.path.join(credential_dir, 'client_secret.json')

          # Test the open in read mode of client_secret.json file here
          # and if it fails then set status panel specific exception
          # gmail_oauth2_SPECIFIC_EXCEPTION_global == "FileNotFoundError"

          try:
              
              client_secret_textFile = open(client_secret_path_global, 'r')

              client_secret_textString = client_secret_textFile.read()

          except Exception:
              exc_type, exc_value, exc_traceback = sys.exc_info()
              lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
              exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

              gmail_oauth2_SPECIFIC_EXCEPTION_global = "FileNotFoundError"
                    
              # open Write_Exception_Logfile() to append logfile to update the logfile items.
              inst_Write_Exception_Logfile_open_client_secret_to_read = Write_Exception_Logfile()
              exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
              exception_logging_string_3 = "\n\n"
                    
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_1) )
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_2) )
              inst_Write_Exception_Logfile_open_client_secret_to_read.log_exception(str(exception_logging_string_3) )
          
          
          ###########################################################################
          #
          #    get credentials .......
          #
          # If modifying these scopes, delete your previously saved credentials
          # at ~/.credentials/gmail-python-quickstart.json
          #
          ###########################################################################
          
          SCOPES = "https://mail.google.com"
          CLIENT_SECRET_FILE = client_secret_path
          APPLICATION_NAME = 'Gmail API Python Quickstart'

          # Store the credential
          store = oauth2client.file.Storage(credential_path)

          credentials = store.get()
          
          if not credentials or credentials.invalid:
              flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
              flow.user_agent = APPLICATION_NAME
              if flags:
                  credentials = tools.run_flow(flow, store, flags)
                  storing_credentials_message = ".... WAIT 5 Seconds - Storing OAUTH2 Credentials to: " + str(credential_home_path_global)
                  self.entry_EMAIL_STATUS.set(str(storing_credentials_message) )
                  # print(str(storing_credentials_message))
                  time.sleep(5)
              else: # Needed only for compatibility with Python 2.6
                  credentials = tools.run(flow, store)
                  storing_credentials_message = ".... WAIT 5 Seconds - Storing OAUTH2 Credentials to: " + str(credential_home_path_global)
                  self.entry_EMAIL_STATUS.set(str(storing_credentials_message) )
                  # print(str(storing_credentials_message))
                  time.sleep(5)
                  
          return credentials


 

      def SendMessage(self, service, user_id, message):
          #
          # Send an email message.
          #
          #  Args:
          #   service: Authorized Gmail API service instance.
          #   user_id: User's email address. The special value "me"
          #   can be used to indicate the authenticated user. 
          #   message: Message to be sent.
          #
          #  Returns: 
          #
          #   Sent Message.
          #
          try:
                message = (service.users().messages().send(userId=user_id, body=message).execute())
                print('Message Id: ' + str(message['id'] ) )
                return message
          
          except Exception as ex:
                temp_time_string = str(datetime.datetime.now() )
                complete_email_status_string = "GMAIL  S E N D   E R R O R - Verify OAUTH2 Credentials - TIME = " + str(temp_time_string)
                self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )
                
                # print(str(complete_email_status_string) )
                # print(ex)


                

      # def create_message_with_attachment(
      #     sender, to, subject, message_text, file):

                
      def create_message_with_attachment(self):

          # Create a message for an email.
          #
          # Args:
          #   sender: Email address of the sender.
          #   to: Email address of the receiver.
          #   subject: The subject of the email message.
          #   message_text: The text of the email message.
          #   file: The path to the file to be attached.
          #
          # Returns:
          #   An object containing a base64url encoded email object.

          COMMASPACE = ", "
          TOADDR = []
          CCADDR = []

          # TOADDR is a PYTHON LIST - use split to build this PYTHON LIST
          # from the TEXT WIDGET input get string
          # my_list = my_string.split(",")
          
          TOADDR = str(self.destination_1_email_address).split(",")
          
          # CCADDR is a PYTHON LIST - use split to build this PYTHON LIST
          # from the TEXT WIDGET input get string
          # my_list = my_string.split(",")
          
          CCADDR = str(self.destination_cc_email_address).split(",")
          
          #
          # Programming Note:  These are Python LISTS  ..... 
          #
          # TOADDR   = ["email_one@gmail.com", "email_two@outlook.com"]
          # CCADDR   = ["email_three@gmail.com", "email_four@outlook.com"]
          #
          #
          # Replacing this: 
          #
          # message = MIMEMultipart()
          #
          # with this:
          #
          # message = MIMEMultipart('alternative')
          #
          # Create message container - the correct MIME type is multipart/alternative.
          #
          #######################################################################################
          #
          #  One guy said to do this ........
          #
          #  msg.set_payload(contents)
          #  ##  Encode the payload using Base64.  This line is from here:
          #  ##  https://docs.python.org/3/library/email-examples.html
          #  encoders.encode_base64(msg)
          #
          #######################################################################################
          #
          #  Another guy said to do this  .......
          #
          # with open(file, 'rb') as pdf_file:
          #      pdf = MIMEBase('application', "pdf")
          #      pdf.set_payload(pdf_file.read())
          #      encoders.encode_base64(pdf)
          #      pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
          #
          # message.attach(pdf)
          #
          # return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
          #
          # debugging and inegration .....

          
          message            = MIMEMultipart('alternative')
          message['Subject'] = str(self.email_title)
          message['From']    = str(self.source_email_address)
          message['To']      = COMMASPACE.join(TOADDR)
          message['Cc']      = COMMASPACE.join(CCADDR)

          body = str(self.email_content)
              
          message.attach(MIMEText(body, 'plain'))

          file = self.file_email_attachment_full_path

          content_type, encoding = mimetypes.guess_type(file)

          if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
          main_type, sub_type = content_type.split('/', 1)
          if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
          elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
          elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
          else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
          filename = os.path.basename(file)
          msg.add_header('Content-Disposition', 'attachment', filename=filename)
          message.attach(msg)

          return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

          # return {'raw': base64.urlsafe_b64encode(message.as_string())}

                

      def CreateMessage(self):
            #
            # Create a message for an email.
            #
            # Returns: 
            #
            # An object containing a base64url encoded email object.
            #
            #################################################################

            COMMASPACE = ", "
            TOADDR = []
            CCADDR = []

            # TOADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            TOADDR = str(self.destination_1_email_address).split(",")
            
            # CCADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            CCADDR = str(self.destination_cc_email_address).split(",")  

            # Programming Note:  These are Python LISTS  ..... 
            #
            # TOADDR   = ["email_one@gmail.com", "email_two@outlook.com"]
            # CCADDR   = ["email_three@gmail.com", "email_four@outlook.com"]
            #

            # Replacing this:
            #
            # message = MIMEText(message_text)
            #
            # with this:
            #
            # message            = MIMEMultipart('alternative')
            #
            # Create message container - the correct MIME type is multipart/alternative.
            
            message            = MIMEMultipart('alternative')
            message['Subject'] = str(self.email_title)
            message['From']    = str(self.source_email_address)
            message['To']      = COMMASPACE.join(TOADDR)
            message['Cc']      = COMMASPACE.join(CCADDR)

            body = str(self.email_content)
              
            message.attach(MIMEText(body, 'plain'))
            
            return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}



      ################################################################################
      #
      # Select Gmail Mode based on GLOBAL Setting.
      #    
      # gmail_mode_global = "OAUTH2_Gmail_Mode" or "SMTP_Gmail_Mode"
      #
      def get_decision_Textbox_File(self, event):
            global gmail_mode_global
            
            if gmail_mode_global == "OAUTH2_Gmail_Mode":
                  self.get_Textbox_File_for_OAUTH2_Email()
            elif gmail_mode_global == "SMTP_Gmail_Mode":
                  self.get_Textbox_File()
            else:
                  return
              

      #######################################################################
      #
      # Attention:   EMAIL ATTACHMENT OPTION  ..... 
      #
      # IF  self.EMAIL_ATTACHMENT_OPTION_FLAG == True 
      #
      # If the EMAIL ATTACHMENT OPTION FLAG is SET,
      # we add the attachment file for the EMail
      # and that attachent file name (FULL PATH)
      # was acquired using our EMAIL ATTACHMENT BUTTON
      # and this dialog_to_get_file_attachment (Dialog Method).
      #  
      #######################################################################

      def email_attachment_option_method(self, event):

          self.EMAIL_ATTACHMENT_OPTION_FLAG = True

          # create and build the return_object_list ......
          #
          # return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type, content_type, main_type, sub_type, encoding]
          #
          # return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type, content_type, main_type, sub_type, encoding]
          # from the self.dialog_to_get_file_attachment() Method. 

          # Create List to store objects returned from self.dialog_to_get_file_attachment() METHOD 

          objects_returned_from_METHOD = []

          objects_returned_from_METHOD = self.dialog_to_get_file_attachment()

          # Extract objects from list:   

          self.file_email_attachment_FULL_PATH = objects_returned_from_METHOD[0]

          self.file_email_attachment_FILE_NAME = objects_returned_from_METHOD[1]

          self.file_email_attachment_FILE_TYPE = objects_returned_from_METHOD[2]

          self.file_email_attachment_CONTENT_TYPE = objects_returned_from_METHOD[3]        

          self.file_email_attachment_MAIN_TYPE = objects_returned_from_METHOD[4]

          self.file_email_attachment_SUB_TYPE = objects_returned_from_METHOD[5]

          self.file_email_attachment_ENCODING = objects_returned_from_METHOD[6]
          
          

          print("\n" + "..... Extracted FULL_PATH from return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type] : " + "\n" + str(self.file_email_attachment_FULL_PATH) + "\n")

          print("..... Extracted FILE_NAME from return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type] : " + "\n" + str(self.file_email_attachment_FILE_NAME) + "\n")

          print("..... Extracted FILE_TYPE from return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type] : " + "\n" + str(self.file_email_attachment_FILE_TYPE) + "\n")



      def dialog_to_get_file_attachment(self):

          ###########   Select a Directory:

          root = tk.Tk()
          root.withdraw()
          home_dir = os.path.expanduser('~')
          dirname = filedialog.askdirectory(parent=root,initialdir=home_dir,title='Please select a directory')

          directory_full_path = os.path.join(str(home_dir), str(dirname) )

          print("\n\n\n")
          print(".... DIRECTORY (FULL PATH): " + str(directory_full_path) )


          ############   Select a File for Opening:  

          # askopenfile - opens the file and returns the opened object (or Null if cancelled).

          # askopenfilename - just gets and returns the full path to the file (or empty string if cancelled).

          ftypes = [
              ('All Files', '*.*'),
              ("Word Files","*.docx"),
              ("PDF Files","*.pdf"),
              ("Excel Worksheet Files","*.xlsx"),
              ("Excel Files","*.xls"),
              ("Excel CSV Files","*.csv"),
              ("Powerpoint Files","*.pptx"),
              ("MSI Files","*.msi"),
              ("XML Files","*.xml"),
              ("HTML Files","*.html"),
              ('Text Files', '*.txt'),
              ("JPEG Files","*.jpg"),
              ("GIF Files","*.gif"),
              ("PNG Files","*.png"),
              ("Bitmap Files","*.bmp"),
              ("MPEG4 Video Files","*.mp4"),
              ("WAV Video Files","*.wav"),
              ("WMA Video Files","*.wma"),
              ("WMV Video Files","*.wmv"),
              ("Config Files","*.cfg"),
              ("Initialization Files","*.ini"),
              ('Python Code Files', '*.py'), 
              ('Perl Code Files', '*.pl;*.pm'),  # semicolon trick
              ('Java Code Files', '*.java'),
              ('Java Server Files', '*.jsp'),
              ('Java Class Files', '*.class'),
              ('JSON Files', '*.json'), 
              ('C++ Code Files', '*.cpp;*.h'),   # semicolon trick
              ("Binary Files","*.bin"),
              ("Executable Files","*.exe"),
              ("Windows System Files","*.sys"),
              ("Batch Files","*.bat"),
              ("Data Files","*.dat"),
              ("ZIP Files","*.zip"),
              ("7Z Files","*.7z"),
              ("TAR Files","*.tar")
          ]

          root = tk.Tk()
          root.withdraw()

          # NOTE:
          #
          # askopenfilename - gets and returns the full path to the file.
          
          dialog_filename_full_path = filedialog.askopenfilename(parent=root,title='Choose a file',filetypes = ftypes)

          print(".... FILE (FULL PATH): " + str(dialog_filename_full_path) )

          dialog_filename = os.path.basename(dialog_filename_full_path)

          print(".... FILE NAME: " + str(dialog_filename) )

          dialog_file_type = dialog_filename.split(".")[1]

          print("..... FILE TYPE: " + str(dialog_file_type) ) 

          # This data_BYTE_TYPE is not used at this time.
          data_BYTE_TYPE = b"INITIALIZE_BYTES_TYPE_OBJECT"   # BYTES TYPE OBJECT 

          #######################################################################################################

          # View the system encoding default
          system_encoding_default = sys.getdefaultencoding()

          print("..... SYSTEM ENCODING DEFAULT from sys.getdefaultencoding() = " + str(system_encoding_default) )
          
          # NOTE:
          #
          # View the content_type, the main_type and sub_type, and the encoding
          # using:  mimetypes.guess_type(file_full_path)  

          content_type, encoding = mimetypes.guess_type(dialog_filename_full_path)

          print("..... content_type = " + str(content_type) )

          print("..... encoding = " + str(encoding) )
                    
          main_type, sub_type = content_type.split('/', 1)

          print("..... main_type = " + str(main_type) )

          print("..... sub_type = " + str(sub_type) )

          print("..... dialog_file_type = " + str(dialog_file_type) ) 

          print(".... FILE NAME: " + str(dialog_filename) )

          print("..... FILE TYPE: " + str(dialog_file_type) ) 

          dialog_file_type = dialog_filename.split(".")[1]

          print("\n")
          print("**************************************************************************************************************") 
          print(".... return:  dialog_filename_full_path : " + str(dialog_filename_full_path) )
          print("**************************************************************************************************************")

          # create and build the return_object_list 

          return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type, content_type, main_type, sub_type, encoding]

          # return_object_list = [dialog_filename_full_path, dialog_filename, dialog_file_type, content_type, main_type, sub_type, encoding]


          return return_object_list


          
      #################################################################################################
      #
      # When the Operator presses SEND EMAIL, if the gmail_mode_global = "OAUTH2_Gmail_Mode"  
      # then since the button event has a bind to the above get_decision_Textbox_File method,
      # the method above calls this get_Textbox_File_for_OAUTH2_Email method.
      #
      def get_Textbox_File_for_OAUTH2_Email(self):
            global gmail_oauth2_json_file_test_global
            global gmail_oauth2_status_global
            global gmail_oauth2_exceptions_status_global
            global gmail_oauth2_SPECIFIC_EXCEPTION_global
            self.source_email_address = self.source_email_address_entry.get()
            self.source_email_password = self.source_email_password_entry.get()
            self.destination_1_email_address = self.destination_1_email_address_entry.get()
            self.destination_cc_email_address = self.destination_cc_email_address_entry.get()
            self.email_title = self.email_title_entry.get()
            self.entry_EMAIL_STATUS.set("")

            #######################################################################
            #
            # Attention:   EMAIL ATTACHMENT OPTION  .....
            #  
            # IF  self.EMAIL_ATTACHMENT_OPTION_FLAG == True 
            #
            # If the EMAIL ATTACHMENT OPTION FLAG is SET,
            # we add the attachment file for the EMail
            # and that attachent file name (FULL PATH)
            # was acquired using our EMAIL ATTACHMENT BUTTON
            # and the dialog_to_get_file_attachment (Dialog Method).
            #
            #######################################################################

            # TEMPORARILY PUTTING THIS HERE FOR DEBUG
            # OF EMAIL ATTACHMENT METHOD AND PROCESS ..........

            ####    self.email_attachment_option_method()

            #######################################################################
            
            # Create a Time Stamp
            temp_time_string = str(datetime.datetime.now() )

            complete_email_status_string = ""

            encode_as_bytes = ""

            COMMASPACE = ", "
            TOADDR = []
            CCADDR = []

            # TOADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            TOADDR = str(self.destination_1_email_address).split(",")
            
            # CCADDR is a PYTHON LIST - use split to build this PYTHON LIST
            # from the TEXT WIDGET input get string
            # my_list = my_string.split(",")
            
            CCADDR = str(self.destination_cc_email_address).split(",")  

            # Programming Note:  These are Python LISTS  ..... 
            #
            # TOADDR   = ["email_one@gmail.com", "email_two@outlook.com"]
            # CCADDR   = ["email_three@gmail.com", "email_four@outlook.com"] 
            #
            ####################################################################
            #
            # Tips on using MIME .....
            # 
            # message = MIMEText(text)
            # message["From"] = emailfrom
            # message["To"] = emailto
            # message["Subject"] = "hi find the attached file"
            #
            # message = MIMEMultipart()
            # message["From"] = emailfrom
            # message["To"] = emailto
            # message["Subject"] = "hi find the attached file"
            # message.attach(MIMEText(text))
            # attachment = MIMEBase('application', 'octet-stream')
            # attachment.set_payload(data)
            # message.attach(attachment)

            # Create message container - the correct MIME type is multipart/mixed.
            message            = MIMEMultipart('mixed')
            message['Subject'] = str(self.email_title)
            message['From']    = str(self.source_email_address)
            message['To']      = COMMASPACE.join(TOADDR)
            message['Cc']      = COMMASPACE.join(CCADDR)

            # GET the Email Content from the Text Widget
            self.email_content = self.EMAIL_Textbox.get("1.0",END)

            print("\n" + "..... self.email_content = " + str(self.email_content) + "\n")

            body_from_textbox = str(self.email_content)

            body = MIMEText(body_from_textbox, 'plain') # convert the body to a MIME compatible string
              
            message.attach(body)

            # Load message into Class Variable Object
            self.EMAIL_MESSAGE = message

            # Wondering if we will ever have to use: MIMEBase('application', 'octet-stream')
            #
            #   fp = open(the_file_full_path, 'rb')
            #   attachment = MIMEBase(main_type, sub_type)
            #   attachment.set_payload(fp.read())
            #   fp.close()
            #   attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            #   message.attach(attachment)
            #   print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")
            # 
            # 

            if self.EMAIL_ATTACHMENT_OPTION_FLAG == True:

                file = b"INITIALIZE_BYTES_TYPE_OBJECT"

                file = self.file_email_attachment_BYTES_TYPE_OBJECT

                # file is a BYTES TYPE OBJECT

                # the_file_full_path = "C:/Users/chipcoder4972/ALL_FILE_TYPES/Each_File_Name.typ"

                the_file_full_path = self.file_email_attachment_FULL_PATH

                filename = os.path.basename(the_file_full_path)

                file_type = self.file_email_attachment_FILE_TYPE

                content_type, encoding = mimetypes.guess_type(the_file_full_path)


                print("................... content_type = " + str(content_type) )

                print("................... encoding = " + str(encoding) )
                

                if content_type is None or encoding is not None:
                    content_type = 'application/octet-stream'
                    
                main_type, sub_type = content_type.split('/', 1)

                print("..... main_type = " + str(main_type) )

                print("..... sub_type = " + str(sub_type) )

                print("..... file_type = " + str(file_type) )

                ##########################################################################
                #
                # Build a LIST of each category of File Extensions to do a compare
                # to route program control to , for example: 
                #
                #   content_type = "text/plain"
                #   file_type = txt (and other txt-like files)
                #   and the TEXT File attachment sequence:
                #
                #   fp = open(str(the_file_full_path), 'r')
                #   attachment = MIMEText(fp.read(), _subtype=sub_type)
                #
                ##########################################################################
                #
                #   content_type = "image/image_file_type"
                #   file_type = jpg, png, gif, etc.
                #   and the IMAGE File attachment sequence:
                #
                #   fp = open(str(the_file_full_path), 'rb')
                #   attachment = MIMEImage(fp.read(), _subtype=sub_type)
                #
                ##########################################################################
                #
                #   main_type = application 
                #   file_type = docx, xlsx, pptx, etc.
                #
                #   attachment = MIMEApplication(docx_file_handle.read(),Name=filename)
                #
                ##########################################################################
                #
                #  We can route attachment processing base on whether the file_type,
                #  which is the file extension (txt, jpg, ini, docx, xlsx, etc) is in
                #  the list associated with each particular class of MIME container
                #  attachment processing using the string compare of the file_type
                #  with the MIME container type: 
                #
                file_extension_MIME_Application_LIST = ["docx", "xlsx", "pptx"]

                file_extension_MIME_Image_LIST = ["jpg", "png", "gif"]

                file_extension_MIME_Audio_LIST = ["mp4", "mp3", "wav"]

                file_extension_MIME_Text_LIST = ["txt", "pl", "json", "ini", "cfg", "cc"]

                # ('All Files', '*.*'),
                # ("Word Files","*.docx"),
                # ("PDF Files","*.pdf"),
                # ("Excel Worksheet Files","*.xlsx"),
                # ("Excel Files","*.xls"),
                # ("Excel CSV Files","*.csv"),
                # ("Powerpoint Files","*.pptx"),
                # ("MSI Files","*.msi"),
                # ("XML Files","*.xml"),
                # ("HTML Files","*.html"),
                # ('Text Files', '*.txt'),
                # ("JPEG Files","*.jpg"),
                # ("GIF Files","*.gif"),
                # ("PNG Files","*.png"),
                # ("Bitmap Files","*.bmp"),
                # ("MPEG4 Video Files","*.mp4"),
                # ("WAV Video Files","*.wav"),
                # ("WMA Video Files","*.wma"),
                # ("WMV Video Files","*.wmv"),
                # ("Config Files","*.cfg"),
                # ("Initialization Files","*.ini"),
                # ('Python Code Files', '*.py'), 
                # ('Perl Code Files', '*.pl;*.pm'),  # semicolon trick
                # ('Java Code Files', '*.java'),
                # ('Java Server Files', '*.jsp'),
                # ('Java Class Files', '*.class'),
                # ('JSON Files', '*.json'), 
                # ('C++ Code Files', '*.cpp;*.h'),   # semicolon trick
                # ("Binary Files","*.bin"),
                # ("Executable Files","*.exe"),
                # ("Windows System Files","*.sys"),
                # ("Batch Files","*.bat"),
                # ("Data Files","*.dat"),
                # ("ZIP Files","*.zip"),
                # ("7Z Files","*.7z"),
                # ("TAR Files","*.tar")
                #
                #
                ################################################################################
                #
                # self.file_email_attachment_FILE_TYPE acquired via dialog method:
                #
                #     dialog_to_get_file_attachment()
                #
                # and the Email attachments button press method (which calls dialog method:
                #
                #     email_attachment_option_method()
                #
                ################################################################################
                
                selected_file_type = self.file_email_attachment_FILE_TYPE

                print(".... LOOPS BELOW .... selected_file_type at the LOOPS is: " + str(selected_file_type) + "\n")

                print(".... LOOPS BELOW .... main_type at the LOOPS is: " + str(main_type) + "\n")

                # initialize the attachment_flow_flag.
                attachment_flow_flag = "NO_FLOW_SET_YET"


                for index, item in enumerate(file_extension_MIME_Application_LIST, start = 1):
                    print(".... MIME_Application_LIST .... S E A R H .... ")
                    if ( (selected_file_type == item) and (main_type == "application") ):
                        print("********   Execute MIMEApplication EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEApplication_FLOW"

                for index, item in enumerate(file_extension_MIME_Image_LIST, start = 1):
                    print(".... MIME_Image_LIST .... S E A R H .... ")
                    if ( (selected_file_type == item) and (main_type == "image") ):
                        print("********   Execute MIMEImage EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEImage_FLOW"

                for index, item in enumerate(file_extension_MIME_Text_LIST, start = 1):
                    print(".... MIME Text_LIST .... S E A R H .... ")
                    if ( (selected_file_type == item) and (main_type == "text") ):
                        print("********   Execute MIMEText EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEText_FLOW"

                for index, item in enumerate(file_extension_MIME_Audio_LIST, start = 1):
                    print(".... MIME_Audio_LIST .... S E A R H .... ")
                    if ( (selected_file_type == item) and (main_type == "audio") ):
                        print("********   Execute MIMEAudio EMail Attachment Sequence")
                        attachment_flow_flag = "MIMEAudio_FLOW"


                if attachment_flow_flag == "MIMEApplication_FLOW":
                    self.EMAIL_base64_urlsafe_b64encode_message = self.email_attachment_MIMEApplication()
                elif attachment_flow_flag == "MIMEImage_FLOW":
                    self.EMAIL_base64_urlsafe_b64encode_message = self.email_attachment_MIMEImage()
                elif attachment_flow_flag == "MIMEText_FLOW":
                    self.EMAIL_base64_urlsafe_b64encode_message = self.email_attachment_MIMEText()
                elif attachment_flow_flag == "MIMEAudio_FLOW":
                    self.EMAIL_base64_urlsafe_b64encode_message = self.email_attachment_MIMEAudio()
                elif attachment_flow_flag == "NO_FLOW_SET_YET":
                    self.EMAIL_base64_urlsafe_b64encode_message = self.email_attachment_MIME_Radio_Button_Select()
                    

                #
                # https://developers.google.com/gmail/api/guides/sending
                #  
                # https://developers.google.com/gmail/api/quickstart/python
                #
                
                try:

                    credentials = self.get_credentials()
                    http = credentials.authorize(httplib2.Http())
                    service = discovery.build('gmail', 'v1', http=http)

                    # SEND the EMAIL message - may have to declare message field below raw ... like str()  int() 
                    self.SendMessage(service, "me", self.EMAIL_base64_urlsafe_b64encode_message)

                    gmail_oauth2_status_global = True

                    complete_email_status_string = " ... OAUTH2  E M A I L   S E N T  ... TIME = " + str(temp_time_string)
                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

                    gmail_oauth2_exceptions_status_global = True
                    
                    complete_email_status_string = "OAUTH2  E M A I L   N O T   S E N T : Verify OAUTH2 CREDENTIALS (JSON FILE) - TIME = " + str(temp_time_string)
                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                    # open Write_Exception_Logfile() to append logfile to update the logfile items.
                    inst_Write_Exception_Logfile_for_oauth2_send = Write_Exception_Logfile()
                    exception_logging_string_1 = "OAUTH2  E M A I L   N O T   S E N T  :  Verify OAUTH2 CREDENTIALS (JSON FILE) - EXCEPTION DETAILS FOLLOW: " + "\n"
                    exception_logging_string_3 = "\n\n"
                  
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_1) )
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_2) )
                    inst_Write_Exception_Logfile_for_oauth2_send.log_exception(str(exception_logging_string_3) )

                    # logger.error(str(exception_logging_string), exc_info=True)

                    # Temporary command for debug that opens the exception logfile and prints the logfile 
                    # called fullpath_exception_logfile_global and prints the logfile contents acquire using read().
                    # We typically place this print of the exception logfile where exceptions are located for debug.

                    #with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
                    #    print(exception_file_handle_var.read() )

                    # Launch Messagebox Instructing How to set up Email when EMail Sending Fails.
                    self.launch_messagebox_when_email_fails()


   
                

      def email_attachment_MIMEText(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) or (main_type == "application") ):
            #
            #####################################################################################
            #
            # EXAMPLE: 
            #
            # content_type = "text/plain"
            # main_type = "text" --------- REQUIRED --------
            # sub_type = "plain"
            # file_type = "txt" 
            #
            # NOTE that message = MIMEMultipart('mixed') and this is the attachment (a jpeg image)
            #
            # Now create the MIME container for the TEXT File:  
            # 
            # Note that for TEXT Files (or TEXT-like file_types), we open in "r" to avoid this error:
            # AttributeError: 'bytes' object has no attribute 'encode'

            # self.file_email_attachment_FILE_TYPE
            # self.file_email_attachment_CONTENT_TYPE        
            # self.file_email_attachment_MAIN_TYPE
            # self.file_email_attachment_ENCODING

            # Load the current message that is being built from its current
            # location in the corresponding Class Variable Object
            # so these MIME Methods can add the Email Attachment.
            message = self.EMAIL_MESSAGE
          
            the_file_full_path = self.file_email_attachment_FULL_PATH

            filename = self.file_email_attachment_FILE_NAME

            sub_type = self.file_email_attachment_SUB_TYPE

            fp = open(str(the_file_full_path), 'r')
            attachment = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(attachment)

            print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            # Create base64.urlsafe_b64encode of message.
            base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            return base64_urlsafe_b64encode_message

                

      def email_attachment_MIMEImage(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) or (main_type == "image") ):
            #
            #####################################################################################
            #
            # EXAMPLE: 
            #
            # NOTE: 
            #
            # content_type = "image/jpeg"
            # main_type = "image" --------- REQUIRED --------
            # sub_type = "jpeg"
            # file_type = "jpg" 
            #
            #
            # NOTE that message = MIMEMultipart('mixed') and this is the attachment (a jpeg image)
            #
            # Now create the MIME container for the JPEG Image:

            # self.file_email_attachment_FILE_TYPE
            # self.file_email_attachment_CONTENT_TYPE        
            # self.file_email_attachment_MAIN_TYPE
            # self.file_email_attachment_ENCODING

            # Load the current message that is being built from its current
            # location in the corresponding Class Variable Object
            # so these MIME Methods can add the Email Attachment.
            message = self.EMAIL_MESSAGE

            filename = self.file_email_attachment_FILE_NAME

            sub_type = self.file_email_attachment_SUB_TYPE

            the_file_full_path = self.file_email_attachment_FULL_PATH

            fp = open(str(the_file_full_path), 'rb')
            attachment = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(attachment)

            print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            # Create base64.urlsafe_b64encode of message.
            base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            return base64_urlsafe_b64encode_message


                    
      def email_attachment_MIMEApplication(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) or (main_type == "application") ):
            #
            #####################################################################################
            #
            #   EXAMPLE: 
            #
            #   xlsx produced THIS from content_type, encoding = mimetypes.guess_type(the_file_full_path)
            #
            #   main_type = application   --------- REQUIRED --------
            #
            #   sub_type = vnd.openxmlformats-officedocument.spreadsheetml.sheet
            #
            #       msg['Message-Id'] = make_msgid()
            #       msg['Date'] = formatdate(localtime=True)
            #

            # self.file_email_attachment_FILE_TYPE
            # self.file_email_attachment_CONTENT_TYPE        
            # self.file_email_attachment_MAIN_TYPE
            # self.file_email_attachment_ENCODING

            # Load the current message that is being built from its current
            # location in the corresponding Class Variable Object
            # so these MIME Methods can add the Email Attachment.
            message = self.EMAIL_MESSAGE

            filename = self.file_email_attachment_FILE_NAME

            sub_type = self.file_email_attachment_SUB_TYPE

            the_file_full_path = self.file_email_attachment_FULL_PATH

            with open(the_file_full_path, "rb") as xlsx_file_handle:
                attachment = MIMEApplication(xlsx_file_handle.read(),Name=filename)
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                message.attach(attachment)

            print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            # Create base64.urlsafe_b64encode of message.
            base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            return base64_urlsafe_b64encode_message


          
                  
      def email_attachment_MIMEAudio(self):
            #####################################################################################
            #
            # if ( (selected_file_type == item) or (main_type == "audio") ):
            #
            #####################################################################################
            #
            # EXAMPLE: 
            #
            # main_type == 'audio':
            #
            #
            #   mp4 produced THIS from content_type, encoding = mimetypes.guess_type(the_file_full_path)
            #
            #   main_type = audio   --------- REQUIRED --------
            # 
            #   sub_type = ??????????????????
            #
            #       msg['Message-Id'] = make_msgid()
            #       msg['Date'] = formatdate(localtime=True)
            #

            # self.file_email_attachment_FILE_TYPE
            # self.file_email_attachment_CONTENT_TYPE        
            # self.file_email_attachment_MAIN_TYPE
            # self.file_email_attachment_ENCODING

            # Load the current message that is being built from its current
            # location in the corresponding Class Variable Object
            # so these MIME Methods can add the Email Attachment.
            message = self.EMAIL_MESSAGE

            filename = self.file_email_attachment_FILE_NAME

            sub_type = self.file_email_attachment_SUB_TYPE

            the_file_full_path = self.file_email_attachment_FULL_PATH

            fp = open(str(the_file_full_path), 'rb')
            attachment = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(attachment)
            print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            # Create base64.urlsafe_b64encode of message.
            base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            return base64_urlsafe_b64encode_message




      def email_attachment_MIME_Radio_Button_Select(self):
            ############################################################################################
            #  
            # if ( (selected_file_type != item) and (main_type != "audio", "image", "application") ):
            #
            ############################################################################################
            # 
            # Program Flow Note:
            #
            # Before we get to this Radio Button QUERY, we will see if we can initiate
            # an email attachment MIME sequence with ONLY the main_type used to route us
            # to the MIME attachment Method.
            #
            # However, if there is no file_type match and no main_type produced,
            # then we may choose to display a message to the user that the attached
            # file is UNKNOWN category sothey can SELECT the MIME Attachment Method ...
            #
            # WE NEED A DIALOG BOX TO POP-UP HERE WITH RADIO BUTTONS
            # INSTRUCTION THE USER THAT WE CANNOT RECONGIZE THE file_type
            # or the main_type AND THEY NEED TO SELECT A RADIO BUTTON FOR:
            #
            # 1.  Application Type File 
            #
            # 2.  Image Type File 
            #
            # 3   Audio Type File 
            #
            # 4.  Text or Text-like File
            #
            # 5.  Some Default Sending Method
            #
            #     attachment = MIMEBase(main_type, sub_type)
            #
            ################################################################################

            print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")
            print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")
            print(".... R A D I O    B U T T O N   D E F A U L T   ....  S E L E C T I O N  .... " + "\n")


            # self.file_email_attachment_FILE_TYPE
            # self.file_email_attachment_CONTENT_TYPE        
            # self.file_email_attachment_MAIN_TYPE
            # self.file_email_attachment_ENCODING

            # Load the current message that is being built from its current
            # location in the corresponding Class Variable Object
            # so these MIME Methods can add the Email Attachment.
            message = self.EMAIL_MESSAGE

            filename = self.file_email_attachment_FILE_NAME

            sub_type = self.file_email_attachment_SUB_TYPE
            
            the_file_full_path = self.file_email_attachment_FULL_PATH

            with open(the_file_full_path, "rb") as file_handle:
                attachment = MIMEApplication(file_handle.read(),Name=filename)
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                message.attach(attachment)

            print("........ attachment['Content-Transfer-Encoding'] = " + str(attachment['Content-Transfer-Encoding']) + "\n")

            # Create base64.urlsafe_b64encode of message.
            base64_urlsafe_b64encode_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

            return base64_urlsafe_b64encode_message




                  
      ###########################################################################
      #   
      # This method is run via button command gets the textbox entries
      #    
      # for the following Email_Gmail_Class OBJECTS:  
      #    
      # self.source_email_address = self.source_email_address_entry.get()
      # 
      # self.source_email_password = self.source_email_password_entry.get()
      #
      # self.destination_1_email_address = self.destination_1_email_address_entry.get()
      #
      # self.destination_cc_email_address = self.destination_cc_email_address_entry.get()
      #
      # self.email_title = self.email_title_entry.get()
      #
      # self.email_content = self.email_content_entry.get()
      #
      ###########################################################################
      #
      # NEW GMAIL SECURE IMPLEMENTATION is also implemented where gmail_mode_global
      # selects oauth2 client mode as an alternative to the less secure STMP Mode:
      #
      # Old Technique requires ALLOW LESS SECURE APPS to be set in Google for
      # smtplib.SMTP("smtp.gmail.com", 587)
      #
      # New Technique implements GMail API pre-registered OAUTH2 CLIENT via the
      # client_secret.json file. 
      # 
      ###########################################################################        
      def get_Textbox_File (self):
              global textbox_edit_mode_select_global
              global gmail_smtp_allow_less_secure_apps_global
              global gmail_smtp_status_global
              global gmail_smtp_exceptions_status_global
              global gmail_smtp_SPECIFIC_EXCEPTION_global
              self.source_email_address = self.source_email_address_entry.get()
              self.source_email_password = self.source_email_password_entry.get()
              self.destination_1_email_address = self.destination_1_email_address_entry.get()
              self.destination_cc_email_address = self.destination_cc_email_address_entry.get()
              self.email_title = self.email_title_entry.get()
              self.entry_EMAIL_STATUS.set("")

              ################################################################################

              # GET THE TIME AND LOAD DATA FROM THE EMAIL CONTENT TEXT WIDGET  ......
              # and BUILD the msg Email Container ...... 

              # Create a Time Stamp
              temp_time_string = str(datetime.datetime.now() )

              # GET the Email Content from the Text Widget
              self.email_content = self.EMAIL_Textbox.get("1.0",END)

              COMMASPACE = ", "
              TOADDR = []
              CCADDR = []

              # TOADDR is a PYTHON LIST - use split to build this PYTHON LIST
              # from the TEXT WIDGET input get string
              # my_list = my_string.split(",")
              TOADDR = str(self.destination_1_email_address).split(",")
              # CCADDR is a PYTHON LIST - use split to build this PYTHON LIST
              # from the TEXT WIDGET input get string
              # my_list = my_string.split(",")
              CCADDR = str(self.destination_cc_email_address).split(",")  

              # Programming Note:  These are Python LISTS  ..... 
              #
              # TOADDR   = ["email_one@gmail.com", "email_two@outlook.com"]
              # CCADDR   = ["email_three@gmail.com", "email_four@outlook.com"]
              #

              # Create message container - the correct MIME type is multipart/alternative.
              msg            = MIMEMultipart('alternative')
              msg['Subject'] = str(self.email_title)
              msg['From']    = str(self.source_email_address)
              msg['To']      = COMMASPACE.join(TOADDR)
              msg['Cc']      = COMMASPACE.join(CCADDR)

              body = str(self.email_content)
              
              msg.attach(MIMEText(body, 'plain'))

              ################################################################################

              #print("\n")
              #print("..... str(self.source_email_address) = " + str(self.source_email_address) )
              #print("..... str(self.destination_1_email_address) = " + str(self.destination_1_email_address) )
              #print("\n")
              #print("..... str(self.email_title) = " + str(self.email_title) )
              #print("\n")
              #print("..... str(email_message_content) = " + str(self.email_content) )
              #print("\n")

              ########################################################################
              #
              #  EXECUTE THE GMAIL SERVER COMMUNICATION SEQUENCE .....     
              #           
              #  Note: Works with Google Setting: "Enable Less Secure Apps"  
              #        so now we are looking at additional security authentication
              #        process (OAUTH2) that meets google standards without having to
              #        change the Google Setting: "Enable Less Secure Apps"  
              #  
              ########################################################################

              complete_email_status_string = ""

              # Send the message via the Gmail SMTP server.
              #
              # Catch Exceptions - smtplib.SMTPException 

              try:
                    mail = smtplib.SMTP("smtp.gmail.com", 587)

                    mail.ehlo()

                    mail.starttls()

                    mail.ehlo()

                    mail.login(str(self.source_email_address), str(self.source_email_password) )

                    mail.sendmail(str(self.source_email_address), TOADDR+CCADDR, msg.as_string() )
                    #mail.sendmail(str(self.source_email_address), str(self.destination_1_email_address), str(self.email_content) )
                    #mail.sendmail(str(self.source_email_address), str(self.destination_1_email_address), str(self.email_content) )

                    mail.close()

                    gmail_smtp_status_global = True

                    self.entry_SOURCE_EMAIL_PASSWORD.set("")

                    # CREATE A STATUS TEXTBOX FOR THE *** EMAIL STATUS MESSAGES *** smtplib.SMTPException

                    # UPDATE EMAIL STATUS MESSAGES ....  

                    complete_email_status_string = " ... SMTP  E M A I L   S E N T  ... TIME = " + str(temp_time_string)

                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )

                    #print(str(complete_email_status_string) )
                                        
                    # except smtplib.SMTPException as smtp_exception: 
              except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

                    gmail_smtp_exceptions_status_global = True

                    gmail_smtp_SPECIFIC_EXCEPTION_global = "SMTPError"

                    self.entry_SOURCE_EMAIL_PASSWORD.set("")

                    complete_email_status_string = "SMTP  E M A I L   N O T   S E N T : Set ALLOW LESS SECURE APPS to (ON) ..... TIME = " + str(temp_time_string)

                    self.entry_EMAIL_STATUS.set(str(complete_email_status_string) )
                    
                    #print(str(complete_email_status_string) ) 

                    # open Write_Exception_Logfile() to append logfile to update the logfile items.
                    inst_Write_Exception_Logfile_for_smtp_send = Write_Exception_Logfile()
                    exception_logging_string_1 = " ... SMTP  E M A I L   N O T   S E N T  : Set ALLOW LESS SECURE APPS (ON) - EXCEPTION DETAILS FOLLOW: " + "\n"
                    exception_logging_string_3 = "\n\n"
                    
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_1) )
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_2) )
                    inst_Write_Exception_Logfile_for_smtp_send.log_exception(str(exception_logging_string_3) )

                    # Temporary command for debug that opens the exception logfile and prints the logfile 
                    # called fullpath_exception_logfile_global and prints the logfile contents acquire using read().
                    # We typically place this print of the exception logfile where exceptions are located for debug.

                    #with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
                    #    print(exception_file_handle_var.read() )

                    # logger.error(str(exception_logging_string), exc_info=True)

                    # Launch Messagebox Instructing How to set up Email when EMail Sending Fails.
                    self.launch_messagebox_when_email_fails()

                    #global gmail_oauth2_json_file_test_global
                    #global gmail_oauth2_status_global
                    #global gmail_oauth2_exceptions_status_global
                    #global gmail_oauth2_SPECIFIC_EXCEPTION_global
                    #global gmail_smtp_allow_less_secure_apps_global
                    #global gmail_smtp_status_global
                    #global gmail_smtp_exceptions_status_global
                    #global gmail_smtp_SPECIFIC_EXCEPTION_global


      def launch_messagebox_when_email_fails(self):
          messagebox.showinfo("Contact Manager Guide ...", \
          "............... ATTENTION: *********** USER ACTION REQUIRED ***********\n\nGMAIL ACCESS METHOD #1 - Must Set Online Switch to ALLOW LESS SECURE APPS:  (SMTP Gmail Mode)\n\nPlease VERIFY that your GMAIL SECURITY SETTINGS SWITCH is set to *** ALLOW LESS SECURE APPS *** as this will enable\nyour Gmail Account to SEND EMAIL from this Contact Management Application.\n\nTo SET the GMAIL SECURITY SWITCH to *** ALLOW LESS SECURE APPS = ON ***, login to your Gmail, and in a new Windows Window Tab, go to this LINK:\n\nhttps://myaccount.google.com/lesssecureapps\n\nand adjust the GMAIL SETTING to ALLOW LESS SECURE APPS = ON.\n\n \nGMAIL ACCESS METHOD #2 -   ADVANCED SECURITY GMAIL:  (OAUTH2 Gmail Mode)\n\nMAY REQUIRE SYSTEM ADMINISTRATOR TO PERFORM ACTIVATION OF THIS GMAIL FEATURE.\n\nTHE PROCEDURE TO ACTIVATE THIS APPLICATION FOR ADVANCED SECURITY OAUTH2 Gmail Mode is - YOU NEED TO LOGIN TO GMAIL AND THEN\nACQUIRE CREDENTIALS TO ALLOW THIS APPLICATION TO USE YOUR GMAIL ACCOUNT TO SEND GMAIL.\nCREDENTIALS ARE ACQUIRED AT THESE LINKS:   IMPORTANT - PLEASE NAME THE CLIENT:  Gmail API Python Quickstart.\n\nhttps://developers.google.com/gmail/api/quickstart/python\n\nhttps://console.developers.google.com/flows/enableapi?apiid=gmail\n\nTO ACQUIRE CREDENTIALS TO USE GMAIL, YOU MUST DOWNLOAD A DOT JSON FILE AND AFTER DOWNLOADING THAT FILE,\nRENAME THE FILE TO client_secret.json and COPY IT TO YOUR WORKING DIRECTORY.\n\nUpon Sending an EMail you will get a pop-up window asking you to login or approve use of your GMAIL Account by this Contact Management Application.\nThe indication that all is well is this message - The authentication flow has completed.\n\n\n..... Press OK to Continue .....\n\n(After you have completed this REQUIRED USER ACTION.)\n")

          

    
      
      def close_windows(self):
            global kick_thread_to_update_main_entry_widgets
            # update the main screen entry widgets
            # to be at the current focus dict index global
            kick_thread_to_update_main_entry_widgets = True
            self.master.destroy()



      
class Person(object):
      """
      This is the Person Class. 

      The Person Class is defined by the statement:  class Person(object): 

      The Person Class has the following attributes:

      self, firstname, lastname, streetadd, citytown, state, zipcode, phonenum, email, website

      """       
      def __init__(self, firstname, lastname, streetadd, citytown, state, zipcode, phonenum, email, website):
            self.firstname = firstname
            self.lastname = lastname
            self.streetadd = streetadd
            self.citytown = citytown
            self.state = state
            self.zipcode = zipcode
            self.phonenum = phonenum
            self.email = email
            self.website = website
            self.person_attribute_list = []
            self.pal = []



      person_attribute_list = ['firstname', 'lastname', 'streetadd', 'citytown', \
                                    'state', 'zipcode', 'phonenum', 'email', 'website']

      pal = ['firstname', 'lastname', 'streetadd', 'citytown', \
                  'state', 'zipcode', 'phonenum', 'email', 'website']

 
      def __name__(self):
            return 
      

      def __str__(self):
            return 'PERSON = ' + '[' + '\n' + 'FIRSTNAME = ' + str(self.firstname) + ', \n' + \
                  'LASTNAME = ' + str(self.lastname) + ', \n' + 'STREETADD = ' + str(self.streetadd) + ', \n' + \
                  'CITYTOWN = ' + str(self.citytown) + ', \n' + 'STATE = ' + str(self.state) + ', \n' + \
                  'ZIPCODE = ' + str(self.zipcode) + ', \n' + 'PHONENUM = ' + str(self.phonenum) + ', \n' + \
                  'EMAIL = ' + str(self.email) + ', \n' + 'WEBSITE = ' + str(self.website) + ', \n' + ']'

      def __repr__(self):
            return '[' + str(self.firstname) + ',' + str(self.lastname) + ',' + str(self.streetadd) + ',' + \
                  str(self.citytown) + ',' + str(self.state) + ',' + str(self.zipcode) + ',' + \
                  str(self.phonenum) + ',' + str(self.email) + ',' + str(self.website) + ',' + ']'
   

      def get_Firstname(self):
            return self.firstname

      def get_Lastname(self):
            return self.lastname

      def get_Streetadd(self):
            return self.streetadd

      def get_Citytown(self):
            return self.citytown

      def get_State(self):
            return self.state

      def get_Zipcode(self):
            return self.zipcode

      def get_Phonenum(self):
            return self.phonenum

      def get_Email(self):
            return self.email

      def get_Website(self):
            return self.website


#########################################################


      def set_Firstname(self, newFirstname):
            self.firstname = newFirstname

      def set_Lastname(self, newLastname):
            self.lastname = new

      def set_Streetadd(self, newStreetadd):
            self.streetadd = newStreetadd

      def set_Citytown(self, newCitytown):
            self.citytown = newCitytown

      def set_State(self, newState):
            self.state = newState

      def set_Zipcode(self, newZipcode):
            self.zipcode = newZipcode

      def set_Phonenum(self, newPhonenum):
            self.phonenum = newPhonenum

      def set_Email(self, newEmail):
            self.email = newEmail

      def set_Website(self, newWebsite):
            self.website = newWebsite
            



        
#######################################################################################
#
# IMPLEMENT APPLICATION STATUS SCREEN for Contact Management Application Functions. 
#
#######################################################################################
#
class App_Status_Class(Frame):    #( object)
    def __init__(self, master=None):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global valid_client_secret_key_format_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Contact Management Software - Application Status")
        #self.master = master 
        #self.frame = tk.Frame(self.master)
        
        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed') 


        self.Frame1 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame1.grid(row = 0, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame2 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame2.grid(row = 4, column = 0, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        self.Frame3 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame3.grid(row = 0, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame4 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame4.grid(row = 4, column = 1, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        self.Frame5 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame5.grid(row = 0, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame6 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame6.grid(row = 4, column = 2, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        
        self.Frame7 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame7.grid(row = 0, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)
        self.Frame8 = tk.Frame(self.master, bg=str(config_bg_color_val_global), borderwidth = 0, highlightthickness = 10, highlightbackground="light sea green", highlightcolor="light sea green")
        self.Frame8.grid(row = 4, column = 3, rowspan = 4, columnspan = 1, padx=5, pady=5, sticky = W+E+N+S)

        # Instantiate GMAIL OAUTH2 Status Buttons
        for r in range(4):
            self.Frame1.rowconfigure(r, weight=1)    
            self.Frame1.columnconfigure(0, weight=1)

        self.oauth2_json_file_test_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nJSON FILE STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_json_file_test_Button.grid(row=0, column=0, padx=5, pady=5)
        self.oauth2_json_file_test_Button.config(borderwidth=5)

        self.oauth2_status_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nOAUTH2 EMAIL SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_status_Button.grid(row=1, column=0, padx=5, pady=5)
        self.oauth2_status_Button.config(borderwidth=5)
        
        self.oauth2_exceptions_Button = Button(self.Frame1, text = "GMAIL OAUTH2\nOAUTH2 EMAIL NOT SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_exceptions_Button.grid(row=2, column=0, padx=5, pady=5)
        self.oauth2_exceptions_Button.config(borderwidth=5)

        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button = Button(self.Frame1, text = str(gmail_oauth2_SPECIFIC_EXCEPTION_global), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.grid(row=3, column=0, padx=5, pady=5)
        self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(borderwidth=5)

        # Instantiate GMAIL SMTP Status Buttons
        for r in range(4):
            self.Frame2.rowconfigure(r, weight=1)    
            self.Frame2.columnconfigure(0, weight=1)

        self.smtp_allow_less_secure_apps_Button = Button(self.Frame2, text = "GMAIL SMTP SWITCH\nALLOW LESS SECURE APPS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_allow_less_secure_apps_Button.grid(row=4, column=0, padx=5, pady=5)
        self.smtp_allow_less_secure_apps_Button.config(borderwidth=5)

        self.smtp_status_Button = Button(self.Frame2, text = "GMAIL SMTP\nSMTP EMAIL SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_status_Button.grid(row=5, column=0, padx=5, pady=5)
        self.smtp_status_Button.config(borderwidth=5)
        
        self.smtp_exceptions_Button = Button(self.Frame2, text = "GMAIL SMTP\nSMTP NOT SENT", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_exceptions_Button.grid(row=6, column=0, padx=5, pady=5)
        self.smtp_exceptions_Button.config(borderwidth=5)
        
        # NOTE: This is the Exception Name that applies here: "SMTPAuthenticationError"
        
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button = Button(self.Frame2, text = str(gmail_smtp_SPECIFIC_EXCEPTION_global), \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button.grid(row=7, column=0, padx=5, pady=5)
        self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(borderwidth=5)

        # Instantiate Thread Status Buttons  
        for r in range(4):
            self.Frame3.rowconfigure(r, weight=1)    
            self.Frame3.columnconfigure(1, weight=1)

        self.MainThread_THREAD_Button = Button(self.Frame3, text = "MainThread\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.MainThread_THREAD_Button.grid(row=0, column=1, padx=5, pady=5)
        self.MainThread_THREAD_Button.config(borderwidth=5)

        self.main_Class_cm_app_THREAD_Button = Button(self.Frame3, text = "main_Class_cm_app_THREAD\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.main_Class_cm_app_THREAD_Button.grid(row=1, column=1, padx=5, pady=5)
        self.main_Class_cm_app_THREAD_Button.config(borderwidth=5)
        
        self.App_Status_Class_THREAD_Button = Button(self.Frame3, text = "App_Status_Class_THREAD\nTHREAD STATUS", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.App_Status_Class_THREAD_Button.grid(row=2, column=1, padx=5, pady=5)
        self.App_Status_Class_THREAD_Button.config(borderwidth=5)

        self.contact_management_spare_1_Button = Button(self.Frame3, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_spare_1_Button.grid(row=3, column=1, padx=5, pady=5)
        self.contact_management_spare_1_Button.config(borderwidth=5)


        for r in range(4):
            bottom_rows = int(r + 4)
            self.Frame4.rowconfigure(bottom_rows, weight=1)    
            self.Frame4.columnconfigure(1, weight=1)

            self.status_Button_N = Button(self.Frame4, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=bottom_rows, column=1, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        for r in range(4):
            self.Frame5.rowconfigure(r, weight=1)    
            self.Frame5.columnconfigure(2, weight=1)

            self.status_Button_N = Button(self.Frame5, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=r, column=2, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        for r in range(4):
            bottom_rows = int(r + 4)
            self.Frame6.rowconfigure(bottom_rows, weight=1)    
            self.Frame6.columnconfigure(2, weight=1)

            self.status_Button_N = Button(self.Frame6, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=bottom_rows, column=2, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        for r in range(4):
            self.Frame7.rowconfigure(r, weight=1)    
            self.Frame7.columnconfigure(3, weight=1)

            self.status_Button_N = Button(self.Frame7, text = "CONTACT MANAGEMENT\nSTATUS SPARE", width = 26, height = 2, \
                    font=('Helvetica', '12'), background="ivory4", fg="black")
        
            self.status_Button_N.grid(row=r, column=3, padx=5, pady=5)
            self.status_Button_N.config(borderwidth=5)


        # Instantiate Frame8 to implement status panel reset.
        for r in range(4):
            self.Frame8.rowconfigure(r, weight=1)    
            self.Frame8.columnconfigure(3, weight=1)

        self.contact_management_frame8_spare_1_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_1_Button.grid(row=4, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_1_Button.config(borderwidth=5)

        self.contact_management_frame8_spare_2_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_2_Button.grid(row=5, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_2_Button.config(borderwidth=5)
        
        self.contact_management_frame8_spare_3_Button = Button(self.Frame8, text = "CONTACT MANAGEMENT\nSTATUS SPARE", \
            width = 26, height = 2, font=('Helvetica', '12'), background="ivory4", fg="black")
        self.contact_management_frame8_spare_3_Button.grid(row=6, column=3, padx=5, pady=5)
        self.contact_management_frame8_spare_3_Button.config(borderwidth=5)
        
        # NOTE: This is currently the STATUS PANEL RESET BUTTON.
        
        self.status_panel_reset_Button = Button(self.Frame8, text = "STATUS PANEL\nRESET BUTTON", \
            width = 26, height = 2, font=('Helvetica', '12'), background="Midnight Blue", \
            fg="deep sky blue", command = self.reset_status_panel_method)
        self.status_panel_reset_Button.grid(row=7, column=3, padx=5, pady=5)
        self.status_panel_reset_Button.config(borderwidth=5)

            
        ##########################################################
        #
        # Create and Initialize Thread Status Variables 
        #
        ##########################################################

        self.thread_list = []
        
        self.MainThread_THREAD_status = False
        self.main_Class_cm_app_THREAD_status = False
        self.App_Status_Class_THREAD_status = False
            

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')


        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

        self.master.configure(background=str(config_bg_color_val_global) )

        # call method to update the app status panel widgets
        self.update_app_status_panel()


        
    def _update_app_status_panel(self): 
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global valid_client_secret_key_format_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global

        while 1:

            # set the value of the client_secret.json validation status
            # determined after validation prcoessing in  main()    

            gmail_oauth2_json_file_test_global = valid_client_secret_key_format_global

            if gmail_oauth2_json_file_test_global == True:
                self.oauth2_json_file_test_Button.config(background="light sea green", fg="black")
            elif gmail_oauth2_json_file_test_global == False:
                self.oauth2_json_file_test_Button.config(background="red2", fg="black")
            elif gmail_oauth2_json_file_test_global == None:
                self.oauth2_json_file_test_Button.config(background="ivory4", fg="black")
                

            if gmail_oauth2_status_global == True:
                self.oauth2_status_Button.config(background="light sea green", fg="black")
            elif gmail_oauth2_status_global == False:
                self.oauth2_status_Button.config(background="red2", fg="black")
            elif gmail_oauth2_status_global == None:
                self.oauth2_status_Button.config(background="ivory4", fg="black")


            if gmail_oauth2_exceptions_status_global == True:
                self.oauth2_exceptions_Button.config(background="red2", fg="black")
            elif gmail_oauth2_exceptions_status_global == False:
                self.oauth2_exceptions_Button.config(background="ivory4", fg="black")
            elif gmail_oauth2_exceptions_status_global == None:
                self.oauth2_exceptions_Button.config(background="ivory4", fg="black")


            if gmail_oauth2_SPECIFIC_EXCEPTION_global == "Specific_OAUTH2_Exception":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="ivory4", fg="black")
            elif gmail_oauth2_SPECIFIC_EXCEPTION_global == "FileNotFoundError":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="red2", fg="black")
            elif gmail_oauth2_SPECIFIC_EXCEPTION_global == "ClientSecretValidationError":
                self.oauth2_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_oauth2_SPECIFIC_EXCEPTION_global), background="red2", fg="black")


            if gmail_smtp_allow_less_secure_apps_global == True:
                self.smtp_allow_less_secure_apps_Button.config(background="light sea green", fg="black")
            elif gmail_smtp_allow_less_secure_apps_global == False:
                self.smtp_allow_less_secure_apps_Button.config(background="red2", fg="black")
            elif gmail_smtp_allow_less_secure_apps_global == None:
                self.smtp_allow_less_secure_apps_Button.config(background="ivory4", fg="black")


            if gmail_smtp_status_global == True:
                self.smtp_status_Button.config(background="light sea green", fg="black")
            elif gmail_smtp_status_global == False:
                self.smtp_status_Button.config(background="red2", fg="black")
            elif gmail_smtp_status_global == None:
                self.smtp_status_Button.config(background="ivory4", fg="black")


            if gmail_smtp_exceptions_status_global == True:
                self.smtp_exceptions_Button.config(background="red2", fg="black")
            elif gmail_smtp_exceptions_status_global == False:
                self.smtp_exceptions_Button.config(background="ivory4", fg="black")
            elif gmail_smtp_exceptions_status_global == None:
                self.smtp_exceptions_Button.config(background="ivory4", fg="black")

            # NOTE: This is the Exception Name that applies here: "SMTPAuthenticationError" 

            if gmail_smtp_SPECIFIC_EXCEPTION_global == "Specific_SMTP_Exception":
                self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(text=str(gmail_smtp_SPECIFIC_EXCEPTION_global),  background="ivory4", fg="black")
            elif gmail_smtp_SPECIFIC_EXCEPTION_global == "SMTPError":
                self.smtp_SPECIFIC_EXCEPTION_NAME_Button.config(text="SMTPAuthenticationError",  background="red2", fg="black")

            # when the status panel tk window, class App_Status_Class, and method update_app_status_panel
            # is active, monitor and display all active threads and display each thread status on status panel. 

            for thread in threading.enumerate():

                # ADD thread.name TO LIST IF thread.name IS NOT IN LIST
                if thread.name not in self.thread_list:
                    self.thread_list.append(thread.name)

                if thread.name == "MainThread":
                    self.MainThread_THREAD_status = True

                elif thread.name == "main_Class_cm_app_THREAD":
                    self.main_Class_cm_app_THREAD_status = True

                elif thread.name == "App_Status_Class_THREAD":
                    self.App_Status_Class_THREAD_status = True

                else:
                    pass
    
                #print("\n") 
                #print(".... THREAD ENUMERATION - THREAD NAMES: ")
                #print(thread.name)

            #print("\n")
            #print(".... LIST OF THREADS: ")
            #print(self.thread_list)


            if self.MainThread_THREAD_status == True:
                self.MainThread_THREAD_Button.config(background="light sea green", fg="black")
            elif self.MainThread_THREAD_status == False:
                self.MainThread_THREAD_Button.config(background="red2", fg="black")
            elif self.MainThread_THREAD_status == None:
                self.MainThread_THREAD_Button.config(background="ivory4", fg="black")

            if self.main_Class_cm_app_THREAD_status == True:
                self.main_Class_cm_app_THREAD_Button.config(background="light sea green", fg="black")
            elif self.main_Class_cm_app_THREAD_status == False:
                self.main_Class_cm_app_THREAD_Button.config(background="red2", fg="black")
            elif self.main_Class_cm_app_THREAD_status == None:
                self.main_Class_cm_app_THREAD_Button.config(background="ivory4", fg="black")

            if self.App_Status_Class_THREAD_status == True:
                self.App_Status_Class_THREAD_Button.config(background="light sea green", fg="black")
            if self.App_Status_Class_THREAD_status == False:
                self.App_Status_Class_THREAD_Button.config(background="red2", fg="black")
            if self.App_Status_Class_THREAD_status == None:
                self.App_Status_Class_THREAD_Button.config(background="ivory4", fg="black")
            
            # Since this method is looping (or threaded) we manage the CPU resources
            # consumed by this method with time.sleep()
            time.sleep(.5)


    ################################################################################
    #
    # Threading INSIDE a Class: 
    #
    # def func_to_be_threaded(self):
    #     threading.Thread(target=self._func_to_be_threaded).start()
    # 
    ################################################################################


    def update_app_status_panel(self):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global gmail_logged_in_global
        global cm_dict_file_startup_test_global
        global cm_csv_file_startup_test_global
        global cm_notes_file_startup_test_global
        
        t_thread_1 = threading.Thread(name="App_Status_Class_THREAD", target=self._update_app_status_panel, daemon=True)
        t_thread_1.start()



    def reset_status_panel_method(self):
        global gmail_oauth2_json_file_test_global
        global gmail_oauth2_status_global
        global gmail_oauth2_exceptions_status_global
        global gmail_oauth2_SPECIFIC_EXCEPTION_global
        global gmail_smtp_allow_less_secure_apps_global
        global gmail_smtp_status_global
        global gmail_smtp_exceptions_status_global
        global gmail_smtp_SPECIFIC_EXCEPTION_global
        global valid_client_secret_key_format_global

        self.MainThread_THREAD_status = None
        self.main_Class_cm_app_THREAD_status = None
        self.App_Status_Class_THREAD_status = None

        gmail_oauth2_json_file_test_global = None
        gmail_oauth2_status_global = None
        gmail_oauth2_exceptions_status_global = None
        gmail_oauth2_SPECIFIC_EXCEPTION_global = "Specific_OAUTH2_Exception"
        gmail_smtp_allow_less_secure_apps_global = None
        gmail_smtp_status_global = None
        gmail_smtp_exceptions_status_global = None
        gmail_smtp_SPECIFIC_EXCEPTION_global = "Specific_SMTP_Exception"
        valid_client_secret_key_format_global = None
        



#######################################################################################
#        
# IMPLEMENT app_config.ini SETTING ..... 
#
# FIRST CONFIG ITEM - ENTER TKINTER COLOR NAMES IN A TEXTBOX FOR EACH CONFIG ITEM
#
#######################################################################################
#
class Config_Setting_Class(Frame):    #( object)
    def __init__(self, master=None):
        global listbox_color_value_global
        global listbox_color_moment_global
        global request_mainscreen_config_update_global
        global cm_listbox_file_global
        global dict_filename_global
        global master_cm_list_name_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_app_config_ini_global
        global mainscreen_bg_color_val_global
        global mainscreen_bg_color_val_global
        global viewscreen_bg_color_val_global
        global selectlist_bg_color_val_global
        global newlist_bg_color_val_global
        global usermanual_bg_color_val_global
        global config_bg_color_val_global
        global mainscreen_fg_color_val_global
        global viewscreen_fg_color_val_global
        global selectlist_fg_color_val_global
        global newlist_fg_color_val_global
        global usermanual_fg_color_val_global
        global config_fg_color_val_global
        global app_config_ini_val_global
        global app_config_request_global
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Contact Management Software - Application Configuration Command Center")
        #self.master = master
        #self.frame = tk.Frame(self.master)


        for r in range(12):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)


        # FIVE COLUMN FRAMES - EACH WITH TWELVE ROWS
        self.Frame1 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame1.grid(row = 0, column = 0, rowspan = 12, columnspan = 1, sticky = W+E+N+S) 
        self.Frame2 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame2.grid(row = 0, column = 1, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame3 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame3.grid(row = 0, column = 2, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame4 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame4.grid(row = 0, column = 3, rowspan = 12, columnspan = 1, sticky = W+E+N+S)
        self.Frame5 = tk.Frame(self.master, bg=str(config_bg_color_val_global))
        self.Frame5.grid(row = 0, column = 4, rowspan = 12, columnspan = 1, sticky = W+E+N+S)


        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")

###########################################################################################
        
        self.master.configure(background=str(config_bg_color_val_global) )
        

        self.select_file_button = Button(self.master, text = "C L I C K   H E R E\nto SAVE your Settings.", width=18,height=2, font=('Helvetica', '18'), background="goldenrod", fg="black")

        self.select_file_button.grid(row=0, column=0, sticky = NW)
        self.select_file_button.bind("<Button-1>", self.get_Config_Textbox_Settings)
        

        self.select_listbox_color_button = Button(self.Frame4, text = "SELECT COLOR from LISTBOX,\nthen TOUCH BUTTONS to the LEFT\nto SET corresponding SCREEN COLOR", \
            width=32,height=3, font=('Helvetica', '12'), background="goldenrod", fg="black")
            
        self.select_listbox_color_button.grid(row=0, column=3, sticky = N)


        self.show_instructions1_button = Button(self.master, text = "\nBackground", width=15,height=2, font=('Helvetica', '18'), background="turquoise4", fg="black")
            
        self.show_instructions1_button.grid(row=0, column=1, sticky = NW)

        self.show_instructions2_button = Button(self.master, text = "\nForeground", width=15,height=2, font=('Helvetica', '18'), background="turquoise4", fg="black")
            
        self.show_instructions2_button.grid(row=0, column=2, sticky = NW)

        
        self.quitButton = Button(self.master, text = 'CLICK HERE to\nReturn to Main Screen\nWILL NOT Save Settings', width = 20, height = 3, \
                                 font=('Helvetica', '16'), background="goldenrod", fg="black", command = self.close_windows)
        
        self.quitButton.grid(row=8, column=0, sticky = SW)


############################################################################################### 
 
        # LABEL FOR NEW MAINSCREEN BACKGROUND
        self.label_main_bg = "MAIN SCREEN:"
        self.my_main_bg_label = Label(self.master, text = self.label_main_bg, font=large_font)
        self.my_main_bg_label.config(height = 1, width=15, anchor = E)
        self.my_main_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_main_bg_label.grid(row=1, column=0, sticky = N)

        # LABEL FOR VIEW CONTACTS BACKGROUND
        self.label_view_bg = "VIEW CONTACTS:"
        self.my_view_bg_label = Label(self.master, text = self.label_view_bg, font=large_font)
        self.my_view_bg_label.config(height = 1, width=15, anchor = E)
        self.my_view_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_view_bg_label.grid(row=2, column=0, sticky = N)

        # LABEL FOR SELECT LIST BACKGROUND
        self.label_select_bg = "SELECT LIST:"
        self.my_select_bg_label = Label(self.master, text = self.label_select_bg, font=large_font)
        self.my_select_bg_label.config(height = 1, width=15, anchor = E)
        self.my_select_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_select_bg_label.grid(row=3, column=0, sticky = N)

        # LABEL FOR NEW LIST BACKGROUND
        self.label_newlist_bg = "NEW LIST:"
        self.my_newlist_bg_label = Label(self.master, text = self.label_newlist_bg, font=large_font)
        self.my_newlist_bg_label.config(height = 1, width=15, anchor = E)
        self.my_newlist_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_newlist_bg_label.grid(row=4, column=0, sticky = N)

        # LABEL FOR USERS MANUAL BACKGROUND
        self.label_user_bg = "USERS MANUAL:"
        self.my_user_bg_label = Label(self.master, text = self.label_user_bg, font=large_font)
        self.my_user_bg_label.config(height = 1, width=15, anchor = E)
        self.my_user_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_user_bg_label.grid(row=5, column=0, sticky = N)

        # LABEL FOR APP CONFIG BACKGROUND
        self.label_conf_bg = "APP CONFIG:"
        self.my_conf_bg_label = Label(self.master, text = self.label_conf_bg, font=large_font)
        self.my_conf_bg_label.config(height = 1, width=15, anchor = E)
        self.my_conf_bg_label.config(bg='light sea green', fg='gray25')  
        self.my_conf_bg_label.grid(row=6, column=0, sticky = N)

############################################################################################### 

        ##########################################################################################
        #
        # When the button is pressed, the listbox_color_moment_global selected will change
        # the color of the button widget and generate the color setting variables and globals
        # that gets saved to update the config and the corresponding screen's: 
        #   
        # 1. background   2. foreground   3. buttons   4. entry/text/list boxes
        # 
        # This will be implemented with the .config function located within the
        #
        # listbox_color_moment_global selection method: OnListBoxSelect(self, event)
        #
        ##########################################################################################
        
        self.main_bg_color_moment_button = Button(self.master, text = str(mainscreen_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(mainscreen_bg_color_val_global))
        self.main_bg_color_moment_button.grid(row=1, column=1, sticky = NW)
        self.main_bg_color_moment_button.bind("<Button-1>", self.main_bg_set_color_variables)

        self.view_bg_color_moment_button = Button(self.master, text = str(viewscreen_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(viewscreen_bg_color_val_global))
        self.view_bg_color_moment_button.grid(row=2, column=1, sticky = NW)
        self.view_bg_color_moment_button.bind("<Button-1>", self.view_bg_set_color_variables)

        self.select_bg_color_moment_button = Button(self.master, text = str(selectlist_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(selectlist_bg_color_val_global))
        self.select_bg_color_moment_button.grid(row=3, column=1, sticky = NW)
        self.select_bg_color_moment_button.bind("<Button-1>", self.select_bg_set_color_variables)

        self.newlist_bg_color_moment_button = Button(self.master, text = str(newlist_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(newlist_bg_color_val_global))
        self.newlist_bg_color_moment_button.grid(row=4, column=1, sticky = NW)
        self.newlist_bg_color_moment_button.bind("<Button-1>", self.newlist_bg_set_color_variables)

        self.usermanual_bg_color_moment_button = Button(self.master, text = str(usermanual_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(usermanual_bg_color_val_global))
        self.usermanual_bg_color_moment_button.grid(row=5, column=1, sticky = NW)
        self.usermanual_bg_color_moment_button.bind("<Button-1>", self.usermanual_bg_set_color_variables)

        self.config_bg_color_moment_button = Button(self.master, text = str(config_bg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(config_bg_color_val_global))
        self.config_bg_color_moment_button.grid(row=6, column=1, sticky = NW)
        self.config_bg_color_moment_button.bind("<Button-1>", self.config_bg_set_color_variables)

        ##########################################################################################

        self.main_fg_color_moment_button = Button(self.master, text = str(mainscreen_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(mainscreen_fg_color_val_global))
        self.main_fg_color_moment_button.grid(row=1, column=2, sticky = NW)
        self.main_fg_color_moment_button.bind("<Button-1>", self.main_fg_set_color_variables)

        self.view_fg_color_moment_button = Button(self.master, text = str(viewscreen_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(viewscreen_fg_color_val_global))
        self.view_fg_color_moment_button.grid(row=2, column=2, sticky = NW)
        self.view_fg_color_moment_button.bind("<Button-1>", self.view_fg_set_color_variables)

        self.select_fg_color_moment_button = Button(self.master, text = str(selectlist_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(selectlist_fg_color_val_global))
        self.select_fg_color_moment_button.grid(row=3, column=2, sticky = NW)
        self.select_fg_color_moment_button.bind("<Button-1>", self.select_fg_set_color_variables)

        self.newlist_fg_color_moment_button = Button(self.master, text = str(newlist_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(newlist_fg_color_val_global))
        self.newlist_fg_color_moment_button.grid(row=4, column=2, sticky = NW)
        self.newlist_fg_color_moment_button.bind("<Button-1>", self.newlist_fg_set_color_variables)

        self.usermanual_fg_color_moment_button = Button(self.master, text = str(usermanual_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(usermanual_fg_color_val_global))
        self.usermanual_fg_color_moment_button.grid(row=5, column=2, sticky = NW)
        self.usermanual_fg_color_moment_button.bind("<Button-1>", self.usermanual_fg_set_color_variables)

        self.config_fg_color_moment_button = Button(self.master, text = str(config_fg_color_val_global), \
            width=17,height=1, font=('Helvetica', '12'), background=str(config_fg_color_val_global))
        self.config_fg_color_moment_button.grid(row=6, column=2, sticky = NW)
        self.config_fg_color_moment_button.bind("<Button-1>", self.config_fg_set_color_variables)

        ##########################################################################################

        self.seeColors = Text(self.Frame4, width=18, height=4)
        self.seeColors.grid(row=12, column=3, sticky = SW)
        self.seeColors.config(borderwidth=12, font=('Helvetica', '20'), background="light sea green")

        self.lbox = Listbox(self.Frame4, width=18, height=12)
        self.lbox.grid(row=10, column=3, sticky = SW)
        self.lbox.config(borderwidth=10, font=('Helvetica', '20'), background="light sea green", fg = "gray18") 
        self.lbox.bind("<<ListboxSelect>>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.Frame4, command=self.lbox.yview)
        self.scrollb.grid(row=10, column=3, sticky='NSE')
        self.lbox['yscrollcommand'] = self.scrollb.set

        List_of_Colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
            'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
            'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
            'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
            'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
            'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
            'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
            'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
            'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
            'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
            'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown',
            'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
            'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
            'pale violet red', 'maroon', 'medium violet red', 'violet red',
            'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
            'thistle', 'snow2', 'snow3',
            'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
            'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
            'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
            'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
            'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
            'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
            'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
            'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
            'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
            'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
            'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
            'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
            'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
            'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
            'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
            'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
            'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
            'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
            'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
            'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
            'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
            'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
            'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
            'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
            'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
            'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
            'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
            'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
            'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
            'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
            'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
            'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
            'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
            'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
            'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
            'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
            'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
            'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
            'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
            'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
            'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


        # Load all COLORS in LIST into the LISTBOX 
        results = []
        reversed_list = []

        # reverse the list so grays are not at beginning of LISTBOX
        reversed_list = list(reversed(List_of_Colors))

        for color in reversed_list:
              results.append(color)
              
        for color_item in results:
              self.lbox.insert(0, color_item)
              

              
    def main_bg_set_color_variables(self, event):
          global mainscreen_bg_color_val_global
          global request_mainscreen_config_update_global
          mainscreen_bg_color_val_global = listbox_color_moment_global
          self.main_bg_color_moment_button.config(text = str(mainscreen_bg_color_val_global), bg = str(mainscreen_bg_color_val_global) )
          #
          # UPDATE MAINSCREEN BACKGROUND COLOR:
          #
          # Set this request_mainscreen_config_update_global GLOBAL to True 
          # to enable the IF statement in the main THREAD to perform
          # the command:
          #
          #      cm_app.config(background = str(mainscreen_bg_color_val_global)
          #
          request_mainscreen_config_update_global = True
          #
          ##########################################################################


    def view_bg_set_color_variables(self, event):
          global viewscreen_bg_color_val_global
          viewscreen_bg_color_val_global = listbox_color_moment_global
          self.view_bg_color_moment_button.config(text = str(viewscreen_bg_color_val_global), bg = str(viewscreen_bg_color_val_global) )
          

    def select_bg_set_color_variables(self, event):
          global selectlist_bg_color_val_global
          selectlist_bg_color_val_global = listbox_color_moment_global
          self.select_bg_color_moment_button.config(text = str(selectlist_bg_color_val_global), bg = str(selectlist_bg_color_val_global) )
          
    
    def newlist_bg_set_color_variables(self, event):
          global newlist_bg_color_val_global
          newlist_bg_color_val_global = listbox_color_moment_global
          self.newlist_bg_color_moment_button.config(text = str(newlist_bg_color_val_global), bg = str(newlist_bg_color_val_global) )
          

    def usermanual_bg_set_color_variables(self, event):
          global usermanual_bg_color_val_global
          usermanual_bg_color_val_global = listbox_color_moment_global
          self.usermanual_bg_color_moment_button.config(text = str(usermanual_bg_color_val_global), bg = str(usermanual_bg_color_val_global) )
          
    
    def config_bg_set_color_variables(self, event):
          global config_bg_color_val_global
          config_bg_color_val_global = listbox_color_moment_global
          self.config_bg_color_moment_button.config(text = str(config_bg_color_val_global), bg = str(config_bg_color_val_global) )


    def main_fg_set_color_variables(self, event):
          global mainscreen_fg_color_val_global
          mainscreen_fg_color_val_global = listbox_color_moment_global
          self.main_fg_color_moment_button.config(text = str(mainscreen_fg_color_val_global), bg = str(mainscreen_fg_color_val_global) )


    def view_fg_set_color_variables(self, event):
          global viewscreen_fg_color_val_global
          viewscreen_fg_color_val_global = listbox_color_moment_global
          self.view_fg_color_moment_button.config(text = str(viewscreen_fg_color_val_global), bg = str(viewscreen_fg_color_val_global) )
          

    def select_fg_set_color_variables(self, event):
          global selectlist_fg_color_val_global
          selectlist_fg_color_val_global = listbox_color_moment_global
          self.select_fg_color_moment_button.config(text = str(selectlist_fg_color_val_global), bg = str(selectlist_fg_color_val_global) )
          
    
    def newlist_fg_set_color_variables(self, event):
          global newlist_fg_color_val_global
          newlist_fg_color_val_global = listbox_color_moment_global
          self.newlist_fg_color_moment_button.config(text = str(newlist_fg_color_val_global), bg = str(newlist_fg_color_val_global) )
          

    def usermanual_fg_set_color_variables(self, event):
          global usermanual_fg_color_val_global
          usermanual_fg_color_val_global = listbox_color_moment_global
          self.usermanual_fg_color_moment_button.config(text = str(usermanual_fg_color_val_global), bg = str(usermanual_fg_color_val_global) )
          
    
    def config_fg_set_color_variables(self, event):
          global config_fg_color_val_global
          config_fg_color_val_global = listbox_color_moment_global
          self.config_fg_color_moment_button.config(text = str(config_fg_color_val_global), bg = str(config_fg_color_val_global) )
          


    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        global listbox_color_moment_global
        listbox_file_capture_global = "False"
        widget = event.widget
        selection = widget.curselection()
        listbox_color_value = widget.get(selection[0])
        listbox_color_moment_global = widget.get(selection[0])
        selection_value_tuple = [selection, listbox_color_value]
        # Change the COLOR in the Text Widget for the Viewer
        self.seeColors.config(background=str(listbox_color_value) )
        return listbox_color_value



    def close_windows(self):
        self.master.destroy()

 

    #########################################################################################
    #
    #  Use the command = func_set_xxxx_bg_textbox feature in Options Menu to acquire the
    #  xxxx_opt_menu_bg_select StringVar with the selected COLOR, then use the
    #  self.entry_xxxx_bg.set(str(xxxxscreen_bg_color_val_global) ) to set the xxxx TEXTBOX
    #  to the COLOR string value, and finally, a ways below, in get_Config_Textbox_Settings,
    #  use the self.my_xxxx_screen_bg_entry.get() to set the new COLOR value for both the
    #  GLOBAL and the app_config.ini value.   
    # 
    ######################################################################################### 
          
    def func_set_main_bg_global(self, main_opt_menu_bg_select):
          global mainscreen_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_main_bg_global feature in Options Menu to get   C O L O R  =  " + str(main_opt_menu_bg_select) )
          mainscreen_bg_color_val_global = str(main_opt_menu_bg_select)

          
    def func_set_view_bg_global(self, view_opt_menu_bg_select):
          global viewscreen_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_view_bg_global feature in Options Menu to get   C O L O R  =  " + str(view_opt_menu_bg_select) )
          viewscreen_bg_color_val_global = str(view_opt_menu_bg_select)
           

    def func_set_select_bg_global(self, select_opt_menu_bg_select):
          global selectlist_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_select_bg_global feature in Options Menu to get   C O L O R  =  " + str(select_opt_menu_bg_select) )
          selectlist_bg_color_val_global = str(select_opt_menu_bg_select)


    def func_set_newlist_bg_global(self, newlist_opt_menu_bg_select):
          global newlist_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_bg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_bg_select) )
          newlist_bg_color_val_global = str(newlist_opt_menu_bg_select)


    def func_set_usermanual_bg_global(self, usermanual_opt_menu_bg_select):
          global usermanual_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_usermanual_bg_global feature in Options Menu to get   C O L O R  =  " + str(usermanual_opt_menu_bg_select) )
          usermanual_bg_color_val_global = str(usermanual_opt_menu_bg_select)


    def func_set_config_bg_global(self, config_opt_menu_bg_select):
          global config_bg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_config_bg_global feature in Options Menu to get   C O L O R  =  " + str(config_opt_menu_bg_select) )
          config_bg_color_val_global = str(config_opt_menu_bg_select)
          

#########################################################################################

    def func_set_main_fg_global(self, main_opt_menu_fg_select):
          global mainscreen_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_main_fg_global feature in Options Menu to get   C O L O R  =  " + str(main_opt_menu_fg_select) )
          mainscreen_fg_color_val_global = str(main_opt_menu_fg_select)

    def func_set_view_fg_global(self, view_opt_menu_fg_select):
          global viewscreen_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_view_fg_global feature in Options Menu to get   C O L O R  =  " + str(view_opt_menu_fg_select) )
          viewscreen_fg_color_val_global = str(view_opt_menu_fg_select)

    def func_set_select_fg_global(self, select_opt_menu_fg_select):
          global selectlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_select_fg_global feature in Options Menu to get   C O L O R  =  " + str(select_opt_menu_fg_select) )
          selectlist_fg_color_val_global = str(select_opt_menu_fg_select)

    def func_set_newlist_fg_global(self, newlist_opt_menu_fg_select):
          global newlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_fg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_fg_select) )
          newlist_fg_color_val_global = str(newlist_opt_menu_fg_select)

    def func_set_newlist_fg_global(self, newlist_opt_menu_fg_select):
          global newlist_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_newlist_fg_global feature in Options Menu to get   C O L O R  =  " + str(newlist_opt_menu_fg_select) )
          newlist_fg_color_val_global = str(newlist_opt_menu_fg_select)

    def func_set_usermanual_fg_global(self, usermanual_opt_menu_fg_select):
          global usermanual_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_usermanual_fg_global feature in Options Menu to get   C O L O R  =  " + str(usermanual_opt_menu_fg_select) )
          usermanual_fg_color_val_global = str(usermanual_opt_menu_fg_select)

    def func_set_config_fg_global(self, config_opt_menu_fg_select):
          global config_fg_color_val_global
          # #print("\n")
          # #print(".... USE of command = func_set_config_fg_global feature in Options Menu to get   C O L O R  =  " + str(config_opt_menu_fg_select) )
          config_fg_color_val_global = str(config_opt_menu_fg_select)

          
#########################################################################################

     

    def get_Config_Textbox_Settings(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_app_config_ini_global
        global mainscreen_bg_color_val_global
        global viewscreen_bg_color_val_global
        global selectlist_bg_color_val_global
        global newlist_bg_color_val_global
        global usermanual_bg_color_val_global
        global config_bg_color_val_global
        global mainscreen_fg_color_val_global
        global viewscreen_fg_color_val_global
        global selectlist_fg_color_val_global
        global newlist_fg_color_val_global
        global usermanual_fg_color_val_global
        global config_fg_color_val_global
        global app_config_ini_val_global 
        global app_config_request_global
        ###########################################################################
        #
        # This button command gets the CONFIG VALUE from the respective
        # Config_Setting_Class OptionsMenu Selections, already upadted as
        # the corresponding CONFIG VALUE GLOBAL and then updates the
        # CONFIG INI FILE called app_config.ini
        #
        ###########################################################################
        #
        #   ******* setting NEW config settings get written here *******
        #   *******    triggered by config button    ******* 
        #
        ###########################################################################
        #
        # config settings here come from OptionsMenu Selections above where
        # the corresponding global has been set from the OptionsMenu Selections.
        #
        ###########################################################################

        # #print("\n")
        # #print(".... Verify NEW SETTING of mainscreen_bg_color_val_global =  " + str(mainscreen_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of viewscreen_bg_color_val_global =  " + str(viewscreen_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of selectlist_bg_color_val_global =  " + str(selectlist_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of newlist_bg_color_val_global =  " + str(newlist_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of usermanual_bg_color_val_global =  " + str(usermanual_bg_color_val_global) )
        # #print(".... Verify NEW SETTING of config_bg_color_val_global =  " + str(config_bg_color_val_global) )
        # #print("\n")
        # #print(".... Verify NEW SETTING of mainscreen_fg_color_val_global =  " + str(mainscreen_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of viewscreen_fg_color_val_global =  " + str(viewscreen_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of selectlist_fg_color_val_global =  " + str(selectlist_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of newlist_fg_color_val_global =  " + str(newlist_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of usermanual_fg_color_val_global =  " + str(usermanual_fg_color_val_global) )
        # #print(".... Verify NEW SETTING of config_fg_color_val_global =  " + str(config_fg_color_val_global) )
        # #print("\n")
        

        ########################################################################################## 
        #
        # Double Check path to app_config.ini 
        #
        # #print(".... CHECK PATH of fullpath_app_config_ini_global =  " + str(fullpath_app_config_ini_global) )
        # #print("\n")
        #
        # instantiate ConfigParser()
        config = ConfigParser()
        #
        # add new app_config.ini file data settings   
        # and re-write the app_config.ini file
        #
        config.add_section("MAIN_SCREEN_COLOR") 
        config.set("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val", str(mainscreen_bg_color_val_global) )
        config.set("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val", str(mainscreen_fg_color_val_global) )

        config.add_section("VIEW_SCREEN_COLOR") 
        config.set("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val", str(viewscreen_bg_color_val_global) )
        config.set("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val", str(viewscreen_fg_color_val_global) )

        config.add_section("SELECT_SCREEN_COLOR")
        config.set("SELECT_SCREEN_COLOR", "selectlist_bg_color_val", str(selectlist_bg_color_val_global) )
        config.set("SELECT_SCREEN_COLOR", "selectlist_fg_color_val", str(selectlist_fg_color_val_global) )

        config.add_section("NEWLIST_SCREEN_COLOR")
        config.set("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val", str(newlist_bg_color_val_global) )
        config.set("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val", str(newlist_fg_color_val_global) )
                   
        config.add_section("USERMANUAL_SCREEN_COLOR")
        config.set("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val", str(usermanual_bg_color_val_global) )
        config.set("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val", str(usermanual_fg_color_val_global) )
        
        config.add_section("CONFIG_SCREEN_COLOR")
        config.set("CONFIG_SCREEN_COLOR", "config_bg_color_val", str(config_bg_color_val_global) )
        config.set("CONFIG_SCREEN_COLOR", "config_fg_color_val", str(config_fg_color_val_global) )
                   

        # save app_config.ini file 
        with open(str(fullpath_app_config_ini_global), 'w') as configfile:
             config.write(configfile)

        # wait one fifth of a second before closing window
        time.sleep(.2)

        # pass executive window control back to App() Class and
        # create and update a CONFIG PROCESSING REQUEST GLOBAL to utilize
        # the THREAD in main() and the CONFIG PROCESSING REQUEST GLOBAL to
        # re-configure the App() Class Object with these new config settings.
        app_config_request_global = True

        # write a new logfile to update the logfile items upon Config updates.
        inst_Write_Main_Logfile_upon_config = Write_Main_Logfile()
        inst_Write_Main_Logfile_upon_config.write_update_logfile()

        self.master.destroy()

    
      
    def close_windows(self):
        self.master.destroy()


            

# VIEW USERS MANUAL and SYSTEM ADMINISTRATION INFO IN A LARGE SCREEN TEXTBOX  
#
class Demo1(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global usermanual_bg_color_val_global
        global usermanual_fg_color_val_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_fn_cm_sw_app_logfile_global

        self.master = master
        self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above 
        # self.master.geometry("900x550") 
        
        self.master.configure(background=str(usermanual_bg_color_val_global) )

        self.master.title("Contact Management Application Software - System Administration and Users Manual")

        self.quitButton = Button(self.master, text = 'RETURN to MAIN SCREEN', width = 30, height = 2, \
            font=('Helvetica', '12'), background="IndianRed1", command = self.close_windows)
        
        self.quitButton.grid(row=3, column=0, sticky = W)
          
        self.display_exceptions_logfile_Button = Button(self.master, text = 'DISPLAY EXCEPTIONS LOGFILE', width = 30, height = 2, \
            font=('Helvetica', '12'), background="light sea green", command = self.display_exceptions_logfile)
        
        self.display_exceptions_logfile_Button.grid(row=3, column=0, sticky = E)


        ###############################################################################
        #
        # Programming Note:
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        # 
        ###############################################################################

 
        # TEXTBOX to insert TITLE at top of window and identify
        # the current Contact List File - cm_listbox_file_global  

        self.title_1_text_box = Text(self.master, width=94, height = 1)
        self.title_1_text_box.grid(row=0, column=0, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(usermanual_fg_color_val_global), background=str(usermanual_bg_color_val_global) )
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "     CONTACT MANAGEMENT USERS MANUAL   .....   SYSTEM ADMINISTRATION INFO  "

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the USERS MANUAL and SYSTEM ADMIN INFO

        self.view_text_box = Text(self.master, width=137, height = 30)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '12'), \
            fg = str(usermanual_fg_color_val_global), background=str(usermanual_bg_color_val_global) )
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # create a Scrollbar and associate it with self.view_text_box 
        self.scrollb = Scrollbar(self.master, command=self.view_text_box.yview)
        self.scrollb.grid(row=2, column=1, sticky='NSW')
        self.view_text_box['yscrollcommand'] = self.scrollb.set

        # INSERT LOGFILE DATA LINES into TEXTBOX to VIEW the TEXTBOX
        # after loading the current LOGFILE using the full path name:
        # fullpath_fn_cm_sw_app_logfile_global
        
        self.textFile = open(fullpath_fn_cm_sw_app_logfile_global, 'r')

        with open(str(fullpath_fn_cm_sw_app_logfile_global) ) as fin:
             for line in fin:
                 self.view_text_box.insert(END, line)
        
        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)  

        ############################################################################### 
        #
        # Programming Note:     ( Reference to the code above )   
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################


                        
    def display_exceptions_logfile(self):
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # INSERT LOGFILE DATA LINES into TEXTBOX to VIEW the TEXTBOX
        # after loading the current LOGFILE using the full path name:
        # fullpath_fn_cm_sw_app_logfile_global and then also append 
        # the exceptions logfile to the TEXTBOX. And then Disable the
        # TEXTBOX for Insert.  
        #
        # The exceptions logfile path is str(fullpath_exception_logfile_global)
        
        self.textFile = open(fullpath_fn_cm_sw_app_logfile_global, 'r')

        with open(str(fullpath_fn_cm_sw_app_logfile_global) ) as fin:
             for line in fin:
                 self.view_text_box.insert(END, line)

        self.exceptionFile = open(fullpath_exception_logfile_global, 'r')

        with open(str(fullpath_exception_logfile_global) ) as exception_file_handle_var:
             for line in exception_file_handle_var:
                 self.view_text_box.insert(END, line)
            
             # print(exception_file_handle_var.read() )

        # Disable TEXT WIDGET for Insert 
        self.view_text_box.config(state=DISABLED)

        ###########################################################################
        #
        # Update the Title Textbox to indicate EXCEPTIONS LOGFILE is displayed.
        # 
        ###########################################################################

        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_update_TITLE = "    SYSTEM ADMINISTRATION INFO:    *** EXCEPTIONS LOGFILE DISPLAY ***"

        self.title_1_text_box.insert(END, text_update_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert
        



    def close_windows(self):
        self.master.destroy()




##############################################################################
#
# SELECT A CONTACT LIST FILE FROM A LISTBOX.
#
# THEN READ IN THE CORRESPONDING DICTIONARY FILE INTO A DICTIONARY GLOBAL
# SO THAT IT CAN BE AVAILABLE TO ALL CLASSES TO BROWSE OR WHATEVER.
#
##############################################################################
#
class Demo2(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global kick_thread_to_update_main_entry_widgets

        self.master = master
        self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550") 
        
        self.master.configure(background=str(selectlist_bg_color_val_global) )

        self.master.title("Contact Management Application Software - Select Contact List")
        
        self.select_file_button = Button(self.master, text = "CLICK HERE after you \nhave SELECTED \na CONTACT LIST File", \
            width=25,height=3, font=('Helvetica', '12'), background="light sea green", command = self.get_Listbox_File)
            
        self.select_file_button.grid(row=1, column=0, sticky = W)
        self.select_file_button.bind("<Button-1>", self.get_Listbox_File)

        
        self.quitButton = Button(self.master, text = 'CLICK HERE to\nReturn to Main Screen', width = 25, height = 2, \
            font=('Helvetica', '12'), background="IndianRed1", command = self.close_windows)
        
        self.quitButton.grid(row=4, column=0, sticky = W)

        # TEXTBOX to insert TITLE at top of window  

        self.title_1_text_box = Text(self.master, width=42, height = 1)
        self.title_1_text_box.grid(row=0, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="light sea green")

        text_1_TITLE = "Select CONTACT LIST below :  "

        self.title_1_text_box.insert(END, text_1_TITLE)


        self.lbox = Listbox(self.master, width=52, height = 22)
        self.lbox.grid(row=2, column=1, sticky = W)
        self.lbox.config(borderwidth=10, font=('Helvetica', '12'), background="light sea green") 
        self.lbox.bind("<<ListboxSelect>>", self.OnListBoxSelect)

        # create a Scrollbar and associate it with self.lbox 
        self.scrollb = Scrollbar(self.master, command=self.lbox.yview)
        self.scrollb.grid(row=2, column=2, sticky='NSEW')
        self.lbox['yscrollcommand'] = self.scrollb.set

        # Load all .txt files from cm_appdatafiles_path_global directory into the LISTBOX
        results = []

        testdir = str(cm_appdatafiles_path_global)

        for root,dirs,files in os.walk(testdir):
            for f in files:
                 if ( (f.endswith('.txt') and ("cm_list_" in str(f) ) ) ):
                     results.append(f)

        for fileName in results:
               self.lbox.insert(0, fileName)


    

    def get_Listbox_File(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global listbox_file_capture_global
        global cnotes_dict_file_global
        global fullpath_cnotes_dict_file_global
        global master_cm_list_name_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global kick_thread_to_update_main_entry_widgets
        # This button command gets the filename_value from
        # below (this Demo2 Class) and sets the
        # CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # AND THE LISTBOX WIDGET METHOD:   
        #     
        # cm_filename_value = widget.get(selection[0])
        #

        ######################################################
        #
        # IMPORTANT:   *** Exception Handler ***
        #
        # This exception handler code captures the IndexError Exception that happens
        # if the USER (OPERATOR) does NOT select a Contact List
        # from the LISTBOX -- In that case:
        # we notify the operator with a messagebox and then we
        # self.master.destroy() and return to bring us back to
        # the main screen for another try.

        verify_listbox_selection = self.lbox.curselection()

        try:
               test_cm_filename_value = str(self.lbox.get(verify_listbox_selection[0] ) )
        except IndexError as err:
               messagebox.showinfo("Contact Manager Guide ...", \
               "ATTENTION: \n\nPlease SELECT a Contact List from the LISTBOX ..... \n\n OPERATOR ERROR (Index Error): \n" + str(err) )
               self.master.destroy()
               return


        selection = self.lbox.curselection()
        cm_filename_value = self.lbox.get(selection[0])
        cm_listbox_file_global = self.lbox.get(selection[0])

        # store_selected listbox filename - cm_filename_value in two classes
        lbfn_instance = Store_Lbox_Filename(selected_lbox_file = cm_filename_value)
        lbfn_instance.set_listbox_file(new_Lbox_File = cm_filename_value)
        get_lbfn_call = lbfn_instance.get_listbox_file()

        # WE ARE SELECTING A CONTACT LIST, BUT WE ALSO HAVE TO
        # UPDATE THE SELECTION OF THE CORRESPONDING DICTIONARY FILE  
        cm_fn_string = str(cm_listbox_file_global)
        split_cn_fn_string = cm_fn_string.split("cm_list_")[1]

        # Syncronize global dict_filename_global with cm_listbox_file_global
        dict_filename_global = "dict_file_" + str(split_cn_fn_string)

        split_cn_fn_string_again = split_cn_fn_string.split(".txt")[0]

        # Finally we must update the master_cm_list_name_global
        master_cm_list_name_global = str(split_cn_fn_string_again)

        # Set listbox_file_capture_global to trigger Contact List Entry Textbox Update 
        # as we have completed registering all the Listbox Filename variable settings
        # We will reset this listbox_file_capture_global back to False after we
        # update the Contact List Entry Textbox with the Listbox Filename selected 
        listbox_file_capture_global = True

        # UPDATE APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files. 
        
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
        
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )


        ###################################################################################
        #
        # If the Contact List was created before the Contact Notes Capability Item,
        # then there will not be a fullpath_cnotes_dict_file_global FILE because
        # the fullpath_cnotes_dict_file_global FILE is created when the User creates
        # a NEW Contact List, so we must test for the existance of the FILE
        # fullpath_cnotes_dict_file_global FILE here, before we try to write to it.
        # If our test indicates that the fullpath_cnotes_dict_file_global FILE
        # does NOT exist, we must create a fullpath_cnotes_dict_file_global FILE.
        #  
        # We want to be sure that when a contact list is selected, we test for the
        # existance of the fullpath_cnotes_dict_file_global FILE, which would
        # need to be created with this code below for any Contact Lists that were
        # created previous to Version 7. And we would do this in Demo2 SELECT LIST.
        #    
        ####################################################################################

        # Build the cnotes_dict_file_global from the master_cm_list_name_global
        # that was acquired above when selcting a contact list.

        cnotes_dict_file_global = "cnotes_" + str(master_cm_list_name_global) + ".txt"

        # print("  ")
        # print(".... VERIFY master_cm_list_name_global FILENAME:  " + str(master_cm_list_name_global) )
        # print("  ")
        # print(".... VERIFY cnotes_dict_file_global FILENAME:  " + str(cnotes_dict_file_global) )
        # print("  ")

        # Build the fullpath_cnotes_dict_file_global from the cnotes_dict_file_global
        # filename that was built above.

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        # print(".... VERIFY fullpath_cnotes_dict_file_global FILENAME:  " + str(fullpath_cnotes_dict_file_global) )
        # print("  ")

        if os.path.isfile(fullpath_cnotes_dict_file_global) == False:

             # Create the File for Contact NOTES DICTIONARY Filename fullpath_cnotes_dict_file_global
             with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
                   new_notes_wdictf.flush()
                   new_notes_wdictf.write("\n")            


        # READ IN THE CORRESPONDING DICTIONARY FILE INTO A DICTIONARY GLOBAL
        # SO THAT IT CAN BE AVAILABLE TO ALL CLASSES TO BROWSE OR WHATEVER.
        # 
        # TO GET THE selected_dictionary_loaded_global GLOBAL SET .... 
        #    
        # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        # WHICH SETS THE selected_dictionary_loaded_global GLOBAL. 

        inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        loaded_contact_dict_acquired = inst_loaded_Process_Dict_File.read_target_dict_file()

        selected_dictionary_record_index_global = 1
        selected_dictionary_record_index_focus_global = 1

        # kick thread to SET mainscreen entry widget data
        kick_thread_to_update_main_entry_widgets = True

        # #print("\n")
        # #print(".... SELECTED and LOADED - selected_dictionary_loaded_global =  " + str(fullpath_fn_dict_filename_global) )
        # #print("\n")

        # write a new logfile to update the logfile items each time a new Contact List is Selected
        inst_Write_Main_Logfile_when_list_select = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_list_select.write_update_logfile()
                

        # close listbox frame window after storing selected filename in Store_Lbox_Filename() Class
        self.master.destroy()
        return cm_filename_value
          


    def OnListBoxSelect(self, event):
        global listbox_file_capture_global
        listbox_file_capture_global = "False"
        widget = event.widget
        selection = widget.curselection()
        filename_value = widget.get(selection[0])
        selection_value_tuple = [selection, filename_value]
        return filename_value



    def close_windows(self):
        self.master.destroy()

  

# ENTER A NEW CONTACT LIST NAME IN A TEXTBOX 
#
class Demo3(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global insert_first_contact_global
        global kick_thread_to_update_main_entry_widgets
        global selected_dictionary_record_index_global
        global selected_dictionary_record_index_focus_global
        global prepend_cnotes_dict_file_global
        global master_cm_list_name_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_cnotes_dict_file_global
        global fullpath_prepend_cnotes_dict_file_global
        self.master = master
        self.frame = tk.Frame(self.master)

        huge_font = ('Verdana',32)
        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")
        
        self.master.configure(background=str(newlist_bg_color_val_global) )

        self.master.title("Contact Management Application Software - Create New Contact List")

        self.select_file_button = Button(self.master, text = "CLICK HERE after you \nhave ENTERED a NEW\nCONTACT LIST NAME\nExample: sales-calls-MAY-25", \
             width=30,height=4, font=('Helvetica', '18'), background="light sea green", command = self.get_Textbox_File)
            
        self.select_file_button.grid(row=1, column=0, sticky = W)
        self.select_file_button.bind("<Button-1>", self.get_Textbox_File)

        
        self.quitButton = Button(self.master, text = 'CLICK HERE to\nReturn to Main Screen', width = 20, height = 2, \
            font=('Helvetica', '16'), background="IndianRed1", command = self.close_windows)
        
        self.quitButton.grid(row=1, column=1, sticky = N)

        # INSERT TEXTBOX CREATION HERE FOR NEW CONTACT LIST FILENAME
        self.entry_CM_FILENAME = StringVar()
        self.my_cm_filename_entry = Entry(self.master, textvariable = self.entry_CM_FILENAME, font = huge_font, width = 30)
        self.my_cm_filename_entry.grid(sticky = W, row=2, column=0)
        self.my_cm_filename_entry.config(borderwidth=5, background="light sea green")
        


    def get_Textbox_File (self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global cnotes_dict_file_global
        global insert_first_contact_global
        global selected_dictionary_record_index_global
        global selected_dictionary_record_index_focus_global
        global kick_thread_to_update_main_entry_widgets
        global prepend_cnotes_dict_file_global
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global fullpath_cnotes_dict_file_global
        global fullpath_prepend_cnotes_dict_file_global
        ###########################################################################
        # This button command gets the contact list name from
        # the Demo3 Textbox and sets the cm_textbox_newfile_global
        # and cm_textbox_newfile_global is used in THREAD to 
        # set the CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # and THE SET TEXTBOX ENTRY WIDGET METHOD:
        #
        #  cm_textbox_newfile_global = self.my_cm_filename_entry.get()
        #
        ###########################################################################
        #
        #  textbox_newfile_capture_global = False
        #
        #  cm_textbox_newfile_global = "Enter New Contact LIst Name Here"
        #
        ###########################################################################  
        #

        cm_textbox_newfile_global = self.my_cm_filename_entry.get()
        master_cm_list_name_global = self.my_cm_filename_entry.get()
        textbox_newfile_capture_global = True

        # Create NEW FILES for the cm_list_CONTACT_LIST_NAME 
        # and dict_file_CONTACT_LIST_NAME Globals filenames
        cm_listbox_file_global = "cm_list_" + str(cm_textbox_newfile_global) + ".txt"
        dict_filename_global = "dict_file_" + str(cm_textbox_newfile_global) + ".txt"
        cnotes_dict_file_global = "cnotes_" + str(cm_textbox_newfile_global) + ".txt"

        # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files. 
       
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )

        fullpath_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )

        fullpath_prepend_cnotes_dict_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cnotes_dict_file_global) )
        
       
        # Create the new Contact List File and add Titles 
        with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
              wf_titles.flush()
              wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "," + "\n")


        
        # Create the File for Contact DICTIONARY Filename dict_filename_global
        with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
              new_wdictf.flush()
              new_wdictf.write("\n")


        # Create the File for Contact NOTES DICTIONARY Filename cnotes_dict_file_global
        with open(fullpath_cnotes_dict_file_global, 'a') as new_notes_wdictf:
              new_notes_wdictf.flush()
              new_notes_wdictf.write("\n")

        # Set the global - insert_first_contact_global = True
        # to add the FIRST RECORD to the New Contact List so the Database Files
        # have at least one Contact to avoid KeyError Exceptions.
        # This triggers the App Class to execute the   
        # self.first_Contact_Data_Entry() method.

        insert_first_contact_global = True

        # #print("\n") 
        # #print(".... SELECTED and LOADED - selected_dictionary_loaded_global =  " + str(fullpath_fn_dict_filename_global) )
        # #print("\n")

        # write a new logfile to update the logfile items each time a new Contact List is Created
        inst_Write_Main_Logfile_when_new_list = Write_Main_Logfile()
        inst_Write_Main_Logfile_when_new_list.write_update_logfile()

              
        # close the Enter New Contact List File window  
        
        self.master.destroy()
        return
    
      
    def close_windows(self):
        self.master.destroy()




# DISPLAY OR VIEW A CONTACT LIST IN A LARGE SCREEN TEXTBOX 
#
class Demo4(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global viewscreen_bg_color_val_global

        self.master = master
        self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice 
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550") 
        
        self.master.configure(background=str(viewscreen_bg_color_val_global) )

        self.master.title("Contact Management Application Software - Contact List Display and Scroll")
          
        self.quitButton = Button(self.master, text = 'RETURN to MAIN SCREEN', width = 30, height = 2, \
            font=('Helvetica', '12'), background="IndianRed1", command = self.close_windows)
        
        self.quitButton.grid(row=3, column=0, sticky = W)

        ###############################################################################
        #
        # Programming Note:
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################

 
        # TEXTBOX to insert TITLE at top of window and identify
        # the current Contact List File - cm_listbox_file_global  

        self.title_1_text_box = Text(self.master, width=95, height = 1)
        self.title_1_text_box.grid(row=0, column=0, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(viewscreen_fg_color_val_global), background=str(viewscreen_bg_color_val_global) )
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "CONTACT LIST:  " + str(cm_listbox_file_global) + "    DICTIONARY: " + str(dict_filename_global) 

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the DICTIONARY FILE corresponding 
        # to the current CONTACT LIST SELECTED or CREATED 

        self.view_text_box = Text(self.master, width=95, height = 19)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '18'), \
            fg = str(viewscreen_fg_color_val_global), background=str(viewscreen_bg_color_val_global) )
        self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        # create a Scrollbar and associate it with self.view_text_box 
        self.scrollb = Scrollbar(self.master, command=self.view_text_box.yview)
        self.scrollb.grid(row=2, column=1, sticky='NSW')
        self.view_text_box['yscrollcommand'] = self.scrollb.set

        # VIEW the TEXTBOX after loading the current
        # DICTIONARY Contact List File - dict_file_cm_listbox_file_global
        # which is stored in APPDATA at fullpath_fn_dict_filename_global

        self.textFile = open(fullpath_fn_dict_filename_global, 'r')

        # This takes the file object opened with the open() and turns it into a string which 
        # you can now use textString in a text widget.
        self.textString = self.textFile.read()

        # Count the DATA RECORDS in the string by counting the
        # number of "DATA_RECORD_DELIMITER:" patterns 
        self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")

        # TEXTBOX appears to have residual data upon startup button select VIEW CONTACTS, 
        # so we may have to check to see that a dictionary global is set to
        # an actual valid dictionary after being initialized to
        # dict_filename_global = "No Contact Dictionary"
        
        self.num_data_records_plus_one = self.num_data_records + 1
        # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings  
        for record_index in range (1, self.num_data_records_plus_one):
             self.view_text_box.insert(END, "\n")
             self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]
             for key_index in range (1, 10):
                   key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                   if key_index == 1:
                        self.view_text_box.insert(END, "NAME: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, " ")
                   if key_index == 2:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 3:
                        self.view_text_box.insert(END, "ADDRESS: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 4:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 5:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, ", ")
                   if key_index == 6:
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 7:
                        self.view_text_box.insert(END, "PHONE: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "   ")
                   if key_index == 8:
                        self.view_text_box.insert(END, "EMAIL: ")
                        self.view_text_box.insert(END, key_indexed_string)
                        self.view_text_box.insert(END, "\n")
                   if key_index == 9:
                         self.view_text_box.insert(END, "WEBSITE: ")
                         self.view_text_box.insert(END, key_indexed_string)
                         self.view_text_box.insert(END, "\n")
                   

        self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 

        ###############################################################################
        #
        # Programming Note:     ( Reference to the code above )   
        #
        # Note that the generic sequence of TEXT WIDGET Commands to use to
        # make the TEXT WIDGET be READ ONLY is as follows:
        #
        # text.config(state=NORMAL)
        # text.delete(1.0, END)
        # text.insert(END, text)
        # text.config(state=DISABLED)
        #
        ###############################################################################
        #
        # Specifically, Our Big Text Widget will experience these commands:
        #
        # self.view_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        # self.view_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data
        # self.view_text_box.insert(END, key_indexed_string)  # Insert Text Data 
        # self.view_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert 
        #
        ###############################################################################



    def close_windows(self):
        self.master.destroy()




# SELECT An "EXPORT TO EXCEL" CONTACT LIST FILE FROM A LISTBOX 
#
class Demo5(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global

        self.master = master
        self.frame = tk.Frame(self.master)

        large_font = ('Verdana',20)
        minilarge_font = ('Verdana',16)
        medium_font = ('Verdana',12,'bold')
        small_font = ('Verdana',10)
        menubar_font = ('Helvetica', '12')

        # Max Screen Size with the Title Bar - BEST Choice  
        self.master.wm_state('zoomed')

        # Another way to set screen size (other than BEST Choice above
        # self.master.geometry("900x550")   
        
        self.master.configure(background='ivory4')

        self.master.title("Contact Management Application Software - Export Contact List to Excel")
        
        self.select_file_button = Button(self.master, text = "CLICK HERE\nto EXPORT Contact List\nto EXCEL Spreadsheet", \
            width=25,height=3, font=('Helvetica', '12'), background="light sea green")
        #command=self.get_Listbox_File  
        self.select_file_button.grid(row=1, column=0, sticky = W)
        self.select_file_button.bind("<Button-1>",self.convert_CSV_to_Excel)

        
        self.quitButton = Button(self.master, text = 'CLICK to Return\nto Main Screen', width = 25, height = 2, \
            font=('Helvetica', '12'), background="IndianRed1", command = self.close_windows)
        
        self.quitButton.grid(row=4, column=0, sticky = W)

        # TEXTBOX to insert TITLE at top of window  

        self.title_1_text_box = Text(self.master, width=90, height = 2)
        self.title_1_text_box.grid(row=0, column=1, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="light sea green")

        text_1_TITLE = "  Currently Selected CONTACT LIST\n  for EXPORT to EXCEL:   " + str(master_cm_list_name_global)

        self.title_1_text_box.insert(END, text_1_TITLE)

        # TEXTBOX to insert EXCEL FILE PATH NOTE and CONTACT LIST EXPORTED STATUS MESSAGE at top of window 

        self.title_2_text_box = Text(self.master, width=90, height = 3)
        self.title_2_text_box.grid(row=1, column=1, sticky = W)
        self.title_2_text_box.config(borderwidth=10, font=('Helvetica', '14'), background="light sea green")

        text_2_TITLE = "  CLICK EXPORT to EXCEL Button to the LEFT ....\n  Note:  EXCEL Spreadsheets are located in Windows Folder:\n  " + str(export_csv_excel_userprofile_global)
        self.title_2_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_text_box.insert(END, text_2_TITLE)



    def convert_CSV_to_Excel(self, event):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global
        global username_global
        global appdata_path_global
        global cm_appdatafiles_path_global
        global export_csv_excel_userprofile_global
        global export_csv_excel_cm_appdata_global
        global export_to_excel_listbox_select_fn_global
        global new_excel_file_created_global


        # WE HAVE PREVIOUSLY SELECTED A CONTACT LIST for EXCEL
        # AND CAPTURED THAT INFO USING GLOBAL VARIABLES
        
        export_to_excel_filename_path = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )

        export_to_excel_workbook_filename_path = os.path.join(str(export_csv_excel_cm_appdata_global), str(master_cm_list_name_global) + ".xlsx" )
        
        export_to_excel_workbook_filename_home_path = os.path.join(str(export_csv_excel_userprofile_global), str(master_cm_list_name_global) + ".xlsx" )

        new_excel_file_created_global = str(export_to_excel_workbook_filename_home_path)

        # Update Excel Spreadsheet STATUS TextBox with PATH and FILENAME of NEW Excel Spreadsheet 
        text_2_NEW_TITLE = "  STATUS UPDATE:\n  Your NEW Excel SPREADSHEET has been CREATED in Windows Folder:\n  " + str(new_excel_file_created_global)
        self.title_2_text_box.delete(1.0, END)  # Clear the TEXT WIDGET of Data
        self.title_2_text_box.insert(END, text_2_NEW_TITLE)
        self.title_2_text_box.config(background="turquoise")

        #read the csv into a pandas dataframe 
        data = pd.read_csv(str(export_to_excel_filename_path) )    
        #setup the writer
        writer = pd.ExcelWriter(str(export_to_excel_workbook_filename_path), engine='xlsxwriter')
        writer_two = pd.ExcelWriter(str(export_to_excel_workbook_filename_home_path), engine='xlsxwriter')
        #write the dataframe to an xlsx file
        data.to_excel(writer, sheet_name=str(master_cm_list_name_global), index=False)
        data.to_excel(writer_two, sheet_name=str(master_cm_list_name_global), index=False)
        writer.save()
        writer_two.save()

        #####################################################################################################
        #
        # SAVE THIS CODE SHOWING EXAMPLE OF HOW TO INSTANTIATE CLASS Process_Dict_File to create OBJECT 
        # Testing CLASS Process__Dict_File to see the INSTANTIATION and the READ of the dict_file_
        # We should see the dictionary # printed when an excel spreadsheet is generated. 
        #
        #####################################################################################################

        ######### PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        #########
        ######### inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        ######### contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

        #####################################################################################################
        
        #   # #print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
        #   for key, value in contact_dict_acquired.items():
        #       # #print("\n")
        #       # #print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)   

        ## #print("\n")
        ## #print("\n")
        #for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
        #      # #print(" .... **** SORTED INSTANTIATED DICTIONARY **** .... =  :  " + str(s) ) 
  

        return new_excel_file_created_global 
  

    def close_windows(self):
        self.master.destroy()


        
        

class Store_Lbox_Filename(object):
      def __init__(self, selected_lbox_file):
            self.selected_lbox_file = selected_lbox_file


      def set_listbox_file(self, new_Lbox_File):
            self.selected_lbox_file = new_Lbox_File
            return


      def get_listbox_file(self):
            return self.selected_lbox_file


        

class Store_Contact_Dict(object):
      def __init__(self, this_contact_dict):
            self.this_contact_dict = this_contact_dict


      def set_contact_dict(self, new_this_contact_dict):
            self.this_contact_dict = new_this_contact_dict
            return


      def get_contact_dict(self):
            return self.this_contact_dict



###################################################################
#
# Build a CLASS to define the DICTIONARY of DICTIONARIES
# to allow instantiation of the object to store each
# dict_file_ representing a contact list.
#
###################################################################
#
class Store_dictionary_of_dictionaries(object):
      def __init__(self, this_dict_of_dicts):
            self.this_dict_of_dicts = this_dict_of_dicts


      def set_dict_of_dicts(self, new_this_dict_of_dicts):
            self.this_dict_of_dicts = new_this_dict_of_dicts
            return


      def get_dict_of_dicts(self):
            return self.this_dict_of_dicts



  #####################################################################################################
  #
  # SAVE THIS CODE SHOWING EXAMPLE OF HOW TO INSTANTIATE CLASS Process_Dict_File to create OBJECT
  # Testing CLASS Process__Dict_File to see the INSTANTIATION and the READ of the dict_file_
  # We should see the dictionary # printed when an excel spreadsheet is generated.
  #
  #####################################################################################################
  #
  #   inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
  #   contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()
  #
  #   # #print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
  #   for key, value in contact_dict_acquired.items():
  #       # #print("\n")
  #       # #print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)
  #        
  #   
  #   # #print("\n")
  #   # #print("\n")
  #   for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
  #         # #print(" .... SORTED INSTANTIATED DICTIONARY  =  :  " + str(s) ) 
  #
  ######################################################################################################


      
#######################################################################################
#
# class Process__Dict_File reads in dictionary files (dict_file_) into a STRING
# and then converts STRING into a DICTIONARY and then processes the DICTIONARY
# and then converts the processed DICTIONARY to a STRING and writes out the
# processed dictionary file. 
#
#######################################################################################

class Process_Dict_File(object):
      def __init__(self, target_dict_file):
            global selected_dictionary_loaded_global
            global num_of_dictionary_data_records_global
            global selected_dictionary_record_index_global
            self.target_dict_file = target_dict_file
            gfn = ''
            gln = ''
            gsa = ''
            gct = ''
            gst = ''
            gzc = ''
            gpn = ''
            gem = ''
            gws = ''
            contact_dict = {}


      ################################################################################
      #
      # Method to READ in the dict_file_ and PARSE to CREATE the
      # DICTIONARY OF DICTIONARIES - dict_of_dictionaries for selected Contact List
      # and then SORT the dict_of_dictionaries so the write_target_dict_file METHOD
      # can MAP from DICTIONARY OF DICTIONARIES to dict_file_ Format and
      # write the (eventually) newly SORTED dict_of_dictionaries to dict_file_
      #
      def read_target_dict_file(self):
              global selected_dictionary_loaded_global
              global num_of_dictionary_data_records_global
              global selected_dictionary_record_index_global
              # Read or Load DICTIONARY Contact List File - dict_file_cm_listbox_file_global
              # which is stored in APPDATA at fullpath_fn_dict_filename_global

              self.textFile = open(fullpath_fn_dict_filename_global, 'r')

              # This takes the file object opened with the open() and turns it into a string which 
              # you can now use textString in a text widget.
              self.textString = self.textFile.read()

              # Define dict_of_dictionaries and sorted_contact_dict
              dict_of_dictionaries = {}
              sorted_dict_of_dictionaries = {}
              sorted_d_of_d = {}
              get_dict_of_dicts_call = {}
              get_sorted_d_of_d_call = {}

              list_of_indexed_dictionaries = []
              new_sorted_list_of_indexed_dictionaries = []

              # Count the DATA RECORDS in the string by counting the
              # number of "DATA_RECORD_DELIMITER:" patterns 
              self.num_data_records = self.textString.count("DATA_RECORD_DELIMITER:")

              # Capture GLOBAL from the "DATA_RECORD_DELIMITER:" patterns Delimiters Counted.
              num_of_dictionary_data_records_global = self.num_data_records

              self.num_data_records_plus_one = self.num_data_records + 1
              # Operate on the textString to search for DATA_RECORD_DELIMITER: and KEY_SYNC: sub-strings  
              for record_index in range (1, self.num_data_records_plus_one):
                   d_of_d_index = record_index
                   self.data_record_string = self.textString.split("DATA_RECORD_DELIMITER:")[record_index]
                   for key_index in range (1, 10):
                         key_indexed_string = self.data_record_string.split("KEY_SYNC:")[key_index]
                         if key_index == 1: gfn = key_indexed_string
                         if key_index == 2: gln = key_indexed_string
                         if key_index == 3: gsa = key_indexed_string
                         if key_index == 4: gct = key_indexed_string
                         if key_index == 5: gst = key_indexed_string
                         if key_index == 6: gzc = key_indexed_string
                         if key_index == 7: gpn = key_indexed_string
                         if key_index == 8: gem = key_indexed_string
                         if key_index == 9: gws = key_indexed_string



                   # Since Dictionaries are immutable (cannot be changed), we could create a LIST
                   # and then SORT that list, and then RE-WRITE the dict_file_ and contact_list_ file
                   # FORMATS from the SORTED LIST, however, we have currently implemented sorting by
                   # creating a couple DICTIONARY of DICTIONARYIES to facilitate SORT Functionality ... 

                   
                   # Create DICTIONARY to store contact data 
                   contact_dict = {"First_Name_KEY": str(gfn), "Last_Name_KEY": str(gln), "Street_Address_KEY": str(gsa), \
                                   "City_Town_KEY": str(gct), "State_KEY": str(gst), "Zip_Code_KEY": str(gzc), \
                                   "Phone_Number_KEY": str(gpn), "EMail_KEY": str(gem), "Website_KEY": str(gws) }


                   # Create the {DICT_KEY: DICT_NUMBER_1} ... {DICT_KEY: DICT_NUMBER_#_of_Records} to build new NESTED dictionary
                   Dict_Key_String = "Dict_KEY" + str(record_index)

                   # dict[key] = value

                   # Define dict_of_dictionaries[str(Dict_Key_String)]
                   # and define sorted_dict_of_dictionaries[str(Dict_Key_String)]
                   dict_of_dictionaries[str(Dict_Key_String)] = {}
                   sorted_dict_of_dictionaries[str(Dict_Key_String)] = {}

                   dict_of_dictionaries[str(Dict_Key_String)]["First_Name_KEY"] = str(gfn)
                   dict_of_dictionaries[str(Dict_Key_String)]["Last_Name_KEY"] = str(gln)
                   dict_of_dictionaries[str(Dict_Key_String)]["Street_Address_KEY"] = str(gsa)
                   dict_of_dictionaries[str(Dict_Key_String)]["City_Town_KEY"] = str(gct)
                   dict_of_dictionaries[str(Dict_Key_String)]["State_KEY"] = str(gst)
                   dict_of_dictionaries[str(Dict_Key_String)]["Zip_Code_KEY"] = str(gzc)
                   dict_of_dictionaries[str(Dict_Key_String)]["Phone_Number_KEY"] = str(gpn)
                   dict_of_dictionaries[str(Dict_Key_String)]["EMail_KEY"] = str(gem)
                   dict_of_dictionaries[str(Dict_Key_String)]["Website_KEY"] = str(gws)


              # dict[key] = value             

              # Store dict_of_dictionaries to Store_dictionary_of_dictionaries Class  
              dict_of_contact_dicts_inst = Store_dictionary_of_dictionaries(this_dict_of_dicts = dict_of_dictionaries)
              dict_of_contact_dicts_inst.set_dict_of_dicts(new_this_dict_of_dicts = dict_of_dictionaries)
              get_dict_of_dicts_call = dict_of_contact_dicts_inst.get_dict_of_dicts()


              SORTED_SEQ_NUMBER = 1
              for s in sorted(dict_of_dictionaries.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):

                    select_tuple_one = str(s[1])
                    split_on_Street_Address_KEY = select_tuple_one.split("', 'Street_Address_KEY':")[0]
                    split_on_Last_Name_KEY = split_on_Street_Address_KEY.split("'Last_Name_KEY': '")[1]
                     
                    split_on_Last_Name_KEY = select_tuple_one.split("', 'Last_Name_KEY':")[0]
                    split_on_First_Name_KEY = split_on_Last_Name_KEY.split("{'First_Name_KEY': '")[1]

                    select_tuple_zero = str(s[0])
                    split_on_dict_KEY = select_tuple_zero.split("Dict_KEY")[1]

                    old_sorted_dict_KEY_String = "Dict_KEY" + str(split_on_dict_KEY)
                    
                    new_sorted_dict_KEY_String = "Dict_KEY" + str(SORTED_SEQ_NUMBER)

                    sorted_dict_of_dictionaries[str(new_sorted_dict_KEY_String)] = get_dict_of_dicts_call[str(old_sorted_dict_KEY_String)]

                    SORTED_SEQ_NUMBER += 1
 
              ########################################################################

              # Store NEW SORTED sorted_dict_of_dictionaries to Store_dictionary_of_dictionaries Class  
              sorted_d_of_d_inst = Store_dictionary_of_dictionaries(this_dict_of_dicts = sorted_dict_of_dictionaries)
              sorted_d_of_d_inst.set_dict_of_dicts(new_this_dict_of_dicts = sorted_dict_of_dictionaries)
              get_sorted_d_of_d_call = sorted_d_of_d_inst.get_dict_of_dicts()

              ######################################################################## 
              
              # RE-Create the new Contact List File and add Titles 
              with open(fullpath_fn_cm_listbox_file_global, 'w') as wf_titles:
                   wf_titles.flush()
                   wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "," + "\n")


        
              # RE-Create and Open the File for Contact DICTIONARY Filename dict_filename_global
              with open(fullpath_fn_dict_filename_global, 'w') as new_wdictf:
                   new_wdictf.flush()
                   new_wdictf.write("\n")
                    

              for record_index in range (1, self.num_data_records_plus_one):
              
                   ######################################################################### 

                   sdfn = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["First_Name_KEY"] )
                   sdln = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Last_Name_KEY"] )
                   sdsa = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Street_Address_KEY"] )
                   sdct = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["City_Town_KEY"] )
                   sdst = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["State_KEY"] )
                   sdzc = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Zip_Code_KEY"] )
                   sdpn = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Phone_Number_KEY"] )
                   sdem = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["EMail_KEY"] )
                   sdws = str(get_sorted_d_of_d_call["Dict_KEY" + str(record_index)]["Website_KEY"] )

                   # write sorted data records to cm_list_file
                   # Note that we use the FULLPATH - fullpath_fn_cm_listbox_file_global
            
                   with open(fullpath_fn_cm_listbox_file_global, 'a') as wf:
                        for x in range(0, 10):
                             if x == 0: wf.flush()
                             #--------------------------------------------------------
                             if x == 1: wf.write(sdfn + ",")
                             elif x == 2: wf.write(sdln + ",")
                             elif x == 3: wf.write(sdsa + ",")
                             elif x == 4: wf.write(sdct + ",")
                             elif x == 5: wf.write(sdst + ",")
                             elif x == 6: wf.write(sdzc + ",")
                             elif x == 7: wf.write(sdpn + ",")
                             elif x == 8: wf.write(sdem + ",")
                             elif x == 9: wf.write(sdws + "," + "\n")
                             else: pass

                   ########################################################################### 

                   # Write sorted contact data dictionary to dict_filename file from class method get_contact_dict_call
                   # Note that we use the FULLPATH - fullpath_fn_dict_filename_global
                   with open(fullpath_fn_dict_filename_global, 'a') as wdictf:
                        for x in range(0, 10):
                             if x == 0:
                                   wdictf.flush()
                                   wdictf.write("DATA_RECORD_DELIMITER:")
                             elif x == 1: wdictf.write("KEY_SYNC:" + sdfn )
                             elif x == 2: wdictf.write("KEY_SYNC:" + sdln )
                             elif x == 3: wdictf.write("KEY_SYNC:" + sdsa )
                             elif x == 4: wdictf.write("KEY_SYNC:" + sdct )
                             elif x == 5: wdictf.write("KEY_SYNC:" + sdst )
                             elif x == 6: wdictf.write("KEY_SYNC:" + sdzc )
                             elif x == 7: wdictf.write("KEY_SYNC:" + sdpn )
                             elif x == 8: wdictf.write("KEY_SYNC:" + sdem )
                             elif x == 9: wdictf.write("KEY_SYNC:" + sdws )
                             else: pass

            ####################################################################################### 

              # Set the selected_loaded_dictionary_global GLOBAL to make this current
              # Store_dictionary_of_dictionaries Object available Globally.
              # 
              selected_dictionary_loaded_global = get_sorted_d_of_d_call                         
            
              return get_sorted_d_of_d_call    # dict_of_dictionaries
 
      ##########################################################################  
      #
      # Method to MAP from DICTIONARY OF DICTIONARIES to dict_file_ Format and
      # write the (eventually) newly SORTED dict_of_dictionaries to dict_file_
      #
      #def write_target_dict_file(self, new_target_dict_file_string): 
            #self.target_dict_file_string = new_target_dict_file_string
            #return




#######################################################################################
#
# class Write_Exception_Logfile logs Exceptions during the application execution.  
#  
#######################################################################################

class Write_Exception_Logfile(object):

      def write_update_exception_logfile(self):
            with open(str(fullpath_exception_logfile_global), 'a') as exception_logfile:
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write(".... (Python) System.Version = " + str(sys.version) )
                  exception_logfile.write("\n" + ".... (tkinter Tcl) System.Version = " + str(tk.TclVersion) )
                  exception_logfile.write("\n" + ".... (tkinter Tk) System.Version = " + str(tk.TkVersion) )
                  exception_logfile.write("\n" + ".... (Windows) sys.platform = " + str(sys.platform) )
                  exception_logfile.write("\n" + ".... (Windows) platform.version = " + str(platform.version() ) )
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write("\n" + ".... Contact  Management  Workstation  Enterprise  Cloud  Software  Application: *** Version 8.0 ***")
                  exception_logfile.write("\n" + ".... Date : Time :  " + str(datetime.datetime.now() ) )
                  exception_logfile.write("\n_____________________________________________________________________________\n")
                  exception_logfile.write("\n") 
                  


      def log_exception(self, exception_info_string):
          # Create a Time Stamp and then execute logging the exception_info_string
          time_stamp_string = str(datetime.datetime.now() )
          exception_logging_time_stamp_string = "\n" + "T I M E   S T A M P  :  " + str(time_stamp_string) + "\n\n"
          with open(str(fullpath_exception_logfile_global), 'a') as exception_logfile:
              exception_logfile.write(str(exception_logging_time_stamp_string) )
              exception_logfile.write(str(exception_info_string) )

              # logger.error(str(exception_logging_string), exc_info=True)
                  


            
#######################################################################################
#   
# class Write_Main_Logfile writes a new logfile replacing the previous logfile. 
#  
#######################################################################################

class Write_Main_Logfile(object):

      def write_update_logfile(self):
            with open(str(fullpath_fn_cm_sw_app_logfile_global), 'w') as cmlogfile:
                  cmlogfile.write(".... (Python) System.Version = " + str(sys.version) )
                  cmlogfile.write("\n" + ".... (tkinter Tcl) System.Version = " + str(tk.TclVersion) )
                  cmlogfile.write("\n" + ".... (tkinter Tk) System.Version = " + str(tk.TkVersion) )
                  cmlogfile.write("\n" + ".... (Windows) sys.platform = " + str(sys.platform) )
                  cmlogfile.write("\n" + ".... (Windows) platform.system = " + str(platform.system() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.machine = " + str(platform.machine() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.platform = " + str(platform.platform() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.version = " + str(platform.version() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.processor = " + str(platform.processor() ) )
                  cmlogfile.write("\n" + ".... (Windows) platform.node = " + str(platform.node() ) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n" + ".... Contact  Management  Workstation  Enterprise  Cloud  Software  Application: *** Version 8.0 ***")
                  cmlogfile.write("\n" + ".... Date : Time :  " + str(datetime.datetime.now() ) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n.... USERNAME = " + str(username_global) )
                  cmlogfile.write("\n.... USER HOME PATH = " + str(userprofile_global) )
                  cmlogfile.write("\n.... APPDATA PATH = " + str(appdata_path_global) )
                  cmlogfile.write("\n.... **********************   D_A_T_A_B_A_S_E___F_I_L_E_S    ********************")
                  cmlogfile.write("\n.... APP CONFIG INI FILE PATH = " + str(fullpath_app_config_ini_global) )
                  cmlogfile.write("\n.... EXCEPTION LOGFILE PATH = " + str(fullpath_exception_logfile_global) )
                  cmlogfile.write("\n.... CONTACT MANAGEMENT DATA PATH = " + str(cm_appdatafiles_path_global) )
                  cmlogfile.write("\n.... CSV FILENAME = " + str(fullpath_fn_cm_listbox_file_global) )
                  cmlogfile.write("\n.... DICTIONARY FILENAME = " + str(fullpath_fn_dict_filename_global) )
                  cmlogfile.write("\n.... NOTES DICT FILENAME = " + str(fullpath_cnotes_dict_file_global) )
                  cmlogfile.write("\n.... GMAIL OAUTH2 CREDENTIALS = " + str(credential_home_path_global) )
                  cmlogfile.write("\n.... GMAIL OAUTH2 CLIENT SECRET = " + str(client_secret_path_global) )
                  cmlogfile.write("\n.... THIS LOGFILE PATH = " + str(fullpath_fn_cm_sw_app_logfile_global) )
                  cmlogfile.write("\n.... EXCEL OUTPUT PATH (AppData) = " + str(export_csv_excel_cm_appdata_global) )
                  cmlogfile.write("\n.... EXCEL OUTPUT PATH (UserProfile) = " + str(export_csv_excel_userprofile_global) )
                  cmlogfile.write("\n_____________________________________________________________________________\n")
                  cmlogfile.write("\n.... mainscreen background color = " + str(mainscreen_bg_color_val_global) + \
                                  "     .... viewcreen background color = " + str(viewscreen_bg_color_val_global) )
                  cmlogfile.write("\n.... selectlist background color = " + str(selectlist_bg_color_val_global) + \
                                  "     .... newlist background color = " + str(newlist_bg_color_val_global) )
                  cmlogfile.write("\n.... usermanual background color = " + str(usermanual_bg_color_val_global) + \
                                  "     .... config background color = " + str(config_bg_color_val_global) )




def main():
      global fullpath_gmail_oauth2_credentials_global
      global fullpath_exception_logfile_global
      global credential_home_dir_global
      global credential_appdata_dir_global
      global credential_home_path_global
      global credential_appdata_path_global
      global client_secret_path_global
      global valid_client_secret_key_format_global
      global gmail_oauth2_exceptions_status_global
      global gmail_oauth2_SPECIFIC_EXCEPTION_global
      global request_mainscreen_config_update_global
      global kick_thread_to_update_main_entry_widgets
      global insert_first_contact_global
      global listbox_file_capture_global
      global cm_listbox_file_global
      global username_global
      global userprofile_global
      global appdata_path_global
      global cm_appdatafiles_path_global
      global mainscreen_bg_color_val_global
      global viewscreen_bg_color_val_global
      global selectlist_bg_color_val_global
      global newlist_bg_color_val_global
      global usermanual_bg_color_val_global
      global config_bg_color_val_global
      global mainscreen_fg_color_val_global
      global viewscreen_fg_color_val_global
      global selectlist_fg_color_val_global
      global newlist_fg_color_val_global
      global usermanual_fg_color_val_global
      global config_fg_color_val_global
      global app_config_ini_val_global
      global app_config_request_global
      global fullpath_app_config_ini_global
      global fullpath_fn_cm_sw_app_logfile_global
      global export_csv_excel_userprofile_global
      global export_csv_excel_cm_appdata_global

#################################################################################################

 
#################################################################################################

      username_global = str(os.environ['USERNAME'])

      userprofile_global = str(os.environ['USERPROFILE'])

      appdata_path_global = str(os.environ['APPDATA'])

      cm_appdatafiles_path_global = os.path.join(str(appdata_path_global), "CONTACT_MANAGEMENT", str(username_global) )

      fullpath_fn_cm_sw_app_logfile_global = os.path.join(str(cm_appdatafiles_path_global), "cm_sw_app_logfile.txt" )

      fullpath_exception_logfile_global = os.path.join(str(cm_appdatafiles_path_global), "cm_app_exception_logfile.txt" )

      # start a new logfile for exceptions logging - this writes over file from previous session.
      with open(str(fullpath_exception_logfile_global), 'w') as exception_logfile_startup_new_file:
          exception_logfile_startup_new_file.write("\n\n")

      # write (append) the header for the exceptions logfile
      # that was created above - this is done once at program startup
      inst_Write_Exception_Logfile_Header_at_startup = Write_Exception_Logfile()
      inst_Write_Exception_Logfile_Header_at_startup.write_update_exception_logfile()

      fullpath_gmail_oauth2_credentials_global = os.path.join(str(cm_appdatafiles_path_global), ".credentials", 'gmail-python-quickstart.json')

      # GMAIL API OAUTH2 CLIENT CREDENTIALS .......  
      #
      # ESTABLISH client_secret.json file store paths (directories / folders) and set associated globals

      ##############################################################################
      #  
      # If modifying these scopes, delete your previously saved credentials
      # at ~/.credentials/gmail-python-quickstart.json
      #
      # SCOPES = "https://mail.google.com"
      # CLIENT_SECRET_FILE = 'client_secret.json'
      # APPLICATION_NAME = 'Gmail API Python Quickstart'
      #
      ##############################################################################

      # we create credentials here because we want to also maintain a copy of the credentials in APPDATA area.
      credential_appdata_dir = os.path.join(str(cm_appdatafiles_path_global), ".credentials")
      credential_appdata_dir_global = os.path.join(str(cm_appdatafiles_path_global), ".credentials")
      if not os.path.exists(credential_appdata_dir):
            os.makedirs(credential_appdata_dir)

      credential_appdata_path = os.path.join(credential_appdata_dir, 'gmail-python-quickstart.json')
      credential_appdata_path_global = os.path.join(credential_appdata_dir, 'gmail-python-quickstart.json')
      
      # we create credentials here because the http routine looks for them here. 
      home_dir = os.path.expanduser('~')
      client_secret_dir = os.path.join(home_dir, '.credentials')
      client_secret_dir_global = os.path.join(home_dir, '.credentials')
      credential_home_dir = os.path.join(home_dir, '.credentials')
      credential_home_dir_global = os.path.join(home_dir, '.credentials')
      if not os.path.exists(credential_home_dir):
            os.makedirs(credential_home_dir)

      credential_home_path = os.path.join(credential_home_dir, 'gmail-python-quickstart.json')
      credential_home_path_global = os.path.join(credential_home_dir, 'gmail-python-quickstart.json')
      client_secret_path = os.path.join(credential_home_dir, 'client_secret.json')
      client_secret_path_global = os.path.join(credential_home_dir, 'client_secret.json')

      ################################################################################################
      #
      #  VALIDATE JSON FILE EXISTANCE AND REQUIRED FILE CONTENTS .....
      #
      #  THEN, SET CORRESPONDIG STATUS PANEL BUTTON.
      #
      ################################################################################################
      #
      #  {
      #    "installed": {
      #      "client_id": "837647042410-75ifg...usercontent.com",
      #      "client_secret":"asdlkfjaskd",
      #      "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
      #      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      #      "token_uri": "https://accounts.google.com/o/oauth2/token"
      #            }
      #  }
      #
      ################################################################################################
      #
      # Verify that a Valid JSON File -  - exists at path:   
      # by executing the following sequence:
      #
      # 1. Check for existance of the client_secrets.json JSON File at the .credentials direcory:
      #
      #    PATH OF client_secret.json in the .credentials directory: client_secret_path_global.
      #
      #    Check for existance of the client_secret.json file using os.path.isfile(path).
      #
      # 2. Read the expected client_secrets.json JSON File into a TEXT STRING VARIABLE.
      #
      #
      # 3. Use the .count method to verify each required KEY in the client_secret.json JSON File.
      #
      #    See above for the "installed application" client_secret.json format.
      #
      #    client_secret_key_count_client_id = self.client_secret_textString.count("client_id")
      #
      #    client_secret_key_count_client_secret = self.client_secret_textString.count("client_secret")
      #
      #    client_secret_key_count_redirect_uris = self.client_secret_textString.count("redirect_uris")
      #
      #    client_secret_key_count_auth_uri = self.client_secret_textString.count("auth_uri")
      #
      #    client_secret_key_count_token_uri = self.client_secret_textString.count("token_uri")
      #
      # 
      # 4. If all the required KEYs are in the client_secret.json JSON File set a GLOBAL to True.
      #
      # 5. The Status Panel while loop with use this VERIFY JSON FILE GLOBAL to
      #    set the VERIFY JSON FILE Status Button Color to GREEN. 
      #
      #################################################################################################

      valid_client_secret_key_format_global = None

      try:

          if not os.path.isfile(client_secret_path_global):
              raise Exception("client_secret_FILE_NOT_FOUND")

      except Exception:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
          exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

          valid_client_secret_key_format_global = False
                    
          # open Write_Exception_Logfile() to append logfile to update the logfile items.
          inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
          exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
          
          exception_logging_string_3 = "\n\n"
                    
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )


      try:
              
          client_secret_textFile = open(client_secret_path_global, 'r')

          client_secret_textString = client_secret_textFile.read()

      except Exception:
          exc_type, exc_value, exc_traceback = sys.exc_info()
          lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
          exception_logging_string_2 = ''.join('Exception Info: ' + line for line in lines)

          valid_client_secret_key_format_global = False
                    
          # open Write_Exception_Logfile() to append logfile to update the logfile items.
          inst_Write_Exception_Logfile_client_secret_keys_validation = Write_Exception_Logfile()
          exception_logging_string_1 = "  *** OAUTH2 client_secret.json FILE NOT FOUND ***  at path: " + str(client_secret_path_global) + "\n" + "....  EXCEPTION DETAILS FOLLOW: " + "\n"
          exception_logging_string_3 = "\n\n"
                    
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_1) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_2) )
          inst_Write_Exception_Logfile_client_secret_keys_validation.log_exception(str(exception_logging_string_3) )

          
      client_secret_key_validation_counter = 0

      if os.path.isfile(client_secret_path_global) == True:

          if "client_id" in client_secret_textString:
              if "client_secret" in client_secret_textString:
                  if "redirect_uris" in client_secret_textString:
                      if "auth_uri" in client_secret_textString:
                          if "token_uri" in client_secret_textString:
                              all_client_secret_json_keys_found = True
              
              
          client_secret_key_count_client_id = client_secret_textString.count("client_id")
          if client_secret_key_count_client_id == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_client_secret = client_secret_textString.count("client_secret")
          if client_secret_key_count_client_secret == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_redirect_uris = client_secret_textString.count("redirect_uris")
          if client_secret_key_count_redirect_uris == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_auth_uri = client_secret_textString.count("auth_uri")
          if client_secret_key_count_auth_uri == 1:
              client_secret_key_validation_counter+=1
              

          client_secret_key_count_token_uri = client_secret_textString.count("token_uri")
          if client_secret_key_count_token_uri == 1:
              client_secret_key_validation_counter+=1
              

          try:

              if not ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                  raise Exception("JSON KEY VALIDATION ERROR")
              elif ( (all_client_secret_json_keys_found) and (client_secret_key_validation_counter == 5) ):
                  valid_client_secret_key_format_global = True

          except Exception:
              # add exception system variable acquisition code here for logging ....
              # set STATUS GLOBAL for JSON FILE KEY VALIDATION ERROR
              print("\n")
              print(" client_secret.json  *** KEY VALIDATION ERROR ***  at .credentials directory ...")
          

          #print("\n")
          #print(".... valid_client_secret_key_format_global = " + str(valid_client_secret_key_format_global) )

          
      ################################################################################################
      #
      # NOTE:    
      #
      # If modifying these scopes, delete your previously saved credentials
      # at ~/.credentials/gmail-python-quickstart.json
      #
      # SCOPES = "https://mail.google.com"
      # CLIENT_SECRET_FILE = client_secret_path
      # APPLICATION_NAME = 'Gmail API Python Quickstart'
      #
      ################################################################################################
      #
      # Try to Copy CM-APP-CLIENT JSON FILE TO APPDATA .credentials AREA - cm_appdatafiles_path_global
      #
      try:
          shutil.copyfile(str(credential_home_path_global), str(credential_appdata_path_global) )

      except:
          pass

      ##############################################################
      #
      # Begin app_config.ini Processing upon startup .....
      #
      ##############################################################

      fullpath_app_config_ini_global = os.path.join(str(cm_appdatafiles_path_global), "app_config.ini" )

      # Note:  str(master_cm_list_name_global) - When Contact List Selected.

      # instantiate ConfigParser() 
      config = ConfigParser()

      #
      # IF the app_config.ini file DOES NOT EXIST, Create-Initialize-Write app_config.ini file to CONFIGURE APP SETTINGS
      #     
      # #print("\n") 
      # #print(".... IF app_config.ini file DOES NOT EXIST, Create-Initialize-Write app_config.ini file to CONFIGURE APP SETTINGS")
      # #print("\n")
      # add app_config.ini file section(s) and some default values 
      # to create an app_config.ini file 
      if os.path.isfile(fullpath_app_config_ini_global) == False:
            config.add_section("MAIN_SCREEN_COLOR")
            config.set("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val", "dark slate gray")
            config.set("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val", "snow")

            config.add_section("VIEW_SCREEN_COLOR")
            config.set("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val", "dark slate gray")
            config.set("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val", "snow")

            config.add_section("SELECT_SCREEN_COLOR")
            config.set("SELECT_SCREEN_COLOR", "selectlist_bg_color_val", "dark slate gray")
            config.set("SELECT_SCREEN_COLOR", "selectlist_fg_color_val", "snow")

            config.add_section("NEWLIST_SCREEN_COLOR")
            config.set("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val", "dark slate gray")
            config.set("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val", "snow")

            config.add_section("USERMANUAL_SCREEN_COLOR")
            config.set("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val", "dark slate gray")
            config.set("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val", "snow")

            config.add_section("CONFIG_SCREEN_COLOR")
            config.set("CONFIG_SCREEN_COLOR", "config_bg_color_val", "dark slate gray")
            config.set("CONFIG_SCREEN_COLOR", "config_fg_color_val", "snow")

            # save app_config.ini file
            with open(str(fullpath_app_config_ini_global), 'w') as configfile:
                 config.write(configfile)

############################# CONFIGURE APP EVERY TIME PROGRAM STARTS ###########################

      if os.path.isfile(fullpath_app_config_ini_global) == True:
            # #print("\n") 
            # #print(".... READ the app_config.ini file to initialize the APP - CONFIGURE APP SETTINGS and set corresponding config GLOBALS")
            # #print("\n")
            # read app_config.ini file
            config.read(str(fullpath_app_config_ini_global) )
            # read values from app_config.ini file sections
            mainscreen_bg_color_val = config.get("MAIN_SCREEN_COLOR", "mainscreen_bg_color_val")
            viewscreen_bg_color_val = config.get("VIEW_SCREEN_COLOR", "viewscreen_bg_color_val")
            selectlist_bg_color_val = config.get("SELECT_SCREEN_COLOR", "selectlist_bg_color_val")
            newlist_bg_color_val = config.get("NEWLIST_SCREEN_COLOR", "newlist_bg_color_val")
            usermanual_bg_color_val = config.get("USERMANUAL_SCREEN_COLOR", "usermanual_bg_color_val")
            config_bg_color_val = config.get("CONFIG_SCREEN_COLOR", "config_bg_color_val")
#################################################################################################
            mainscreen_fg_color_val = config.get("MAIN_SCREEN_COLOR", "mainscreen_fg_color_val")
            viewscreen_fg_color_val = config.get("VIEW_SCREEN_COLOR", "viewscreen_fg_color_val")
            selectlist_fg_color_val = config.get("SELECT_SCREEN_COLOR", "selectlist_fg_color_val")
            newlist_fg_color_val = config.get("NEWLIST_SCREEN_COLOR", "newlist_fg_color_val")
            usermanual_fg_color_val = config.get("USERMANUAL_SCREEN_COLOR", "usermanual_fg_color_val")
            config_fg_color_val = config.get("CONFIG_SCREEN_COLOR", "config_fg_color_val")
#################################################################################################
            
            # set globals to communicate color settings
            mainscreen_bg_color_val_global = str(mainscreen_bg_color_val)
            viewscreen_bg_color_val_global = str(viewscreen_bg_color_val)
            selectlist_bg_color_val_global = str(selectlist_bg_color_val)
            newlist_bg_color_val_global = str(newlist_bg_color_val)
            usermanual_bg_color_val_global = str(usermanual_bg_color_val)
            config_bg_color_val_global = str(config_bg_color_val)
            
#################################################################################################

            mainscreen_fg_color_val_global = str(mainscreen_fg_color_val)
            viewscreen_fg_color_val_global = str(viewscreen_fg_color_val)
            selectlist_fg_color_val_global = str(selectlist_fg_color_val)
            newlist_fg_color_val_global = str(newlist_fg_color_val)
            usermanual_fg_color_val_global = str(usermanual_fg_color_val)
            config_fg_color_val_global = str(config_fg_color_val)
            
################################################################################################# 
      appdata_cm_then_user_dir = (str(cm_appdatafiles_path_global) )     
      if not os.path.isdir(appdata_cm_then_user_dir):
          os.makedirs(appdata_cm_then_user_dir)
#################################################################################################
      export_csv_excel_userprofile_global = os.path.join(str(userprofile_global), "export_csv_excel" )
      export_csv_excel_cm_appdata_global = os.path.join(str(cm_appdatafiles_path_global), "export_csv_excel" )
      
      if not os.path.isdir(export_csv_excel_userprofile_global):
          os.makedirs(export_csv_excel_userprofile_global)

      if not os.path.isdir(export_csv_excel_cm_appdata_global):
          os.makedirs(export_csv_excel_cm_appdata_global)
################################################################################################# 

      # Opens a Logfile every session which we can append to from anywhere 
      # in the program execution to monitor or debug. However, please note
      # that this logfile is being used to create a system administration screen
      # and therefore this logfile is re-written upon every new or selected
      # contact list Class/Method call. 

      # write a new logfile to update the logfile items upon program startup.
      inst_Write_Main_Logfile_upon_startup = Write_Main_Logfile()
      inst_Write_Main_Logfile_upon_startup.write_update_logfile()

 
      root = tk.Tk()
      cm_app = App(root)

      this_person = []

      # This is the cm_filename_worker_THREAD to maintain the Contact List Entry Widget filename String 
      # that we selected from LISTBOX to create CONTACT LIST FILENAME GLOBAL - str(cm_listbox_file_global)
      # Execute thread is a daeon thread that must run in a loop to always update the  
      # Contact List Entry Widget with the currently selected Contact List Filename: cm_listbox_file_global.
      # This thread is implemented as a continuous loop (with sleep) because if we let thr thread stop,
      # then we would have to instantiate it again to start another instance of the thread. 
      # The global variable, listbox_file_capture_global = False, resets the global variable 
      # that shows the STATUS of 1. Button Selects Contact List File 2. Update Entry Widget Textbox
      def cm_filename_worker():
           """Thread to UPDATE Contact List Entry Widgetthread - cm_filename_worker function"""
           
           global selected_dictionary_record_index_focus_global
           global kick_thread_to_update_main_entry_widgets
           global request_mainscreen_config_update_global
           global mainscreen_bg_color_val_global
           global insert_first_contact_global
           while 1:
                 
                 # Update the Main Screen Background Color per the latest GLOBAL setting
                 # so when User changes it, the new color appears instantly.
                 if request_mainscreen_config_update_global == True:
                     cm_app.master.config(background = str(mainscreen_bg_color_val_global) )
                     request_mainscreen_config_update_global = False

                 # #print("...... W H A T   I S   kick_thread_to_update_main_entry_widgets = " + str(kick_thread_to_update_main_entry_widgets) )

                 if (mode_select_global == "Browse Mode") and (str(dict_filename_global) != "No Contact Dictionary") and (kick_thread_to_update_main_entry_widgets == True):
                       try:
                             # Utilize this try to Avoid a KeyError if there is an EMPTY DICTIONARY where no contacts were added.

                             # #print("...... DO WE EVER INITIATE kick_thread_to_update_main_entry_widgets = True ??? " + str(kick_thread_to_update_main_entry_widgets) )
                             fn_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["First_Name_KEY"] )
                             ln_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Last_Name_KEY"] ) 
                             sa_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Street_Address_KEY"] ) 
                             ct_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["City_Town_KEY"] ) 
                             st_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["State_KEY"] ) 
                             zc_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Zip_Code_KEY"] ) 
                             pn_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Phone_Number_KEY"] ) 
                             em_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["EMail_KEY"] ) 
                             ws_browse = str(selected_dictionary_loaded_global["Dict_KEY" + str(selected_dictionary_record_index_focus_global)]["Website_KEY"] ) 
                             cm_app.entry_first.set(str(fn_browse) )
                             cm_app.entry_last.set(str(ln_browse) )
                             cm_app.entry_streetadd.set(str(sa_browse) )
                             cm_app.entry_citytown.set(str(ct_browse) )
                             cm_app.entry_state.set(str(st_browse) )
                             cm_app.entry_zipcode.set(str(zc_browse) )
                             cm_app.entry_phonenum.set(str(pn_browse) )
                             cm_app.entry_email.set(str(em_browse) )
                             cm_app.entry_website.set(str(ws_browse) )
                             selected_dictionary_counter_status_display = "Contact # " + str(selected_dictionary_record_index_focus_global) + \
                             " of " + str(num_of_dictionary_data_records_global) 
                             cm_app.contact_dict_count_status.set(str(selected_dictionary_counter_status_display) )
                      
                             # reset the kick_thread_to_update_main_entry_widgets = False 
                             kick_thread_to_update_main_entry_widgets = False

                       except:
                             # reset the kick_thread_to_update_main_entry_widgets = False
                             kick_thread_to_update_main_entry_widgets = False
                             
                             # # print(".... LIKELY DETECTED KEY ERROR due to empty DICTIONARY, thus no need to update main screen")

                 # Keep this master_cm_list_name_global data entry widget assertion     
                 # setting Contact List Entry Widget String from LISTBOX FILE GLOBAL - str(cm_listbox_file_global)
                 cm_app.entry_buildlist.set(str(master_cm_list_name_global) )
                 listbox_file_capture_global = False

                 # When each New Contact List is created, we will
                 # execute this method to insert the first contact  
                 # and then reset the insert_first_contact_global flag: 
                 if insert_first_contact_global == True:
                     
                     cm_app.first_Contact_Data_Entry()
            
                     # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
                     # WHICH SETS THE selected_dictionary_loaded_global GLOBAL.  

                     inst_loaded_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
                     loaded_contact_dict_acquired_GLOBAL = inst_loaded_Process_Dict_File.read_target_dict_file()

                     # NOTE:
                     # selected_dictionary_record_index_global = 1
                     # selected_dictionary_record_index_focus_global = 1

                     kick_thread_to_update_main_entry_widgets = True
                     insert_first_contact_global = False

                 # manage this thread CPU usage but keep updates executed
                 # in the thread fast enough for human perception.
                 time.sleep(.05)

      t = threading.Thread(name="main_Class_cm_app_THREAD", target=cm_filename_worker, daemon=True)
      t.start()

      root.mainloop()


    

if __name__ == '__main__':
    main()
        
                       

