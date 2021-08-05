from selenium import webdriver
from time import sleep
from os import environ
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException


class Login:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def login(self) -> None:
        """
        Walks through the login process using preset environment variables as credentials
        :return: None
        """

        wait = WebDriverWait(driver, 10)

        try:
            # Find and click the sign-in button
            sign_in = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')))
            sign_in.click()

            # Find and click the Facebook button
            facebook = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span')))
            facebook.click()

            # Switch to the pop-up
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Find and click the Accept all button

            accept = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')))
            accept.click()

            try:
                # Find the username and password fields, and the login button
                fb_username = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
                fb_pwd = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
                fb_login = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')))

                # Fill the fields with their relevant variables, and click login
                fb_username.send_keys(environ['FB_USER'])
                fb_pwd.send_keys(environ['FB_PWD'])
                fb_login.click()

            except StaleElementReferenceException:
                accept = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[3]')))
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, accept)

            # Switch back to main window
            self.driver.switch_to.window(self.driver.window_handles[0])

            # TODO: Add a check for 'session expired' thing

            expiry_check = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[1]/div/div[2]/div/div/div/section/div/div/div/div/div')))
            expiry_check.click()


        except Exception as e:
            # If an error occurs, close the window and raise it
            # self.driver.quit()
            raise e


if __name__ == '__main__':
    from util import Util
    util = Util()
    driver = util.set_driver()
    driver.get('https://bumble.com')
    Login(driver).login()
