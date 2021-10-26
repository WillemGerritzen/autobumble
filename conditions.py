import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

import auth
from driver import Driver
import json


class Conditions(Driver):

    def __init__(self):
        self.wait = WebDriverWait(self.driver, 5)
        self.conditions = self._open_cond()

    def cond_eval(self, condition: str) -> bool:
        """
        Template to evaluate conditions
        :return: True if the c is within range, False otherwise
        """
        pass

    def cond_find(self, condition: str) -> str or None:
        """
        Template to find conditions
        :return: None
        """
        xpath = self.conditions[condition]['xpath']
        typ = type(self.conditions[condition]['value'])

        if self.conditions[condition]['page'] == 2:
            inter = self.wait.until(ec.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[2]/div[2]")))
            inter.click()

        try:
            element = self.wait.until(ec.presence_of_element_located((By.XPATH, xpath))).text  # Avoid returning a comma
            return element.get_attribute('text')

        except NoSuchElementException or TimeoutException:
            return None

    @staticmethod
    def _open_cond() -> dict:
        """
        Opens the JSON file with the conditions and returns them as a dictionary
        :return: The conditions for swiping
        """
        with open('./conditions.json', 'r') as file:
            conditions = json.load(file)
        return conditions


if __name__ == '__main__':
    Driver.driver.get('https://bumble.com')
    auth = auth.Auth()
    auth.signin()
    cond = Conditions()
    height = cond.cond_find('looking')
    print(height)

# TODO: Scrape the whole profile and then evaluate
