import tkinter as tk
import tkinter.messagebox
from tkinter.tix import COLUMN
import pandas as pd
col_list = ["name","id","uid"]

dbfile = pd.read_csv("final_project/process/01.csv", usecols=col_list)

col_list = ["name","id","uid"]

dbfile2 = pd.read_csv("final_project/process/02.csv", usecols=col_list)


window = tk.Tk()
window.title('X O')
frame = tk.Frame(master=window)
frame.pack(pady=10)

label = tk.Label(master=frame, text=str(dbfile["name"][0]) + " VS " + str(dbfile2["name"][0]), font=("Arial", 15))
label.pack()

frame1 = tk.Frame(master=window, borderwidth=2, relief=tk.SUNKEN, bg='#dadec3')
frame1.pack(padx=10, pady=10)

button1 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(1))
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(2))
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(3))
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(4))
button4.grid(row=1, column=0, padx=5, pady=5)

button5 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(5))
button5.grid(row=1, column=1, padx=5, pady=5)

button6 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(6))
button6.grid(row=1, column=2, padx=5, pady=5)

button7 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(7))
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(8))
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: buttonclick(9))
button9.grid(row=2, column=2, padx=5, pady=5)

frame2 = tk.Frame(master=window, border=2, relief=tk.SUNKEN, bg='#dadec3')
frame2.pack()
label1 = tk.Label(master=frame2, text=str(dbfile["name"][0]) +"--> X\n"+str(dbfile2["name"][0])+"--> O", width=15)
label1.grid(row=0, column=0, padx=5)
button_restart = tk.Button(master=frame2, text="Restart", width=10, height=3, relief=tk.GROOVE,
                           command=lambda: restartbutton())
button_restart.grid(row=0, column=1, padx=10, pady=10)
label2 = tk.Label(master=frame2, text=str(dbfile["name"][0])+' Turn', bg="skyblue", width=10, height=3, relief=tk.SUNKEN,font=('', 8))
label2.grid(row=0, column=2, padx=5)
a = 1
b = 0
c = 0


def disablebutton():
    button1['state'] = tk.DISABLED
    button2['state'] = tk.DISABLED
    button3['state'] = tk.DISABLED
    button4['state'] = tk.DISABLED
    button5['state'] = tk.DISABLED
    button6['state'] = tk.DISABLED
    button7['state'] = tk.DISABLED
    button8['state'] = tk.DISABLED
    button9['state'] = tk.DISABLED


def restartbutton():
    global a, b, c
    a = 1
    b = 0
    c = 0
    label2['bg'] = "skyblue"
    label2['text'] = str(dbfile["name"][0])+' Turn'
    button1['text'] = ''
    button1['bg'] = 'white'
    button2['text'] = ''
    button2['bg'] = 'white'
    button3['text'] = ''
    button3['bg'] = 'white'
    button4['text'] = ''
    button4['bg'] = 'white'
    button5['text'] = ''
    button5['bg'] = 'white'
    button6['text'] = ''
    button6['bg'] = 'white'
    button7['text'] = ''
    button7['bg'] = 'white'
    button8['text'] = ''
    button8['bg'] = 'white'
    button9['text'] = ''
    button9['bg'] = 'white'
    button1['state'] = tk.NORMAL
    button2['state'] = tk.NORMAL
    button3['state'] = tk.NORMAL
    button4['state'] = tk.NORMAL
    button5['state'] = tk.NORMAL
    button6['state'] = tk.NORMAL
    button7['state'] = tk.NORMAL
    button8['state'] = tk.NORMAL
    button9['state'] = tk.NORMAL


def buttonclick(x):
    global a, b, c
    # for player 1
    if (x == 1 and a == 1 and button1['text'] == ''):
        button1['text'] = "X"
        button1['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 2 and a == 1 and button2['text'] == ''):
        button2['text'] = "X"
        button2['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 3 and a == 1 and button3['text'] == ''):
        button3['text'] = "X"
        button3['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 4 and a == 1 and button4['text'] == ''):
        button4['text'] = "X"
        button4['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 5 and a == 1 and button5['text'] == ''):
        button5['text'] = "X"
        button5['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 6 and a == 1 and button6['text'] == ''):
        button6['text'] = "X"
        button6['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 7 and a == 1 and button7['text'] == ''):
        button7['text'] = "X"
        button7['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 8 and a == 1 and button8['text'] == ''):
        button8['text'] = "X"
        button8['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1
    if (x == 9 and a == 1 and button9['text'] == ''):
        button9['text'] = "X"
        button9['bg'] = "skyblue"
        label2['bg'] = "#e8956f"
        label2['text'] = str(dbfile2["name"][0])+' Turn'
        a = 0
        b += 1

    # for player 2
    if (x == 1 and a == 0 and button1['text'] == ''):
        button1['text'] = 'O'
        button1['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 2 and a == 0 and button2['text'] == ''):
        button2['text'] = 'O'
        button2['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 3 and a == 0 and button3['text'] == ''):
        button3['text'] = 'O'
        button3['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 4 and a == 0 and button4['text'] == ''):
        button4['text'] = 'O'
        button4['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 5 and a == 0 and button5['text'] == ''):
        button5['text'] = 'O'
        button5['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 6 and a == 0 and button6['text'] == ''):
        button6['text'] = 'O'
        button6['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 7 and a == 0 and button7['text'] == ''):
        button7['text'] = 'O'
        button7['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 8 and a == 0 and button8['text'] == ''):
        button8['text'] = 'O'
        button8['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1
    if (x == 9 and a == 0 and button9['text'] == ''):
        button9['text'] = 'O'
        button9['bg'] = "#e8956f"
        label2['bg'] = "skyblue"
        label2['text'] = str(dbfile["name"][0])+' Turn'
        a = 1
        b += 1

    # checking winner
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        disablebutton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is "+str(dbfile["name"][0]))
        dbfile_send = pd.read_csv('final_project/Database/users.csv',index_col='uid')
        points= list(dbfile_send.points)
        win = list(dbfile_send.win)
        lose = list(dbfile_send.lose)
        the_id = int(dbfile["uid"][0])
        the_id2 = int(dbfile2["uid"][0])
        the_idx = int(dbfile["uid"][0])-1
        the_id2x = int(dbfile2["uid"][0])-1
        print(the_id)
        print(the_id2)
        player1_point = points[the_idx] + 3
        print(player1_point)
        player1_win = win[the_idx]+1
        player2_lose = lose[the_id2x]+1
        dbfile_send.loc[the_id,'win'] = player1_win
        dbfile_send.loc[the_id,'points'] = player1_point
        dbfile_send.loc[the_id2,'lose'] = player2_lose
        dbfile_send.to_csv('final_project/Database/users.csv')

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        disablebutton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Winner is "+str(dbfile2["name"][0]))
        dbfile_send = pd.read_csv('final_project/Database/users.csv',index_col='uid')
        points= list(dbfile_send.points)
        win = list(dbfile_send.win)
        lose = list(dbfile_send.lose)
        the_id2 = int(dbfile2["uid"][0])
        the_id = int(dbfile["uid"][0])
        the_idx = int(dbfile["uid"][0])-1
        the_id2x = int(dbfile2["uid"][0])-1
        player2_point = points[the_id2x] + 3
        player2_win = win[the_id2x]+1
        player1_lose = lose[the_idx]+1
        print(player1_lose)
        print(player2_point)
        dbfile_send.loc[the_id2,'win'] = player2_win
        dbfile_send.loc[the_id2,'points'] = player2_point
        dbfile_send.loc[the_id,'lose'] = player1_lose
        dbfile_send.to_csv('final_project/Database/users.csv')


    elif (b == 9):
        disablebutton()
        c = 1
        tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")
        dbfile_send = pd.read_csv('final_project/Database/users.csv', index_col='uid')
        points= list(dbfile_send.points)
        draw = list(dbfile_send.draw)
        the_id = int(dbfile["uid"][0])
        the_id2 = int(dbfile2["uid"][0])
        the_idx = int(dbfile["uid"][0])-1
        the_id2x = int(dbfile2["uid"][0])-1
        player1_point = points[the_idx] + 1
        player1_draw = draw[the_idx]+1
        player2_point = points[the_id2x]+1
        player2_draw = points[the_id2x]+1
        dbfile_send.loc[the_id,'points'] = player1_point
        dbfile_send.loc[the_id,'draw'] = player1_draw
        dbfile_send.loc[the_id2,'points'] = player2_point
        dbfile_send.loc[the_id2,'draw']= player2_draw
        dbfile_send.to_csv('final_project/Database/users.csv')



window.mainloop()