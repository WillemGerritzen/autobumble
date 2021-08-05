from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class Swipe (Driver):

    def right(self) -> None:
        """
        Swipe right
        :return: None
        """

        wait = WebDriverWait(self.driver, 5)

        right = wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')))
        right.click()

    def left(self) -> None:
        """
        Swipe left
        :return: None
        """

        wait = WebDriverWait(self.driver, 5)

        left = wait.until(ec.presence_of_element_located(
            (By.XPATH,
             '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')))
        left.click()

    def check_match(self) -> None:
        """
        Checks if match occured.
        :return: None
        :todo: Add inherent waiting
        """

        # Looks for a button appearing only in case of match
        try:
            cont = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div')
            cont.click()

        # If it fails to find it, passes
        except NoSuchElementException:
            pass

    def check_end(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False if the queue is not empty
        """

        # Looks for a button that only appears in case of an empty queue
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div/section/div/div[2]/div')

        # Returns False if it fails to find it
        except NoSuchElementException:
            return False

        return True
