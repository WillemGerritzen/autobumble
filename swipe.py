from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Swipe:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def right(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            right = wait.until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')))
            right.click()

        except Exception as e:
            self.driver.quit()
            raise e

    def left(self):
        pass
