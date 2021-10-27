import random
import json

from time import sleep
from driver import Driver


d = Driver(headless=True)

LEFT = 0
RIGHT = 0
MATCH = 0

if __name__ == '__main__':
    try:
        with open('conditions.json', 'r') as f:
            conditions = json.load(f)

        d.driver.get('https://bumble.com')
        d.signin()
        sleep(2)
        while not d.check_end():
            if not d.cond_eval(conditions):
                sleep(random.randint(2, 5))
                d.left()
                LEFT += 1
                print('Swiped left')
                sleep(random.randint(2, 5))
            else:
                sleep(random.randint(2, 5))
                d.right()
                RIGHT += 1
                print('Swiped right')
                sleep(1)
                if d.check_match():
                    MATCH += 1
                sleep(random.randint(2, 5))
        d.driver.quit()
        print(f'Hit the end of the line\n\nLeft swipes: {LEFT}\n\nRight swipes: {RIGHT}\n\nMatches: {MATCH}')
    except Exception as e:
        d.driver.quit()
        raise e
    # TODO: Move waiting to driver functions
