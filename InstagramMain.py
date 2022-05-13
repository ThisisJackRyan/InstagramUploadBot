import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows
#chromedriverPath = "/Users/jackcryan/Downloads/chromeDrivers/chromedriver" #For Mac



loginEmail = input("What is your login Email")
loginPassword = input("What is your login Password")


driver = webdriver.Chrome(chromedriverPath)
driver.get("https://www.instagram.com/")

def login(email, password):
    instaEmail = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    instapassword = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    time.sleep(2)
    instaEmail.send_keys(email)
    time.sleep(2)
    instapassword.send_keys(password)
    time.sleep(2)
    instapassword.send_keys(Keys.RETURN)
    postButton()

def saveInfo():
    notNow = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    notNow.click()


def notifcations():
    notifictationNotNow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    notifictationNotNow.click()

def postButton():
    time.sleep(5)
    postButton = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
    postButton.click()
    selectImage()

def selectImage():
    time.sleep(5)
    selection = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
    selection.click()
        # here I get the path to the desired directory from user input, but it could come from elsewhere
    #path_to_directory = Path(input("enter the path to the folder : "))

    #extension_of_interest = ".jpg"
   # filepaths_of_interest = []

   # for entry in path_to_directory.iterdir():
        #if entry.is_file() and entry.name.endswith(extension_of_interest):
           # print("match: " + str(entry))
            #filepaths_of_interest.append(entry)
       # else:
           # print("ignored: " + str(entry))

   # print("now opening ...")
    #for filepath_of_interest in filepaths_of_interest:
      #  os.startfile(filepath_of_interest, "open")

time.sleep(5)
login(loginEmail, loginPassword)

#saveInfo()
#notifcations()












path = os.listdir("uploadpictures")
print(path)
lala = 0
for i in path:
    if i == "Hwlllo.txt":
        b = i
        print(b)


#File_object = open(r"File_Name", "Access_Mode")
