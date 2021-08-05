import os
import subprocess
import psutil

from selenium.webdriver import ChromeOptions, Chrome


class Util:
    def __init__(self, op_sys: str):
        self.platform = op_sys

    def check_browser(self):
        chrome = ''

        if self.platform == 'linux':
            chrome = 'chromium'

        if self.platform == 'win32':
            chrome = 'chrome.exe'

        if chrome in [i.name() for i in psutil.process_iter()]:
            self._close_browser(chrome)

    def set_driver(self):

        webdriver_path = ''

        self.check_browser()

        options = ChromeOptions()

        if self.platform == 'linux':
            options.add_argument('user-data-dir=~/.config/chromium/Default')
            # options.add_argument('profile-directory=Default')
            options.binary_location = '/usr/bin/chromium'
            webdriver_path = '/usr/bin/chromedriver'

        if self.platform == 'win32':
            options.add_argument('user-data-dir=%USERPROFILE%\\AppData\\Google\\Chrome\\User Data')
            webdriver_path = 'C:\\Program Files (x86)\\chromedriver.exe'



        return Chrome(webdriver_path, options=options)

    @staticmethod
    def _close_browser(chrome: str):
        if chrome == 'chromium':
            subp = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            output, error = subp.communicate()
            target_process = chrome
            for line in output.splitlines():
                if target_process in str(line):
                    pid = int(line.split(None, 1)[0])
                    os.kill(pid, 9)

        if chrome == 'chrome.exe':
            os.system('taskkill /f /im ' + chrome)


if __name__ == '__main__':
    from sys import platform
    util = Util(platform)
    driver = util.set_driver()
    driver.get('https://google.com')

