from tkinter import *
root = Tk()
root.geometry("300x300")
def infoStuff(email, password):
    global userEmail
    global userPassword
    
    temp1 = email.get()
    userEmail = str(temp1)

    temp2 = password.get()
    userPassword = str(temp2)
    root.destroy()

def van():
    global account 
    account = "v"

def midwest():
    global account
    account = "m"
    

def start(startButton, label):
    label.destroy()
    startButton.destroy()
    infoText = Label(root, text="Please give me your email and password")
    infoText.grid(row=0, column=1) 
    email = Entry(root, width=50)
    email.grid(row=1, column=1)
    password = Entry(root, width=50)
    password.grid(row=2,column=1)
    passwordText = Label(root, text="Password:")
    passwordText.grid(row=2,column=0)
    emailText = Label(root, text="Email")
    emailText.grid(row=1,column=0)
    vanButton = Button(root, text="Van", command=lambda: van() )
    vanButton.grid(row=4, column=0)
    midwestButton = Button(root, text = "Midwest", command=lambda: midwest() )
    midwestButton.grid(row=5, column=0)
    enter = Button(root, text="Enter", command=lambda: infoStuff(email, password))
    enter.grid(row=5,column=1)
   
    

def main():
    label = Label(root, text="Hello please click the Start button below ")
    label.grid(row=0, column=0)
    startButton = Button(root, text="Start", command=lambda: start(startButton, label))
    startButton.grid(row=1, column=0)

main()

root.mainloop()