import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Path = "C:\Program Files (x86)\chromedriver.exe" #for Windows
Path = "/Users/jackcryan/Downloads/chromeDrivers/chromedriver"
driver = webdriver.Chrome(Path)

#driver.get("https://github.com/login")
#Email = driver.find_element_by_name("login")
#password = driver.find_element_by_name("password")
#Email.send_keys("thisisjackryan1@gmail.com")
#password.send_keys("nODDOG1021")
#password.send_keys(Keys.RETURN)


driver.get("https://www.instagram.com/")
time.sleep(5)
instaEmail = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
instapassword = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
instaEmail.send_keys("thisisjackryan@icloud.com")
instapassword.send_keys("nODDOG1021")
instapassword.send_keys(Keys.RETURN)

time.sleep(10)

notNow = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notNow.click()

time.sleep(3)

notifictationNotNow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
notifictationNotNow.click()
#this poped up twice so fix that 



path = os.listdir("uploadpictures")
print(path)
lala = 0
for i in path:
    if i == "Hwlllo.txt":
        b = i
        print(b)


#File_object = open(r"File_Name", "Access_Mode")
