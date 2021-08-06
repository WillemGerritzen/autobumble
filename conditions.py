from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from driver import Driver


class Conditions(Driver):
    def __init__(self):
        self.wait = WebDriverWait(self.driver, 5)

    def cond_eval(self) -> bool:
        """
        Template to evaluate conditions
        :return: True if the condition is within range, False otherwise
        """
        pass

    def cond_find(self) -> None:
        """
        Template to find conditions
        :return: None
        """
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, 'XPATH HERE')))
        except NoSuchElementException:
            pass
