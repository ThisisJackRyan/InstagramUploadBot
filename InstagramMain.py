import os
import time
import userInterface
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows
#chromedriverPath = "/Users/jackcryan/Downloads/chromeDrivers/chromedriver" #For Mac

loginEmail= userInterface.userEmail
loginPassword = userInterface.userPassword
print(loginEmail)
print(loginPassword)
pickCaption = userInterface.account
print(pickCaption)



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
    selectImage()


def postButton():
    time.sleep(5)
    postButton = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
    postButton.click()

def selectImage():
    imagePath = []
    pathToPictures = os.listdir("uploadpictures") #list
    num = 0
    for pic in pathToPictures:
        postButton()
        extraPath = "\\" 
        print(extraPath + pic)
        imagePath.append(extraPath + pic) 
        uploadImage(num, imagePath)
        num += 1


def uploadImage(num, imagePath):
    inputImage = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage.send_keys("C:\\Users\\Jack Ryan\\Desktop\\Coding\\Python\\InstagramUploadBot\\Uploadpictures" + imagePath[num] )
    next()

def next():
    time.sleep(2)
    firstNext = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
    firstNext.click()
    time.sleep(2)
    secondNext = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
    secondNext.click()
    caption()

def caption():
    if pickCaption == 'm':
        time.sleep(3)
        midwestCaption()
    elif pickCaption == 'v':
        time.sleep(3)
        vanCaption()
    else:
        print(" Please only type m or v ")
        time.sleep(3)
        caption()

def midwestCaption():
    midwestCaption = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
    midwestCaption.send_keys("Follow For More!!!")
    i = 0
    while i < 10:
        midwestCaption.send_keys(Keys.RETURN)
        midwestCaption.send_keys(".")
        i += 1

    midwestCaption.send_keys(Keys.RETURN)
    midwestCaption.send_keys("#midwest #midwestlife #midwestisthebest #camping #campinglife #campinglove #campinglife⛺️ #camp #hiking #hikingadventures #fishing #fish #fishinglife #northdakota #southdakota #minnesota #wisconsin #michigan #ohio #indiana #iowa #nebraska #kansas #missouri ")
    share()

def vanCaption():
    vanCaption = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
    vanCaption.send_keys("Follow For More!!!")
    i = 0
    while i < 10:
        vanCaption.send_keys(Keys.RETURN)
        vanCaption.send_keys(".")
        i += 1
        
    vanCaption.send_keys(Keys.RETURN)
    vanCaption.send_keys("#vanlife #fishing #camping #campinglife #campingtrip #campinggear #campinglife⛺️ #campinglove #camp #hiking #hikingadventures #suzuki #vwbus #volkswagen #van #buslife #buslifeadventure #busliving #campervan #campervanlife ")
    share()

def share():
    time.sleep(3)
    sharebutton = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
    sharebutton.click()
    time.sleep(10)
    exit = driver.find_element_by_xpath("/html/body/div[6]/div[1]/button")
    exit.click()
    time.sleep(15)
    return
    

       
time.sleep(3)
login(loginEmail, loginPassword)