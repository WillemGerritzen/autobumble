import random
import json

from time import sleep
from driver import Driver


class Bumble:
    LEFT = 0
    RIGHT = 0
    MATCH = 0

    def autoswipe(self, headless=False):

        d = Driver(headless=headless)

        try:

            print('\n========================')
            print('Opening Bumble')
            print('========================\n')

            d.driver.get('https://bumble.com')

            d.signin()

            with open('b_conditions.json', 'r') as f:
                conditions = json.load(f)

            sleep(2)

            printout = '\tSwiping'
            count = 1

            print(printout, end='')

            while not d.check_end():
                if not d.cond_eval(conditions):
                    sleep(random.randint(2, 5))
                    d.left()
                    sleep(random.randint(2, 5))
                else:
                    sleep(random.randint(2, 5))
                    d.right()
                    self.RIGHT += 1
                    sleep(1)
                    if d.check_match():
                        self.MATCH += 1
                    sleep(random.randint(2, 5))

                if count >= 4:
                    count = 0
                print('\r' + printout + '.' * count, end='')
                count += 1

            d.driver.quit()

            print('\r\tSwiping... Done!\n', end='')

        except Exception as e:
            d.driver.quit()
            raise e
