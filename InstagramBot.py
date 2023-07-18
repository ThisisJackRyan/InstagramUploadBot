from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



chromeDriverPath = "C:\Program Files (x86)\chromedriver.exe"

loginEmail = input("What is your Email?")
loginPassword = input("What is your password")
accountCaption = input("give me your caption")






def findIt(id):
    try:
        WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, id))
        print("Found it!")
    except:
        print("")
        print("--ERROR--")
        print("Was not able to locate element in time")

try:
    driver = webdriver.Chrome(chromeDriverPath)
    driver.get("https://www.instagram.com/")

except:
    print("")
    print("--ERROR--")
    print("Out Dated Driver or No Wifi connection")

findIt("loginForm")



print()
print("Done!")
print()