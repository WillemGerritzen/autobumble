from selenium import webdriver
from time import sleep
from os import environ


class Login:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def login(self) -> None:
        """
        Walks through the login process using preset environment variables as credentials
        :return: None
        """

        try:
            # Find and click the sign-in button
            sign_in = self.driver.find_element_by_xpath(
                '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
            sign_in.click()
            sleep(1)

            # Find and click the Facebook button
            facebook = self.driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span')
            facebook.click()
            sleep(1)

            # Switch to the pop-up
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Find and click the Accept all button
            accept = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
            accept.click()
            sleep(1)

            # Find the username and password fields, and the login button
            fb_username = self.driver.find_element_by_xpath('//*[@id="email"]')
            fb_pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
            fb_login = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')

            # Fill the fields with their relevant variables, and click login
            fb_username.send_keys(environ['FB_USER'])
            fb_pwd.send_keys(environ['FB_PWD'])
            fb_login.click()

        except Exception as e:
            # If an error occurs, close the window and raise it
            # self.driver.quit()
            raise e
