#import login
import keyring
import pickle
from tkinter import *
from InstagramMain import *


def mainInterface(nameOfUser):


    root = Tk()
    #root.geometry("500x400")
    

    #print email and password this is for testing purposes
    def printY(value):
        name = accounts[value]
        e = keyring.get_password(name,"email")
        p = keyring.get_password(name,"password")
        print(e)
        print(p)
        
    def getEmail(value):
        name = accounts[value]
        return keyring.get_password(name, "email")

    def getPassword(value):
        name = accounts[value]
        return keyring.get_password(name, "password")

    def getCaption(value):
        return captions[value]



    #outputs the list on the side of display -- needs to make so that it can be updated
    def accountList():
        num = 0
        n = len(accounts)
        for a in accounts:
            accbutton = Button(root, text=a,width=15,command=lambda k=num:thisAccount(k))
            accbutton.grid(row=num,column=0)
            num+=1
        addAccount = Button(root, text="Add Account", width=15, command=lambda: newAccount())
        addAccount.grid(row=num+1,column=0)
    
    #entries for a new account
    def newAccount():
        name = Entry(root, width = 40 )
        name.grid(row=1,column=2)
        nameText = Label(root, text = "Name:")
        nameText.grid(row=1,column=1, sticky="se")
        email = Entry(root, width = 40 )
        email.grid(row=2,column=2)
        emailText = Label(root, text = "Email:")
        emailText.grid(row=2,column=1,sticky="se")
        password = Entry(root, width = 40 )
        password.grid(row=3,column=2)
        passwordText = Label(root, text = "Password:")
        passwordText.grid(row=3,column=1,sticky="se")
        caption = Text(root, width =30, height= 10)
        caption.grid(row=4, column=2, sticky ="w")
        captionText =Label(root, text ="Caption:")
        captionText.grid(row=4, column=1)
        addAccount = Button(root, text="Add Account", command=lambda: addNewAccount(name, email, password, caption))
        addAccount.grid(row=5,column=1)

    #shoves it into the software
    def addNewAccount(n,e,p,c):
        tempN = n.get()
        tempE = e.get()
        tempP = p.get()
        tempC = c.get("1.0","end-1c")
        print(tempC)

        accounts.append(tempN)
        captions.append(tempC)
        keyring.set_password(tempN, "email", tempE)
        keyring.set_password(tempN, "password", tempP)
        print(accounts)
        print(captions)
        updatePickle()
        


    #Shows name, email, password and has buttons to remove or edit 
    def thisAccount(value):
        printY(value)
        names = accounts[value]
        name = Label(root, text=names, width = 40 )
        name.grid(row=1,column=2)
        nameText = Label(root, text = "Name:")
        nameText.grid(row=1,column=1, sticky="se")
        email = Label(root, text=getEmail(value), width = 40 )
        email.grid(row=2,column=2)
        emailText = Label(root, text = "Email:")
        emailText.grid(row=2,column=1,sticky="se")
        password = Label(root, text=getPassword(value),  width = 40 )
        password.grid(row=3,column=2)
        passwordText = Label(root, text = "Password:")
        passwordText.grid(row=3,column=1,sticky="se")
        edit = Button(root, text="edit", command=lambda: editInfo(name, email, password,caption, value))
        edit.grid(row=5,column=1)
        post = Button(root, text="Post", command=lambda: postPic(value))
        post.grid(row=6, column=1)
        caption = Label(root, text=getCaption(value))
        caption.grid(row=4, column=2,)
        captionText =Label(root, text ="Caption:")
        captionText.grid(row=4, column=1, sticky="w")


    def postPic(value):
        email = getEmail(value)
        password = getPassword(value)
        root.destroy()
        accountCaption = captions[value]
        bot(email,password, accountCaption )




    #looks for change in name -- needs to be fixed with thisAccount() function
    def editInfo(n,e,p, c, value):
        n.destroy()
        e.destroy()
        p.destroy()
        c.destroy()
        name = accounts[value]

        editName = Entry(root, width=40)
        editName.grid(row=1,column=2)
        editName.insert(0, name)

        editEmail = Entry(root, width=40)
        editEmail.grid(row=2, column=2)
        editEmail.insert(0, getEmail(value))
        
        editPassword = Entry(root, width = 40)
        editPassword.grid(row=3, column=2)
        editPassword.insert(0, getPassword(value))

        editCaption = Text(root, width =30, height= 10)
        editCaption.grid(row=4, column=2, sticky ="w")
        editCaption.insert(INSERT, getCaption(value))

        update = Button(root,text="Update", command=lambda: updatePasswords(value, editName, editEmail, editPassword, editCaption))
        update.grid(row=5, column=1)
        removeButton = Button(root, text="Remove", command= lambda: removeAccount(value))
        removeButton.grid(row=6, column=1)

        
    #removes account from list and calls to update pickle
    def removeAccount(value):
        print(value)
        accounts.pop(value)
        captions.pop(value)
        updatePickle()


    def updatePasswords(value, n,e,p,c):
        tempN = n.get()
        tempE = e.get()
        tempP = p.get()
        tempC = c.get("1.0","end-1c")

        oldN = accounts[value]
        oldC = captions[value]
        oldE = getEmail(value)
        oldP = getPassword(value)


        if oldN != tempN:
            accounts[value] = tempN
            keyring.delete_password(oldN, "email")
            keyring.delete_password(oldN, "password")
            keyring.set_password(tempN, "email", tempE)
            keyring.set_password(tempN, "password", tempP)
            oldE = tempE
            oldP = tempP

        if oldE != tempE:
            keyring.delete_password(oldN, "email")
            keyring.set_password(oldN, "email", tempE)

        if oldP != tempP:
            keyring.delete_password(oldN, "password")
            keyring.set_password(oldN, "password", tempP)
        if oldC != tempC:
            captions[value] = tempC
        updatePickle()

    #updates the pickled list
    def updatePickle():
        print(captions)
        print("dumping")
        with open(pickleAccountsFileName, "wb")as accountsList:
            pickle.dump(accounts, accountsList)
        with open(pickleCaptionsFileName, "wb")as captionsList:
            pickle.dump(captions, captionsList)

    
    pickleAccountsFileName = "accounts" + nameOfUser
    pickleCaptionsFileName = "captions" + nameOfUser
    try:
        print("loading")
        with open(pickleAccountsFileName, "rb")as accountsList:
            accounts =  pickle.load(accountsList)
            if accounts == None:
                print("New List after Loading")
                accounts = []
        
    except:
        print("New lsit for dumping")
        accounts = []
        with open(pickleAccountsFileName, "wb")as accountsList:
            pickle.dump(accounts, accountsList)
    

    try:
        with open(pickleCaptionsFileName, "rb")as captionsList:
            captions = pickle.load(captionsList)
        print("old caption List")
    except:
        print("New Captions List")
        captions = []
        with open(pickleCaptionsFileName, "wb")as captionsList:
            pickle.dump(captions, captionsList)


        

    #this is for testing sake
    #length = len(accounts)
    #if length > 5:
        #accounts.clear()

    print(accounts)
    accountList()
    root.mainloop()