from swipe import Swipe
from util import Util
from sys import platform


util = Util(platform)
driver = util.set_driver()

swipe = Swipe(driver)

if __name__ == '__main__':
    driver.get('https://bumble.com')
    while True:
        swipe.right()
