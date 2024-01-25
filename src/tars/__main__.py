import os
import sys
import os.path
import logging
import json
import time
import traceback
import subprocess

from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.edge.options import Options as EDOptions
from selenium import webdriver

from selenium.webdriver.common.keys import Keys as KEYS
from selenium.webdriver.common.by import By as BY

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support.ui import Select as SEL
from selenium.webdriver.support import expected_conditions as EC

import selenium


FORMAT = '%(asctime)s+00:00 %(levelname)10s: %(message)-80s    (%(filename)s,%(funcName)s:%(lineno)s)'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.Formatter.converter = time.gmtime



opts = selenium.webdriver.FirefoxOptions()

#opts = EDOptions()
#opts = CHOptions()

#driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=opts)

driver = webdriver.Firefox(options=opts)

driver.get("https://www.google.de")
driver.save_screenshot("test.png")
driver.quit()
logging.info("finished")
