################################################################
#
# Author: Mike Hughes
#
# Program: contact_management_python.py 
#
# Version: Beta 2.0
#
# Date: September 21, 2017 
#
# Description: Simple Contact Management Software Program.
# This Contact Management Software Program is implemented
# with very large FONT (Letter Sizes) to improve productivity.
#
# Language: Python 3.6.2 
#
################################################################ 

import os
import csv
import sys
import threading
import time
import datetime
import random
import xlsxwriter
import numpy
import pandas as pd

import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from tkinter.messagebox import *

from openpyxl import workbook

username_global = "USERNAME Path Not Set"
appdata_path_global = "APPDATA Path Not Set"
cm_appdatafiles_path_global = "CM_APPDATAFILES Path Not Set"
fullpath_fn_cm_listbox_file_global = "FULLPATH_FN_CM_LISTBOX_FILE Not Set"
fullpath_fn_dict_filename_global = "FULLPATH_FN_DICT_FILENAME Not Set"
fullpath_fn_cm_sw_app_logfile_global = "FULLPATH_FN_CM_SW_APP_LOGFILE Not Set"

export_csv_excel_userprofile_global = "EXPORT CSV TO EXCEL USERPROFILE DIR Not Set"
export_csv_excel_cm_appdata_global = "EXPORT CSV TO EXCEL APPDATA DIR Not Set"
export_to_excel_listbox_select_fn_global = "EXPORT CSV TO EXCEL LISTBOX FILE Not Set"
new_excel_file_created_global = "NEW EXCEL FILE CREATED GLOBAL Not Set"

listbox_file_capture_global = False
cm_listbox_file_global = "No Contact List Selected"
dict_filename_global = "No Contact Dictionary"
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
            global listbox_file_capture_global
            global cm_listbox_file_global
            global dict_filename_global
            global master_cm_list_name_global
            global cm_appdatafiles_path_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global
            global fullpath_fn_cm_sw_app_logfile_global
            global export_csv_excel_userprofile_global
            global export_csv_excel_cm_appdata_global
            global export_to_excel_listbox_select_fn_global
            global new_excel_file_created_global

            self.master = master

            self.frame = tk.Frame(self.master)

            # Set Messagebox Font
            self.master.option_add('*Dialog.msg.font', 'Helvetica 16')

            self.master.configure(background='ivory4')
            
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

            self.export_csv_button = Button(self.master, text = "EXPORT CSV for EXCEL", \
                  width=20,height=2, font=('Helvetica', '12'), \
                  background="light sea green", command = self.export_CSV_for_Excel)

            self.export_csv_button.grid(row=1, column=0, sticky=E)

            self.sort_contact_list_button = Button(self.master, text = "SORT Contact List", \
                  width=20,height=2, font=('Helvetica', '12'), \
                  background="light sea green", command = self.sort_Contact_List)

            self.sort_contact_list_button.grid(row=2, column=0, sticky=E)

            self.insert_button = Button(self.master, text = "INSERT DATA", \
                  width=30,height=3, font=('Helvetica', '12'), \
                  background="ivory4", command = self.insert_Data_Entry)
            
            self.insert_button.grid(row=12, column=2, sticky=W)
            

            self.new_window_button = Button(self.master, text = "SELECT\nContact\nList", \
                  width = 8, height = 4, font=minilarge_font, background="ivory4", \
                  fg = "gray25", command = self.new_window)

            self.new_window_button.grid(row=10, column=1, sticky=W)
  

############################################################################################# 
         
            scroll_label = ['>>>>>>>>','>>>>','>>','<<','<<<<','<<<<<<<<']

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
                             width=12,height=2, font=medium_font, \
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
                             width=12,height=2, font=medium_font, \
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
                             speedbutton_6 = Button(self.master, text = c, \
                             width=12,height=2, font=medium_font, \
                             background="royal blue", fg = "SteelBlue1", command = self.backward_fast)
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
            self.myentry = Entry(self.master, textvariable = self.entry_first, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=1, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_last = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_last, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=2, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_streetadd = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_streetadd, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=3, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_citytown = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_citytown, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=4, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_state = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_state, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=5, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_zipcode = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_zipcode, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=6, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_phonenum = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_phonenum, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=7, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_email = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_email, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=8, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_website = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_website, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=9, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")

            self.entry_buildlist = StringVar()
            self.myentry = Entry(self.master, textvariable = self.entry_buildlist, font=large_font, width=35)
            self.myentry.grid(sticky = W, row=10, column=2)
            self.myentry.config(borderwidth=5, background="light sea green")
  

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
      #   SELECT CONTACT LIST from LISTBOX
      #
      #####################################################################################
      # Method to open new window with LISTBOX of cm_list_ files to select a CONTACT LIST.
      def new_window(self):
              self.newWindow = tk.Toplevel(self.master)
              self.cm_app = Demo2(self.newWindow)

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
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            
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
            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
                  return
            
            # PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES 

            inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
            contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

            messagebox.showinfo("Contact Manager Guide ...", \
            "ATTENTION: \n\nSTATUS UPDATE:\nYour Contact Data\nhas been SORTED\nby LAST NAME\n..... Press OK to Continue .....")

            return

      
      def forward_fast(self):
            # (self, event)
            pass
            #print("Executing - forward_fast METHOD")
            #self.report_event(event) 

            
      def forward_scroll(self):
            # (self, event)
            pass
            #print("Executing - forward_scroll METHOD")
            #self.report_event(event)

            
      def forward_tick(self):
            # (self, event)
            pass
            #print("Executing - forward_tick METHOD")
            #self.report_event(event)

            
      def forward_click(self):
            pass
            #print("Executing - forward_click METHOD")
            
            
      def backward_click(self):
            # (self, event)
            pass
            #print("Executing - backward_click METHOD")
            
            
      def backward_tick(self):
            # (self, event)
            pass
            #print("Executing - backward_tick METHOD")
            #self.report_event(event)

            
      def backward_scroll(self):
            # (self, event)
            pass
            #print("Executing - backward_scroll METHOD")
            #self.report_event(event)

            
      def backward_fast(self):
            # (self, event)
            pass
            #print("Executing - backward_fast METHOD")
            #self.report_event(event)

      #
      # KEEP THESE HERE FOR IMPLEMENTING HOVER SCROLL
      #
      #def report_event(self,event):   
      #      print ("Event Time: " + str(event.time) + "  EventType: " + str(event.type) + \
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
            
            if str(dict_filename_global) == "No Contact Dictionary":
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



      
      def finished_Data_Entry(self):
            global cm_listbox_file_global
            global dict_filename_global
            global fullpath_fn_cm_listbox_file_global
            global fullpath_fn_dict_filename_global

            if str(dict_filename_global) == "No Contact Dictionary":
                  messagebox.showinfo("Contact Manager Guide ...", \
                  "ATTENTION: \n\nFirst Please SELECT an existing Contact List\nor Create a New Contact List\nusing the Buttons on the\nLOWER LEFT of your screen")
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
            



# VIEW USERS MANUAL and SYSTEM ADMINISTRATION INFO IN A LARGE SCREEN TEXTBOX  
#
class Demo1(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
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
        
        self.master.configure(background='black')
          
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

        self.title_1_text_box = Text(self.master, width=94, height = 1)
        self.title_1_text_box.grid(row=0, column=0, sticky = W)
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), fg = "black", background="seashell4")
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "     CONTACT MANAGEMENT USERS MANUAL   .....   SYSTEM ADMINISTRATION INFO  "

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the USERS MANUAL and SYSTEM ADMIN INFO

        self.view_text_box = Text(self.master, width=137, height = 28)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '12'), fg = "black", background="seashell4")
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



    def close_windows(self):
        self.master.destroy()




            
# SELECT A CONTACT LIST FILE FROM A LISTBOX
#
class Demo2(object):
    def __init__(self, master):
        global cm_listbox_file_global
        global dict_filename_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        global listbox_file_capture_global
        global master_cm_list_name_global

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
        global master_cm_list_name_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
        # This button command gets the filename_value from
        # below (this Demo2 Class) and sets the
        # CONTACT LIST ENTRY BOX in the App Class
        # USING THE GLOBAL VARIABLE cm_listbox_file_global
        # AND THE LISTBOX WIDGET METHOD: 
        # 
        # cm_filename_value = widget.get(selection[0])
        #
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
        global master_cm_list_name_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
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
        
        self.master.configure(background='ivory4')
        
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
        global master_cm_list_name_global
        global listbox_file_capture_global
        global cm_textbox_newfile_global
        global textbox_newfile_capture_global
        global fullpath_fn_cm_listbox_file_global
        global fullpath_fn_dict_filename_global
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

        # Create APPDATA Path + FILENAME Global for the above File Names using cm_appdatafiles_path_global
        # and be sure to reference this new APPDATA Path + FILENAME Global everywhere we open files
        # which gives us the FULL PATH NAME to our contact_management.py data files. 
       
        fullpath_fn_cm_listbox_file_global = os.path.join(str(cm_appdatafiles_path_global), str(cm_listbox_file_global) )
       
        fullpath_fn_dict_filename_global = os.path.join(str(cm_appdatafiles_path_global), str(dict_filename_global) )
       
        # Create the new Contact List File and add Titles 
        with open(fullpath_fn_cm_listbox_file_global, 'a') as wf_titles:
              wf_titles.flush()
              wf_titles.write("First Name" + "," + "Last Name" + "," + "Street Address" + "," + "City or Town" + "," + "State" + "," + "Zipcode" + "," + "Phone Number" + "," + "Email" + "," + "Website" + "," + "\n")


        
        # Open the File for Contact DICTIONARY Filename dict_filename_global
        with open(fullpath_fn_dict_filename_global, 'a') as new_wdictf:
              new_wdictf.flush()
              new_wdictf.write("\n")
        
                        
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
        
        self.master.configure(background='blue4')
          
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
        self.title_1_text_box.config(borderwidth=10, font=('Helvetica', '18'), fg = "dodger blue", background="blue4")
        self.title_1_text_box.config(state=NORMAL)  # Enable TEXT WIDGET for Insert
        self.title_1_text_box.delete(1.0, END)      # Clear the TEXT WIDGET of Data

        text_1_TITLE = "CONTACT LIST:  " + str(cm_listbox_file_global) + "    DICTIONARY: " + str(dict_filename_global) 

        self.title_1_text_box.insert(END, text_1_TITLE)
        self.title_1_text_box.config(state=DISABLED)  # Disable TEXT WIDGET for Insert

        
        # TEXTBOX to view the DICTIONARY FILE corresponding
        # to the current CONTACT LIST SELECTED or CREATED

        self.view_text_box = Text(self.master, width=95, height = 19)
        self.view_text_box.grid(row=2, column=0, sticky = W)
        self.view_text_box.config(borderwidth=10, font=('Helvetica', '18'), fg = "dodger blue", background="blue4")
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
        # We should see the dictionary printed when an excel spreadsheet is generated. 
        #
        #####################################################################################################

        ######### PLACE THESE TWO LINES ABOVE OR WHEREVER WE WANT TO SORT AND RE-WRITE DATA FILES
        #########
        ######### inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
        ######### contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()

        #####################################################################################################
        
        #   print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
        #   for key, value in contact_dict_acquired.items():
        #       print("\n")
        #       print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)   

        #print("\n")
        #print("\n")
        #for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
        #      print(" .... **** SORTED INSTANTIATED DICTIONARY **** .... =  :  " + str(s) ) 
  

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
  # We should see the dictionary printed when an excel spreadsheet is generated.
  #
  #####################################################################################################
  #
  #   inst_Process_Dict_File = Process_Dict_File(fullpath_fn_dict_filename_global)
  #   contact_dict_acquired = inst_Process_Dict_File.read_target_dict_file()
  #
  #   print("\n" + "FROM INSTANTIATION OF CLASS :  Process_Dict_File ....... DICTIONARY GENERATED FROM dict_file_ READ:" + "\n")
  #   for key, value in contact_dict_acquired.items():
  #       print("\n")
  #       print('    ', key, 'is the INSTANTION key for the INSTANTIATION CLASS value', value)
  #       
  #   
  #   print("\n")
  #   print("\n")
  #   for s in sorted(contact_dict_acquired.items(), key=lambda k_v: k_v[1]["Last_Name_KEY"]):
  #         print(" .... SORTED INSTANTIATED DICTIONARY  =  :  " + str(s) ) 
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

            ############################################################################
                                       
            
              return dict_of_dictionaries
 
      ##########################################################################  
      #
      # Method to MAP from DICTIONARY OF DICTIONARIES to dict_file_ Format and
      # write the (eventually) newly SORTED dict_of_dictionaries to dict_file_
      #
      #def write_target_dict_file(self, new_target_dict_file_string): 
            #self.target_dict_file_string = new_target_dict_file_string
            #return




def main(): 
      global listbox_file_capture_global
      global cm_listbox_file_global
      global username_global
      global userprofile_global
      global appdata_path_global
      global cm_appdatafiles_path_global
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
      # in the program execution to monitor or debug.
      with open(str(fullpath_fn_cm_sw_app_logfile_global), 'w') as cmlogfile:
            cmlogfile.write("\n_____________________________________________________________________________\n")
            cmlogfile.write("\n" + ".... (Python) System.Version = " + str(sys.version) )
            cmlogfile.write("\n" + ".... (Windows) System.Platform = " + str(sys.platform) )
            cmlogfile.write("\n_____________________________________________________________________________\n")
            cmlogfile.write("\n" + ".... Contact Management Workstation Enterprise Cloud Software Application")
            cmlogfile.write("\n" + ".... Date : Time :  " + str(datetime.datetime.now() ) )
            cmlogfile.write("\n_____________________________________________________________________________\n")
            cmlogfile.write("\n.... USERNAME = " + str(username_global) )
            cmlogfile.write("\n.... USER HOME PATH = " + str(userprofile_global) )
            cmlogfile.write("\n.... APPDATA PATH = " + str(appdata_path_global) )
            cmlogfile.write("\n.... CONTACT MANAGEMENT DATA PATH = " + str(cm_appdatafiles_path_global) )
            cmlogfile.write("\n.... LOGFILE PATH = " + str(fullpath_fn_cm_sw_app_logfile_global) )
            cmlogfile.write("\n.... EXCEL OUTPUT PATH (AppData) = " + str(export_csv_excel_cm_appdata_global) )
            cmlogfile.write("\n.... EXCEL OUTPUT PATH (UserProfile) = " + str(export_csv_excel_userprofile_global) )
            cmlogfile.write("\n_____________________________________________________________________________\n")

 
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
           while 1:
                # setting Contact List Entry Widget String from LISTBOX FILE GLOBAL - str(cm_listbox_file_global)
                cm_app.entry_buildlist.set(str(master_cm_list_name_global) )
                listbox_file_capture_global = False
                time.sleep(.1)

      t = threading.Thread(name='UPDATE_CM_LIST_NAME_ENTRY_TEXTBOX_THREAD', target=cm_filename_worker, daemon=True)
      t.start()

      root.mainloop()


    

if __name__ == '__main__':
    main()
        
                       

