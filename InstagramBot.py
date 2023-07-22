import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



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



def postImages(pic):


    #click the post icon
    findItXPATH("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a") #instagram has doesn't have any Id's that get add on new page. May have to rethink findIT()? 
    postButton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a')
    postButton.click()

    extraSlash = "\\"
    print(extraSlash + pic)
    imagePath.append(extraSlash + pic)
    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input")
    inputImage.send_keys("C:\\Users\\Jack Ryan\\Desktop\\Coding\\Python\\InstagramUploadBot\\Uploadpictures" + imagePath[num] )

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
    shareButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div")
    shareButton.click()

    findItXPATH("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")
    exit = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div")
    exit.click()


imagePath = []
pathToPictures = os.listdir("uploadpictures")
num = 0
for pic in pathToPictures:
        postImages(pic)
        num+=1





print()
print("Done!")
print()