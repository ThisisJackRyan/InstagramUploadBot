from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



chromeDriverPath = "C:\Program Files (x86)\chromedriver.exe"

loginEmail = input("What is your Email?")
loginPassword =  input("What is your password")
accountCaption = input("give me your caption")






def findIt(id):
    try:
        name = "ID"
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, id))
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

findIt("loginForm")

#Logging in to the Account
instagramEmail = driver.find_element(By.NAME, "username")
instagramPassword = driver.find_element(By.NAME, "password")

instagramEmail.send_keys(loginEmail)
instagramPassword.send_keys(loginPassword)
instagramPassword.send_keys(Keys.RETURN)


#click the post icon
findIt("ssrb_root_start") #instagram has doesn't have any Id's that get add on new page. May have to rethink findIT()? 
postButton = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a')
postButton.click()




print()
print("Done!")
print()