import re

from browser import Browser
from utils import _check_os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup


class Driver:
    def __init__(self, headless=True, debug=False):
        platform = _check_os()
        browser = Browser(platform)
        self.driver = browser.set_driver(headless=headless)
        self.debug = debug

        print('\n========================')
        print('Booting driver')
        print('========================\n')

        self.wait = WebDriverWait(self.driver, 5)

        print('\tSuccess!\n')

    def right(self) -> None:
        """
        Swipe right
        :return: None
        """
        if 'tinder' in self.driver.current_url:
            right = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button')
        else:
            right = self.wait.until(ec.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')))

        right.click()
        print('\tSwiped right\n')

    def left(self) -> None:
        """
        Swipe left
        :return: None
        """
        if 'tinder' in self.driver.current_url:
            left = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[2]/button')
        else:
            left = self.wait.until(ec.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')))

        left.click()
        print('\tSwiped left\n')

    def check_match(self) -> bool:
        """
        Checks if match occured.
        :return: None
        """

        # Looks for a button appearing only in case of match
        try:
            if 'tinder' in self.driver.current_url:
                pass

            else:
                cont = self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div')
                cont.click()
                return True

        # If it fails to find it, passes
        except NoSuchElementException:
            return False

    def check_end(self) -> bool:
        """
        Checks if the queue is empty
        :return: True if the queue is empty, False if the queue is not empty
        """

        # Looks for a button that only appears in case of an empty queue
        try:
            if 'tinder' in self.driver.current_url:
                self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div/div[1]/div[2]/div[1]/span[1]/div/div/span/div/h3')

            else:
                self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div/section/div/div[2]/div')

        # Returns False if it fails to find it
        except NoSuchElementException:
            return False

        return True

    def signin(self) -> None:
        """
        Finds and clicks the signin button
        :return: None
        """

        print('\tSigning in...\n')

        sign_in = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')))

        sign_in.click()

        print('\tSuccess!\n')

    def scrape_about(self) -> list:

        # Scroll down a page
        inter = self.wait.until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[2]/div[2]")))
        inter.click()

        # Retrieve all listed pills
        try:
            about_html = self.driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[2]/article/div/section/div/ul').get_attribute(
                'innerHTML')

            soup = BeautifulSoup(about_html, 'html.parser')

            abouts = re.findall('[0-9a-zA-Z][^A-Z]*', soup.get_text())

            return abouts

        except NoSuchElementException or TimeoutException:
            return []

    def cond_eval(self, conditions: dict) -> bool:
        """
        Template to evaluate conditions
        :return: True if the c is within range, False otherwise
        """

        abouts = self.scrape_about()

        pills = conditions['pills']

        for element in pills.values():
            if element in abouts:
                return True
            else:
                return False

    def open_info(self) -> None:
        self.driver.find_element_by_xpath('/html/body').send_keys(Keys.UP)

    def find_distance(self) -> int:

        html = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]').get_attribute(
            'innerHTML')

        soup = BeautifulSoup(html, 'html.parser')

        info = soup.get_text().split(' ')

        try:
            pot_dist = info[-3]

        except IndexError:
            return 9999

        try:
            distance = int(pot_dist[-2:])
            return distance

        except ValueError:
            try:
                distance = int(pot_dist[-1])
                return distance

            except ValueError:
                return 9999

    def t_check_verified(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]')

        except NoSuchElementException as e:
            return False

        return True

    def t_eval_cond(self, conditions: dict) -> bool:

        if 'max_distance' in conditions.keys():

            distance = self.find_distance()

            if distance > conditions['max_distance']:
                return False

        if 'verified' in conditions.keys():

            verified = self.t_check_verified()

            if not verified:
                return False

        return True

    def t_check_interest(self):
        pass

    def t_check_likes(self):
        pass
