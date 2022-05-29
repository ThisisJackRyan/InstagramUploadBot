import os
import time
import keyring #work on this 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows
#chromedriverPath = "/Users/jackcryan/Downloads/chromeDrivers/chromedriver" #For Mac


def bot(loginEmail,loginPassword, accountCaption):
    #loginEmail= mainPage.userEmail
    #loginPassword = mainPage.userPassword
    #pickCaption = mainPage.account

    print(loginEmail)
    print(loginPassword)
    print(accountCaption)
 


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
        time.sleep(3)
        captionLocation = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
        captionLocation.send_keys(accountCaption)
        share()

    def share():
        print("test share")
        time.sleep(3)
        sharebutton = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        sharebutton.click()
        time.sleep(15)
        exit = driver.find_element_by_xpath("/html/body/div[6]/div[1]/button")
        exit.click()
        time.sleep(15)
        return
        

        
    time.sleep(3)
    login(loginEmail, loginPassword)
print("intresting")