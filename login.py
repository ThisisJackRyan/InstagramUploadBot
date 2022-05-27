import keyring
from tkinter import *
import pickle



root = Tk()
root.geometry("300x300")

# loas main screen should be a good spot of adding a cool lofing because it looks very blank
def main():
    #put picture of logo here
    removeMainAccount = Button(root, text = "Remove Account", width =12, command =getName )
    removeMainAccount.grid(row=0,column=1)
    loginButton = Button(root, text="Login", width=12,command =lambda: login(loginButton, removeMainAccount))
    loginButton.grid(row=0,column=2, )

#for testing purposes
def remove(n):
    tempN =n.get()
    keyring.delete_password(tempN, "username")
    keyring.delete_password(tempN, "password")
    print("password Deleted")


def getName():
    name = Entry(root, width=35)
    nameText=Label(root, text = "Name")
    name.grid(row=1,column=2)
    nameText.grid(row=1,column=1)
    enter = Button(root, text="Enter", command=lambda: remove(name))
    enter.grid(row=2,column=1)


def login(a,b):
    a.destroy()
    b.destroy()
    infoText = Label(root, text="Please give me your Username and Password")
    infoText.grid(row=0, column=1, sticky="w") 
    name = Entry(root, width=50)
    name.grid(row=1, column=1)
    nameText=Label(root, text="Name:")
    nameText.grid(row=1,column=0)
    username = Entry(root, width=50)
    username.grid(row=2, column=1)
    password = Entry(root, width=50)
    password.grid(row=3,column=1)
    passwordText = Label(root, text="Password:")
    passwordText.grid(row=3,column=0)
    usernameText = Label(root, text="Username")
    usernameText.grid(row=2,column=0)
    enter = Button(root, text="Enter", command=lambda: check(name, username, password))
    enter.grid(row=5,column=1)


def check(n,u,p):
    tempN = n.get()
    tempU = u.get()
    tempP = p.get()
    username = keyring.get_password(tempN, "username")
    password = keyring.get_password(tempN, "password")
    if username == tempU:
        if password == tempP:
            root.destroy()
            import mainPage
main()
root.mainloop()