import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import csv
import pandas as pd
import easygui
from csv import writer
import csv
import os
import os.path


def on_closing():
    if messagebox.askokcancel("Do yo really wanna quit?"):
        if os.path.isfile('final_project/process/02.csv'):
            os.remove('final_project/process/02.csv')
            root.destroy()
        else:
            root.destroy()




class App:
    def __init__(self, root):
        global GLineEdit_873
        global GLineEdit_874
        global GLineEdit_1
        #setting title
        root.title("XO")
        #setting window size
        width=885
        height=612
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "Player 2 please login"
        GLabel_656.place(x=350, y=20, width=250, height=39)

        # Username input
        GLabel_434 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Username"
        GLabel_434.place(x=380, y=70, width=125, height=49)

        GLineEdit_873 = tk.Entry(root)
        GLineEdit_873["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_873["font"] = ft
        GLineEdit_873["fg"] = "#333333"
        GLineEdit_873["justify"] = "center"
        GLineEdit_873["text"] = "Type your name here"
        GLineEdit_873.place(x=360, y=120, width=173, height=35)

        # Id input
        GLabel_434 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "ID"
        GLabel_434.place(x=600, y=70, width=50, height=49)

        GLineEdit_1 = tk.Entry(root)
        GLineEdit_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_1["font"] = ft
        GLineEdit_1["fg"] = "#333333"
        GLineEdit_1["justify"] = "center"
        GLineEdit_1["text"] = "Entry"
        GLineEdit_1.place(x=600, y=120, width=50, height=35)

        # Password entry
        GLabel_434 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Password"
        GLabel_434.place(x=380, y=170, width=125, height=49)

        GLineEdit_874 = tk.Entry(root)
        GLineEdit_874["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_874["font"] = ft
        GLineEdit_874["fg"] = "#333333"
        GLineEdit_874["justify"] = "center"
        GLineEdit_874["show"] = "*"
        GLineEdit_874["text"] = "Type your password here"
        GLineEdit_874.place(x=360, y=220, width=173, height=35)

        # Submit
        GButton_124 = tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Submit"
        GButton_124.place(x=380, y=270, width=121, height=50)
        GButton_124["command"] = self.GButton_125_command


        # Login bottons
    def GButton_125_command(self):
        from csv import writer
        global GLineEdit_873
        global GLineEdit_874
        global GLineEdit_1

        col_list = ["name"]

        dbfile89 = pd.read_csv("final_project/process/01.csv", usecols=col_list)
        # CheckLogin

        dbfile = pd.read_csv('final_project/Database/users.csv')

        names = list(dbfile.Username)
        passwords = list(dbfile.Password)
        ids = int(GLineEdit_1.get()) - 1
        print(names)
        print(passwords)

        if GLineEdit_873.get() != str(dbfile89["name"][0]):
            if (GLineEdit_873.get() in names) and (GLineEdit_874.get() == passwords[ids]):
                print("Both correct")
                header = ['id','name','uid']
                data=[1, GLineEdit_873.get(),GLineEdit_1.get()]

                # Open our existing CSV file in append mode
                # Create a file object for this file
                with open('final_project/process/02.csv', 'w', encoding='UTF8') as f:
                    writer = csv.writer(f)

                    # write the header
                    writer.writerow(header)

                    # write the data
                    writer.writerow(data)
                import Multiplayer

            else:
                easygui.msgbox("Incorrect password and/or username please try again.", title="Error")
            lines = list()
            col_list = ["id"]

            dbfile = pd.read_csv("final_project/process/02.csv", usecols=col_list)

            remove = [dbfile["id"][0]]

            with open('final_project/process/02.csv', 'r') as read_file:
                reader = csv.reader(read_file)
                for row_number, row in enumerate(reader, start=0):
                    if (row_number not in remove):
                        lines.append(row)

            with open('final_project/process/02.csv', 'w') as write_file:
                writer = csv.writer(write_file)
                writer.writerows(lines)
        else:
            easygui.msgbox("You can not play against yourself", title="Error")






root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
app = App(root)
root.mainloop()
