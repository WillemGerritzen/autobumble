import random
import json

from time import sleep
from driver import Driver

B_LEFT = 0
B_RIGHT = 0
B_MATCH = 0

T_LEFT = 0
T_RIGHT = 0
T_MATCH = 0

if __name__ == '__main__':

    d = Driver(headless=False)

    try:

        # Start with Bumble

        print('\n========================')
        print('Opening Bumble')
        print('========================\n')

        d.driver.get('https://bumble.com')

        d.signin()

        with open('b_conditions.json', 'r') as f:
            conditions = json.load(f)

        sleep(2)

        print('\tStarting swipes:\n')

        while not d.check_end():
            if not d.cond_eval(conditions):
                sleep(random.randint(2, 5))
                d.left()
                sleep(random.randint(2, 5))
            else:
                sleep(random.randint(2, 5))
                d.right()
                B_RIGHT += 1
                sleep(1)
                if d.check_match():
                    B_MATCH += 1
                sleep(random.randint(2, 5))

        d.driver.quit()

        print(f'\tHit the end of the line:\n\n\t\tLeft swipes: {B_LEFT}\n\n\t\tRight swipes: {B_RIGHT}\n\n\t\tMatches: {B_MATCH}')

    except Exception as e:
        # d.driver.quit()
        raise e


