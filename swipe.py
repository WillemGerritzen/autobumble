from selenium import webdriver


class Swipe:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def swipe_right(self):
        try:
            right = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
            right.click()

        except Exception as e:
            self.driver.quit()
            raise e

    def swipe_left(self):
        pass
