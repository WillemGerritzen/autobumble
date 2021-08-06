import random

from swipe import Swipe
from auth import Auth
from time import sleep
from driver import Driver
from conditions import Conditions

auth = Auth()
swipe = Swipe()

if __name__ == '__main__':
    try:
        Driver.driver.get('https://bumble.com')
        auth.signin()
        sleep(2)
        while not swipe.check_end():
            swipe.right()
            sleep(1)
            swipe.check_match()
            sleep(random.randint(2, 5))
        Driver.driver.quit()
        print('Hit the end of the line')
    except Exception as e:
        Driver.driver.quit()
        raise e
