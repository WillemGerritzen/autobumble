import json
import random

from driver import Driver
from time import sleep


class Tinder:
    LEFT = 0
    RIGHT = 0
    MATCH = 0

    def autoswipe(self, headless=False):

        d = Driver(headless=headless)

        try:
            print('\n========================')
            print('Opening Tinder')
            print('========================\n')

            d.driver.get('https://tinder.com')

            with open('t_conditions.json', 'r') as f:
                conditions = json.load(f)

            sleep(5)

            d.t_check_likes()

            printout = '\tSwiping'
            count = 1

            print(printout, end='')

            while not d.check_end():
                d.open_info()
                sleep(2)
                if not d.t_eval_cond(conditions):
                    sleep(random.randint(2, 5))
                    d.left()
                    self.LEFT += 1
                    sleep(random.randint(2, 5))
                else:
                    sleep(random.randint(2, 5))
                    d.right()
                    self.RIGHT += 1
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
            # d.driver.quit()
            raise e
