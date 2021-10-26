import random
import json

from swipe import Swipe
from auth import Auth
from time import sleep
from driver import Driver
from conditions import Conditions


d = Driver()
a = Auth()
s = Swipe()
c = Conditions()

if __name__ == '__main__':
    try:
        with open('conditions.json', 'r') as f:
            condi = json.load(f)

        d.driver.get('https://bumble.com')
        a.signin()
        sleep(2)
        while not s.check_end():
            left = False
            for cond in condi.keys():
                if cond == 'page':
                    continue
                cond_check = c.cond_find(cond)
                if condi[cond]['value'] != cond_check or cond_check is None:
                    print(condi[cond]['value'], cond_check)
                    sleep(random.randint(2, 5))
                    s.left()
                    left = True
                    print('Swiped left')
                    break
                else:
                    continue
            if not left:
                sleep(random.randint(2, 5))
                s.right()
                print('Swiped right')
                sleep(1)
                s.check_match()
                sleep(random.randint(2, 5))
        d.driver.quit()
        print('Hit the end of the line')
    except Exception as e:
        d.driver.quit()
        raise e
