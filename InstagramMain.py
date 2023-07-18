import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" 



#lots of sleep for page to load. Sometimes has issues on bad wifi

def bot(loginEmail,loginPassword, accountCaption):

    print(loginEmail)
    print(loginPassword)
    print(accountCaption)
 


    driver = webdriver.Chrome(chromedriverPath)
    driver.get("https://www.instagram.com/")

    def login(email, password):
        time.sleep(5)
        instaEmail = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        instapassword = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        time.sleep(2)
        instaEmail.send_keys(email)
        time.sleep(2)
        instapassword.send_keys(password)
        time.sleep(2)
        instapassword.send_keys(Keys.RETURN)
        selectImage()


    def postButton():
        time.sleep(5)
        postButton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a')
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
        #location of Image and where to upload
        time.sleep(2)
        inputImage = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input")
        inputImage.send_keys("C:\\Users\\Jack Ryan\\Desktop\\Coding\\Python\\InstagramUploadBot\\Uploadpictures" + imagePath[num] )

        time.sleep(2)

        #click the next button twice
        firstNext = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
        firstNext.click()
        time.sleep(2)
        secondNext = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div')
        secondNext.click()

        time.sleep(3)

        #putting pickled caption into text box
        captionLocation = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]")
        captionLocation.send_keys(accountCaption)
        
        time.sleep(3)

        #Share the IMAGE!!!
        sharebutton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
        sharebutton.click()
        time.sleep(30)

        #exit and restart head back to for each loop
        exit = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")
        exit.click()
        time.sleep(30)
        return

    time.sleep(3)
    login(loginEmail, loginPassword)