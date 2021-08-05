from driver import Driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Auth(Driver):
    def signin(self) -> None:
        """
        Finds and clicks the signin button
        :return: None
        """
        wait = WebDriverWait(self.driver, 5)

        sign_in = wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')))

        sign_in.click()


if __name__ == '__main__':
    Driver.driver.get('https://bumble.com')
    auth = Auth()
    auth.signin()
