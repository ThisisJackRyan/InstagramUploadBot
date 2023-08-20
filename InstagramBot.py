import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import json


if(input("What Device are you on? (1 for Mac)  (2 for Windows)") == 1):
    chromeDriverPath = "/usr/local/bin/chromedriver.exe"
else:
    chromeDriverPath = "C:\Program Files (x86)\chromedriver.exe"



loginEmail = input("What is your Email? ")
loginPassword =  input("What is your password? ")
#accountCaption = input("give me your caption? ")
accountCaption = '''
Follow For More!!!
.
.
.
.
.
.
.
.
.
.
#vanlife #fishing #camping #campinglife #campingtrip #campinggear #campinglife⛺️ 
#campinglove #camp #hiking #hikingadventures #suzuki #vwbus #volkswagen #van 
#buslife #buslifeadventure #busliving #campervan #campervanlife 
'''

#this is an example of the type of json that will be passed from InstagramBotOptions.jsx to this file.

Options = {
            "Options" : {
                "type": "SinglePicture",
                "ratio": "OriginalSizing",
                "images": "img",#this will be an array of images
                "imageURL": "imgURL" #this will be an array of imageURLs
            }
        }
with open("sample.json", "w") as outfile:
    json.dump(Options, outfile)

with open('sample.json', 'r') as openfile:
    loadedOptions = json.load(openfile)




def findItXPATH(id):
    try:
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, id))
        print("Found it!")
        print()
    except:
        print()
        print("--ERROR--")
        print("Was not able to locate element in time")
        print()

try:
    driver = webdriver.Chrome(chromeDriverPath)
    driver.get("https://www.instagram.com/")

except:
    print("")
    print("--ERROR--")
    print("Out Dated Driver or No Wifi connection")

#findIt("loginForm")
findItXPATH("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")

#Logging in to the Account
instagramEmail = driver.find_element(By.NAME, "username")
instagramPassword = driver.find_element(By.NAME, "password")

instagramEmail.send_keys(loginEmail)
instagramPassword.send_keys(loginPassword)
instagramPassword.send_keys(Keys.RETURN)








def jsonFunction():
     print(loadedOptions["Options"]["type"])

def SinglePicture():
    print("SinglePicture")
def Video():
    print("Video")
def Carousel():
    print("Carousel")


def OriginalSizing():
    print("OriginalSizing")
    originalSizing = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]")
    originalSizing.click()
    PostIt()
def FourByFive():
    print("4:5")
    fourByFive = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]")
    fourByFive.click()
    PostIt()
def SixteenByNine():
    print("16:9")
    sixteenByNine = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]")
    sixteenByNine.click()
    PostIt()


def postImages(pic):

    #click the post icon
    findItXPATH("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a") #instagram has doesn't have any Id's that get add on new page. May have to rethink findIT()? 
    postButton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a')
    postButton.click()

    #image logic
    extraSlash = "\\"
    print(extraSlash + pic)
    imagePath.append(extraSlash + pic)
    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage.send_keys("C:\\Users\\Jack Ryan\\Desktop\\Coding\\Python\\InstagramUploadBot\\Uploadpictures" + imagePath[num] )



    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button")
    ratioButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button")
    ratioButton.click()
    #logic of type,ration needs to go here
    match(loadedOptions["Options"]["type"]):
        case "SinglePicture":
            SinglePicture()
        case "Video":
            Video()
        case "Carousel":
            Carousel()
    
    match(loadedOptions["Options"]["ratio"]):
        case "OriginalSizing":
            OriginalSizing()
        #Default
        case "1:1":
            print("1:1")
            PostIt()
        case "4:5":
            FourByFive()
        case "16:9":
            SixteenByNine()










def PostIt():      
    #Click the next button twice 
    firstNext = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
    firstNext.click()
    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
    secondNext = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div')
    secondNext.click()

    #putting caption into text box
    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]")
    captionLocation = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]")
    captionLocation.send_keys(accountCaption)

    #Share the IMAGE!!!
    #shareButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
    #shareButton.click()

    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span")
    exit = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")
    exit.click()


imagePath = []
pathToPictures = os.listdir("uploadpictures")
num = 0
for pic in pathToPictures:
        postImages(pic)
        num+=1

jsonFunction()




print()
print("Done!")
print()