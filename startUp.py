import keyring
from tkinter import *
from login import main

root =Tk()
root.geometry("300x300")

def startUp():
    l = Label(root, text = "Thanks for Downloading my Bot")
    l.grid(row=0,column=0)
    c = Label(root, text='Click the Button Below to create an account')
    c.grid(row=1,column=0)
    b = Button(root, text="Create Account", command=lambda:createMainAccount(l,c, b))
    b.grid(row=2,column=0)

def createMainAccount(l,c,b):
    l.destroy()
    c.destroy()
    b.destroy()
    nameText = Label(root, text = "Your Name:")
    nameText.grid(row=1,column=0, sticky="se")
    usernameText = Label(root, text = "Username:")
    usernameText.grid(row=2,column=0,sticky="se")
    passwordText = Label(root, text = "Password:")
    passwordText.grid(row=3,column=0,sticky="se")
    enter = Button(root, text= "Enter", command = lambda: push(name,username,password))
    enter.grid(row=4,column=0)

    name = Entry(root, width=35)
    name.grid(row=1, column=1)
    username = Entry(root, width=35)
    username.grid(row=2, column=1)
    password = Entry(root, width=35)
    password.grid(row=3, column=1)
   

    def push(n,u,p):
        tempN = n.get()
        tempU = u.get()
        tempP = p.get()
        keyring.set_password(tempN, "username", tempU)
        keyring.set_password(tempN, "password", tempP)

        print("name:" + tempN)
        print("username: " + tempU)
        print("password: " + tempP)
        root.destroy()
        main()


startUp()
root.mainloop()