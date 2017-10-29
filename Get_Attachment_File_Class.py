#
#
#
################################################################################################################
#
# Author: Michael Hughes 
#
# Program:  Get_Attachment_File_Class
#
# Methods:  a_dialog_to_get_file_attachment.py 
#
# Version: 1.0
#   
# Date: October 29, 2017 
#
# Description: tk program to open dialog windows to get a file.
# that can be used as an attachment.
#
# returns:  FILE NAME (FULL PATH):  file_full_path
#
# Language: Python 3.6.2
#
#
# Example Use Case:
#
#    def main():
#        root = tk.Tk()
#        root.withdraw()
#        create_Get_Attachment_File_Class_object = Get_Attachment_File_Class(root)
#        target_file_full_path = create_Get_Attachment_File_Class_object.a_dialog_to_get_file_attachment()
#        class_file_full_path = create_Get_Attachment_File_Class_object.full_path_of_filename_for_attachment
#
#
#        print("\n")
#        print("**************************************************************************************************************")
#        print(".... FILE (FULL PATH) from METHOD - " + str(target_file_full_path) )
#        print("**************************************************************************************************************")
#        print(".... FILE (FULL PATH) from CLASS - " + str(class_file_full_path) )
#        print("**************************************************************************************************************") 
#
#
#
# if __name__ == '__main__':
#     main()
#         
#
###############################################################################################################

import os
import tkinter as tk
from tkinter import filedialog

class Get_Attachment_File_Class(object):

      def __init__(self, master):
          self.full_path_of_filename_for_attachment = "full_path_of_filename_for_attachment_NOT_SET"


      def a_dialog_to_get_file_attachment(self):

          ###########   Select a Directory:

          root = tk.Tk()
          root.withdraw()
          home_dir = os.path.expanduser('~')
          dirname = filedialog.askdirectory(parent=root,initialdir=home_dir,title='Please select a directory')

          directory_full_path = os.path.join(str(home_dir), str(dirname) )

          print("\n\n\n")
          print(".... DIRECTORY (FULL PATH): " + str(directory_full_path) )


          ############   Select a File for Opening:

          root = tk.Tk()
          root.withdraw()
          file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')

          io_buffer_filepath_string = str(file)

          # print(".... io_buffer_filepath_string = str(file): " + str(io_buffer_filepath_string) ) 

          splitting_this_off_of_right_side  = "'>"

          splitting_this_off_of_left_side = str(directory_full_path) + "/"

          splitting_off_left_side = io_buffer_filepath_string.split(str(splitting_this_off_of_left_side) )[1]

          just_the_file_name = splitting_off_left_side.split(str(splitting_this_off_of_right_side) )[0]

          file_type = just_the_file_name.split(".")[1]

          print(".... FILE TYPE: " + str(file_type) )

          print(".... FILE NAME: " + str(just_the_file_name) )

          file_full_path = str(directory_full_path) + "/" + str(just_the_file_name)

          print(".... FILE (FULL PATH): " + str(file_full_path) )

          print("\n")
          print("**************************************************************************************************************")
          print(".... return file_full_path - FILE (FULL PATH) - " + str(file_full_path) )
          print("**************************************************************************************************************")

          
          self.full_path_of_filename_for_attachment = file_full_path
          
          # return file_full_path 

          return file_full_path



      
def main():
    root = tk.Tk()
    root.withdraw()
    create_Get_Attachment_File_Class_object = Get_Attachment_File_Class(root)
    target_file_full_path = create_Get_Attachment_File_Class_object.a_dialog_to_get_file_attachment()
    class_file_full_path = create_Get_Attachment_File_Class_object.full_path_of_filename_for_attachment

    print("\n")
    print("**************************************************************************************************************")
    print(".... FILE (FULL PATH) from METHOD - " + str(target_file_full_path) )
    print("**************************************************************************************************************")
    print(".... FILE (FULL PATH) from CLASS - " + str(class_file_full_path) )
    print("**************************************************************************************************************")
 


if __name__ == '__main__':
    main()
        
              


