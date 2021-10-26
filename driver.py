from browser import Browser
from utils import _check_os


class Driver:
    platform = _check_os()
    browser = Browser(platform)
    driver = browser.set_driver(headless=False)
