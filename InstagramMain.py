import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
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


def postButton():
    time.sleep(5)
    postButton = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
    postButton.click()
    selectImage()

def selectImage():
    time.sleep(5)
    selection = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
    #selection.click()

    imagePath = []
    pathToPictures = os.listdir("uploadpictures") #list
    for pic in pathToPictures:
        extraPath = "\\" 
        print(extraPath + pic)
        imagePath.append(extraPath + pic) 
    #uploadImage =Image.open(r"C:\Users\Jack Ryan\Desktop\Coding\Python\InstagramUploadBot\Uploadpictures" + imagePath[1])
    inputImage = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage.send_keys("C:\\Users\\Jack Ryan\\Desktop\\Coding\\Python\\InstagramUploadBot\\Uploadpictures" + imagePath[1] )


        # here I get the path to the desired directory from user input, but it could come from elsewhere
    #path_to_directory = Path(input("C:\Users\Jack Ryan\Pictures\Uploadpictures"))

    #extension_of_interest = ".png"
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

time.sleep(3)
login(loginEmail, loginPassword)

#saveInfo()
#notifcations()












#path = os.listdir("uploadpictures")
#print(path)
#lala = 0
#for i in path:
    #if i == "Hwlllo.txt":
       # b = i
        #print(b)


#File_object = open(r"File_Name", "Access_Mode")
