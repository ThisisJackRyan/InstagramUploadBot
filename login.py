import keyring
from tkinter import *
import pickle

root = Tk()
root.geometry("300x300")

def main():
   blank = Label(root,width=7) 
   blank.grid(row=0,column=0)
   createAccount = Button(root, text="Create Account", width=12, command=lambda: createAccountLogin(createAccount,blank, loginButton) )
   createAccount.grid(row=0,column=1,)
   loginButton = Button(root, text="Login", width=12,command =lambda: login(createAccount,blank, loginButton))
   loginButton.grid(row=0,column=2, )

def createAccountLogin(a,b,c):
    a.destroy()
    b.destroy()
    c.destroy()
    infoText = Label(root, text="Please give me your Username and Password")
    infoText.grid(row=0, column=1) 
    username = Entry(root, width=50)
    username.grid(row=1, column=1)
    password = Entry(root, width=50)
    password.grid(row=2,column=1)
    passwordText = Label(root, text="Password:")
    passwordText.grid(row=2,column=0)
    usernameText = Label(root, text="Username")
    usernameText.grid(row=1,column=0)
    enter = Button(root, text="Enter", command=lambda: push(username, password))
    enter.grid(row=5,column=1)

def push(u,p):
    tempU = u.get()
    tempP = p.get()
    keyring.set_password("python", "username", tempU)
    keyring.set_password("python", 'password', tempP)
    

def login(a,b,c):
    a.destroy()
    b.destroy()
    c.destroy()
    infoText = Label(root, text="Please give me your Username and Password")
    infoText.grid(row=0, column=1, sticky="w") 
    username = Entry(root, width=50)
    username.grid(row=1, column=1)
    password = Entry(root, width=50)
    password.grid(row=2,column=1)
    passwordText = Label(root, text="Password:")
    passwordText.grid(row=2,column=0)
    usernameText = Label(root, text="Username")
    usernameText.grid(row=1,column=0)
    enter = Button(root, text="Enter", command=lambda: check(username, password))
    enter.grid(row=5,column=1)
    Username = keyring.get_password("python", "username")
    Password = keyring.get_password("python", "password")
    print("username:" + Username)
    print("password:" + Password)

    
def check(u,p):
    tempU = u.get()
    tempP = p.get()
    username = keyring.get_password("python", "username")
    password = keyring.get_password("python", "password")
    if username == tempU:
        if password == tempP:
            root.destroy()
            import mainPage

main()
root.mainloop()