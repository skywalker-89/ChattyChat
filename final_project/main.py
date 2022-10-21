from email import header
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import pandas as pd
from csv import writer
import easygui
import csv, operator
from tkinter import END
from tkinter import messagebox
import os
import os.path


#necessities
filename = "final_project/Database/users.csv"
fields = ['Username', 'Password', 'uid', 'records']

def sortingdata():
    # importing pandas package
    import pandas as pandasForSortingCSV
    import pandas as pd
    from csv import writer

    # assign dataset
    csvData = pandasForSortingCSV.read_csv("final_project/Database/users.csv")
    # sort data frame
    csvData.sort_values(["points"],
                        axis=0,
                        ascending=[False],
                        inplace=True)

    header = ['uid','Username','Password','win','lose','draw','points']
    with open('final_project/Database/sorted_data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)



    # displaying unsorted data frame
    print("\nBefore sorting:")
    print(csvData)


    df = pd.DataFrame(csvData)
    df.to_csv('final_project/Database/sorted_data.csv', mode='a', index=False, header=False)

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.homepage()

#pages
    def homepage(self):
        for i in self.master.winfo_children():
            i.destroy()
        #set title
        root.title("XO")
        #setting window size
        width=885
        height=612
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        sortingdata()

        # First label
        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "XO game"
        GLabel_656.place(x=350, y=20, width=178, height=39)

        # Leader Board
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Leader Board"
        GLabel_497.place(x=360, y=26, width=150, height=44)
        #uid label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "ID"
        GLabel_497.place(x=300, y=80, width=30, height=44)

        #uid table list
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=300, y=120, width=30, height=332)

        col_list = ["uid"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["uid"][item])

        #username label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Name"
        GLabel_497.place(x=350, y=80, width=30, height=44)

        #username table list
        GListBox_225 = tk.Listbox(root)
        GListBox_225["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_225["font"] = ft
        GListBox_225["fg"] = "#333333"
        GListBox_225["justify"] = "center"
        GListBox_225.place(x=330, y=120, width=100, height=332)

        col_list = ["Username"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_225.insert(END,userdata["Username"][item])

        #Win label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Win|"
        GLabel_497.place(x=430, y=80, width=30, height=44)

        #win
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=430, y=120, width=30, height=332)

        col_list = ["win"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["win"][item])

        #Lose label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Lose|"
        GLabel_497.place(x=460, y=80, width=30, height=44)

        #lose
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=460, y=120, width=30, height=332)

        col_list = ["lose"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["lose"][item])

        #Draw label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Draw|"
        GLabel_497.place(x=490, y=80, width=30, height=44)

        #draw
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=490, y=120, width=35, height=332)

        col_list = ["draw"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["draw"][item])

        #Points label
        GLabel_498 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_498["font"] = ft
        GLabel_498["fg"] = "#333333"
        GLabel_498["justify"] = "center"
        GLabel_498["text"] = "Points"
        GLabel_498.place(x=520, y=80, width=35, height=44)

        #points
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=520, y=120, width=30, height=332)

        col_list = ["points"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["points"][item])




        # Login
        GButton_307 = tk.Button(root)
        GButton_307["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_307["font"] = ft
        GButton_307["fg"] = "#000000"
        GButton_307["justify"] = "center"
        GButton_307["text"] = "Login"
        GButton_307.place(x=50, y=80, width=121, height=50)
        GButton_307["command"] = self.GButton_307_command

        # Register
        GButton_628 = tk.Button(root)
        GButton_628["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_628["font"] = ft
        GButton_628["fg"] = "#000000"
        GButton_628["justify"] = "center"
        GButton_628["text"] = "Register"
        GButton_628.place(x=50, y=160, width=120, height=49)
        GButton_628["command"] = self.GButton_628_command

        # Quick play
        GButton_124 = tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Quick Play PVP"
        GButton_124.place(x=50, y=240, width=150, height=49)
        GButton_124["command"] = self.GButton_124_command

    def loginpage(self):
        global GLineEdit_873
        global GLineEdit_874
        global GLineEdit_9
        for i in self.master.winfo_children():
            i.destroy()
        GLabel_656=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "XO game"
        GLabel_656.place(x=350,y=20,width=178,height=39)


        #Username input
        GLabel_434=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Username"
        GLabel_434.place(x=380,y=70,width=125,height=49)

        GLineEdit_873=tk.Entry(root)
        GLineEdit_873["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_873["font"] = ft
        GLineEdit_873["fg"] = "#333333"
        GLineEdit_873["justify"] = "center"
        GLineEdit_873["text"] = "Type your name here"
        GLineEdit_873.place(x=360,y=120,width=173,height=35)

        #Id input
        GLabel_434=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "ID"
        GLabel_434.place(x=600,y=70,width=50,height=49)

        GLineEdit_9=tk.Entry(root)
        GLineEdit_9["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_9["font"] = ft
        GLineEdit_9["fg"] = "#333333"
        GLineEdit_9["justify"] = "center"
        GLineEdit_9["text"] = "Entry"
        GLineEdit_9.place(x=600,y=120,width=50,height=35)

        #Password entry
        GLabel_434=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Password"
        GLabel_434.place(x=380,y=170,width=125,height=49)

        GLineEdit_874=tk.Entry(root)
        GLineEdit_874["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_874["font"] = ft
        GLineEdit_874["fg"] = "#333333"
        GLineEdit_874["justify"] = "center"
        GLineEdit_874["show"]="*"
        GLineEdit_874["text"] = "Type your password here"
        GLineEdit_874.place(x=360,y=220,width=173,height=35)


        #Submit
        GButton_124=tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Submit"
        GButton_124.place(x=380,y=270,width=121,height=50)
        GButton_124["command"] = self.GButton_125_command

        #BackHome
        GButton_124=tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Home"
        GButton_124.place(x=380,y=320,width=121,height=50)
        GButton_124["command"] = self.GButton_126_command

    def registerpage(self):
        global GLineEdit_875
        global GLineEdit_876
        for i in self.master.winfo_children():
            i.destroy()
        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "XO game"
        GLabel_656.place(x=350, y=20, width=178, height=39)


        # Username input
        GLabel_434 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Username"
        GLabel_434.place(x=380, y=70, width=125, height=49)
        #userinput
        GLineEdit_875 = tk.Entry(root)
        GLineEdit_875["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_875["font"] = ft
        GLineEdit_875["fg"] = "#333333"
        GLineEdit_875["justify"] = "center"
        GLineEdit_875["text"] = "Type your name here"
        GLineEdit_875.place(x=360, y=120, width=173, height=35)



        # Password entry
        GLabel_434 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_434["font"] = ft
        GLabel_434["fg"] = "#333333"
        GLabel_434["justify"] = "center"
        GLabel_434["text"] = "Password"
        GLabel_434.place(x=380, y=170, width=125, height=49)
        #userinput
        GLineEdit_876 = tk.Entry(root)
        GLineEdit_876["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_876["font"] = ft
        GLineEdit_876["fg"] = "#333333"
        GLineEdit_876["justify"] = "center"
        GLineEdit_876["show"]="*"
        GLineEdit_876["text"] = "Type your password here"
        GLineEdit_876.place(x=360, y=220, width=173, height=35)



        # Submit
        GButton_124 = tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Submit"
        GButton_124.place(x=380, y=270, width=121, height=50)
        GButton_124["command"] = self.GButton_127_command

        # BackHome
        GButton_124 = tk.Button(root)
        GButton_124["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_124["font"] = ft
        GButton_124["fg"] = "#000000"
        GButton_124["justify"] = "center"
        GButton_124["text"] = "Home"
        GButton_124.place(x=380, y=320, width=121, height=50)
        GButton_124["command"] = self.GButton_128_command

    def userhome(self):
        for i in self.master.winfo_children():
            i.destroy()

        col_list = ["name"]

        dbfile = pd.read_csv("final_project/process/01.csv", usecols=col_list)

        # setting title
        root.title("X O")
        # setting window size
        width = 885
        height = 612
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # First label
        GLabel_656 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_656["font"] = ft
        GLabel_656["fg"] = "#333333"
        GLabel_656["justify"] = "center"
        GLabel_656["text"] = "Hello  " + str(dbfile["name"][0])
        GLabel_656.place(x=350, y=2, width=178, height=39)


        # QuickPlay
        GButton_888 = tk.Button(root)
        GButton_888["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_888["font"] = ft
        GButton_888["fg"] = "#000000"
        GButton_888["justify"] = "center"
        GButton_888["text"] = "Quick Play PVP"
        GButton_888.place(x=50, y=80, width=121, height=50)
        GButton_888["command"] = self.GButton_888_command

        # Multiplayer
        GButton_700 = tk.Button(root)
        GButton_700["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_700["font"] = ft
        GButton_700["fg"] = "#000000"
        GButton_700["justify"] = "center"
        GButton_700["text"] = "Multiplayer Play"
        GButton_700.place(x=50, y=160, width=121, height=50)
        GButton_700["command"] = self.GButton_700_command

        # LogOut
        GButton_300 = tk.Button(root)
        GButton_300["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_300["font"] = ft
        GButton_300["fg"] = "#000000"
        GButton_300["justify"] = "center"
        GButton_300["text"] = "Logout"
        GButton_300.place(x=50, y=240, width=121, height=50)
        GButton_300["command"] = self.GButton_300_command

         # Leader Board
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Leader Board"
        GLabel_497.place(x=360, y=26, width=150, height=44)
        #uid label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "ID"
        GLabel_497.place(x=300, y=80, width=30, height=44)

        #uid table list
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=300, y=120, width=30, height=332)

        col_list = ["uid"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["uid"][item])

        #username label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Name"
        GLabel_497.place(x=350, y=80, width=30, height=44)

        #username table list
        GListBox_225 = tk.Listbox(root)
        GListBox_225["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_225["font"] = ft
        GListBox_225["fg"] = "#333333"
        GListBox_225["justify"] = "center"
        GListBox_225.place(x=330, y=120, width=100, height=332)

        col_list = ["Username"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_225.insert(END,userdata["Username"][item])

        #Win label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Win|"
        GLabel_497.place(x=430, y=80, width=30, height=44)

        #win
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=430, y=120, width=30, height=332)

        col_list = ["win"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["win"][item])

        #Lose label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Lose|"
        GLabel_497.place(x=460, y=80, width=30, height=44)

        #lose
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=460, y=120, width=30, height=332)

        col_list = ["lose"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["lose"][item])

        #Draw label
        GLabel_497 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "center"
        GLabel_497["text"] = "Draw|"
        GLabel_497.place(x=490, y=80, width=30, height=44)

        #draw
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=490, y=120, width=35, height=332)

        col_list = ["draw"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["draw"][item])

        #Points label
        GLabel_498 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_498["font"] = ft
        GLabel_498["fg"] = "#333333"
        GLabel_498["justify"] = "center"
        GLabel_498["text"] = "Points"
        GLabel_498.place(x=520, y=80, width=35, height=44)

        #points
        GListBox_224 = tk.Listbox(root)
        GListBox_224["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_224["font"] = ft
        GListBox_224["fg"] = "#333333"
        GListBox_224["justify"] = "center"
        GListBox_224.place(x=520, y=120, width=30, height=332)

        col_list = ["points"]
        userdata = pd.read_csv('final_project/Database/sorted_data.csv', usecols=col_list)

        for item in range(len(userdata)):
            GListBox_224.insert(END,userdata["points"][item])



#Buttons

#Home Bottons
    #login Botton
    def GButton_307_command(self):
        self.loginpage()
    #Register Botton
    def GButton_628_command(self):
        self.registerpage()
    #quick game button
    def GButton_124_command(self):
        import quickplay1v1

#Login page bottons
    # Login bottons
    def GButton_125_command(self):
        global GLineEdit_873
        global GLineEdit_874
        global GLineEdit_9
        #CheckLogin

        dbfile = pd.read_csv('final_project/Database/users.csv')

        names = list(dbfile.Username)
        passwords = list(dbfile.Password)
        ids=int(GLineEdit_9.get())-1
        print(names)
        print(passwords)


        if (GLineEdit_873.get() in names) and (GLineEdit_874.get() == passwords[ids]):
            print("Both correct")
            header = ['id','name','uid']
            data=[1, GLineEdit_873.get(),GLineEdit_9.get()]

            with open('final_project/process/01.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write the data
                writer.writerow(data)

            self.userhome()
        else:
            easygui.msgbox("Incorrect password and/or username please try again.", title="Error")

    # BackHome
    def GButton_126_command(self):
        update_board()
        self.homepage()

#Register page buttons
    #Subbmit
    def GButton_127_command(self):
        global GLineEdit_875
        global GLineEdit_876

        # writing to csv file
        dbfile = pd.read_csv('final_project/Database/users.csv')

        rowscount = len(dbfile)

        # List
        List = [rowscount+1, GLineEdit_875.get(),GLineEdit_876.get() ,0,0,0,0]

        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open('final_project/Database/users.csv', 'a') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)

            # Close the file object
            f_object.close()
        easygui.msgbox("Register complete please return home to login", title="Success")


    #BackHome
    def GButton_128_command(self):
            update_board()
            self.homepage()

#Main User Buttons
    #Quickplay
    def GButton_888_command(self):
        import quickplay1v1

    #Multiplayer play
    def GButton_700_command(self):
        import player2login

    #LogOut
    def GButton_300_command(self):
        os.remove('final_project/process/01.csv')
        update_board()
        self.homepage()


def on_closing():
    update_board()
    if messagebox.askokcancel("Do yo really wanna quit?"):
        
        if os.path.isfile('final_project/process/01.csv'):
            os.remove('final_project/process/01.csv')
            root.destroy()
        else:
            root.destroy()

def update_board():
    if os.path.isfile('final_project/Database/sorted_data.csv'):
        os.remove('final_project/Database/sorted_data.csv')
        root.destroy()
    else:
        root.destroy()


root = Tk()
root.protocol("WM_DELETE_WINDOW",on_closing)
app(root)
root.mainloop()