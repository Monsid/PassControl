from pynput.keyboard import Key, Controller
import time
import sys
import os
from tkinter import *
import io
import functools
from cryptography.fernet import Fernet

def opening2write():

    global windows
    windows=Tk()
    windows.title("Create New Login Credentials")
    windows.configure(background="black")

    Label (windows, text="Name this set of login credentials (e.g Facebook/Google/Email/Netflix)", bg="black", fg="white", font="none 14 bold") .grid(row=0, column=0, sticky=W)
    global textEntry1
    textEntry1 = Entry(windows, width=20, font=("none", 14), bg="white")
    textEntry1.grid(row=1, column=0, sticky=W)

    Label(windows, text="Please type Username/Email", bg="black",
          fg="white", font="none 14 bold").grid(row=2, column=0, sticky=W)
    global textEntry2
    textEntry2 = Entry(windows, width=20, font=("none", 14), bg="white")
    textEntry2.grid(row=3, column=0, sticky=W)

    Label(windows, text="Please type Password", bg="black",
          fg="white", font="none 14 bold").grid(row=4, column=0, sticky=W)
    global textEntry3
    textEntry3 = Entry(windows, width=20, font=("none", 14), bg="white")
    textEntry3.grid(row=5, column=0, sticky=W)
    #save button
    Button(windows, text=" Save Credentials ", width=50, font=("none", 14), command=opening2writes).grid(row=3, column=1, sticky=W)
    def closededed():
        windows.destroy()
    Button(windows, text=" Close ", width=50, font=("none", 14), command=closededed).grid(row=4, column=1, sticky=W)


def opening2writes():

    key = b'5Ciyf8PzHxDCYm2ja_N1IJC14uITPqpHWnpSIceXLTA='
    NameTheSecret = textEntry1.get()
    Filename = NameTheSecret + ".key"
    StringToJoin = textEntry2.get() + "|"
    StringToJoin2 = textEntry3.get()
    StringToWrite = StringToJoin + StringToJoin2
    CRYPTED = StringToWrite.encode()
    f = Fernet(key)
    encrypted = f.encrypt(CRYPTED)
    d = open(Filename, "wb")
    d.write(encrypted)
    windows.destroy()

def View_these_secrets():


    global files
    files = [f for f in os.listdir('.') if f.endswith(".key")
             if os.path.isfile(f)]

    maxi = 0
    buffer = io.StringIO()
    for num, lines in enumerate(files):
        needvar = (num, lines)
        print (needvar, file=buffer)
        if maxi < num:
            maxi = num

    textss = buffer.getvalue()

    global windowy
    windowy=Tk()
    windowy.title("SHOW CREDENTIALS")
    windowy.configure(background="black")
    output = Text(windowy, width=75, height=6, wrap=WORD, background="white", font=("none", 14))
    output.grid(row=0, column=0, columnspan=2, sticky=W)
    output.insert(END, textss)
    output["state"] = DISABLED

    Label(windowy, text="Which line (e.g 0, 1, 2, 3, etc) would you like to read?", bg="black",
          fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)
    global textEntry4
    textEntry4 = Entry(windowy, width=20, bg="white")
    textEntry4.grid(row=2, column=0, sticky=W)

    output2 = Text(windowy, width=75, height=6, wrap=WORD, background="white", font=("none", 14))
    output2.grid(row=3, column=0, columnspan=2, sticky=W)
    output2["state"] = DISABLED

    def button_press():

        key = b'5Ciyf8PzHxDCYm2ja_N1IJC14uITPqpHWnpSIceXLTA='
        buffer2 = io.StringIO()
        set_var = (files[int(textEntry4.get())])
        file_object = open(set_var, "rb")
        encrypted = file_object.read()

        f2 = Fernet(key)
        decrypted = f2.decrypt(encrypted)
        original_message = decrypted.decode()
        credsss = (original_message).replace("|", "\n") + "\n"

        print(credsss, file=buffer2)
        texty = buffer2.getvalue()
        output2["state"] = NORMAL
        output2.delete(0.0, END)
        output2.insert(END, texty)
        output2["state"] = DISABLED

    def closeded():
        windowy.destroy()
    Button(windowy, text=" Read ", width=25, command=button_press).grid(row=1, column=2, sticky=W)
    Button(windowy, text=" Close ", width=25, command=closeded).grid(row=2, column=2, sticky=W)


def WriteOut():
    def pinrto(name):

        key = b'5Ciyf8PzHxDCYm2ja_N1IJC14uITPqpHWnpSIceXLTA='
        set_var1 = str(name)
        keyboard = Controller()
        print("5 seconds till type out")
        time.sleep(5)

        reked = set_var1.split("'",1)[-1].replace("'","").replace(")", "").replace('"', '')

        file_object = open(reked, "rb")
        encrypted = file_object.read()

        f2 = Fernet(key)
        decrypted = f2.decrypt(encrypted)
        original_message = decrypted.decode()
        credsss = (original_message).replace("|", "\t") + "\n"
        keyboard.type(credsss)

    global windower
    windower = Tk()
    windower.title("Type For Me")
    windower.configure(background="black")

    global files
    files = [f for f in os.listdir('.') if f.endswith(".key")
             if os.path.isfile(f)]


    for num, lines in enumerate(files):
        needvar = (num, lines)
        specubuton = Button(windower,text=needvar, width=50, font=("none", 14), command=functools.partial(pinrto, needvar))
        specubuton.pack()


def main():

    window = Tk()
    window.title("PassController_V1.0")
    window.configure(background = "black")
    Label(window, text="Welcome to PassController_V1.0", bg="black",
          fg="green", font="none 16 bold").grid(row=1, column=0, sticky=W)

    Label(window, text="1 New Login Credentials | 2 Show Credentials list | 3 Type-out Credentials for me", bg="black",
          fg="green", font="none 12 bold").grid(row=2, column=0, sticky=W)

    Button(window, text=" 1 New Login Credentials ", width= 65, font=("none", 14), command=opening2write) .grid(row=3, column=0, sticky=W)

    Button(window, text=" 2 Show Credentials list ", width=65, font=("none", 14), command=View_these_secrets) .grid(row=4, column=0, sticky=W)

    Button(window, text=" 3 Type-out Credentials for me ", width=65, font=("none", 14), command=WriteOut).grid(row=5, column=0, sticky=W)

    window.mainloop()

main()