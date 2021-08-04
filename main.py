from selenium import webdriver
from time import sleep
from login import Login
from swipe import Swipe


driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


if __name__ == '__main__':
    driver.get('https://bumble.com')
    Login(driver).login()
    sleep(7)
    Swipe(driver).swipe_right()
