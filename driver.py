from browser import Browser
from sys import platform, exit


def _check_os():
    if platform != 'linux' and platform != 'win32':
        print('This bot works only on Windows and Linux machines')
        exit(0)


class Driver:
    _check_os()
    browser = Browser(platform)
    driver = browser.set_driver()
