import os
import sys
import os.path
import logging
import json
import time
import traceback
import subprocess
import datetime

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


logbasedir = os.path.join("log", "firefox-local", datetime.datetime.today().strftime("%Y-%m-%d-%H%M"))
os.makedirs(logbasedir, exist_ok=False)



def break_handler(data):
    if data == "?":
        print("")
        print("HELP")
        print("")

if os.path.isfile("play.js"):
    play = json.loads(open("play.js", "r").read())
    for play_part in play:
        if play_part[0] == None:
            if play_part[1] == "get": ###ntcommand
                driver.get(play_part[2])
            if play_part[1] == "sleep":###ntcommand
                time.sleep(float(play_part[2]))
            if play_part[1] == "halt":###ntcommand
                while True:
                    print("*** DEBUG HALT ***")
                    break_input = input("Press RETURN (no input) to continue (leave DEBUG HALT)... $ ")
                    if break_input == "":
                        break
                    else:
                        break_handler(break_input)

        else:
            lel = None # list of elements
            if play_part[0].startswith("id:"):
                target_id = play_part[0][3:]
                lel = driver.find_elements(BY.ID, target_id)
            else:
                lel = driver.find_elements(BY.XPATH, play_part[0])
            
            if play_part[1] == "type": ###tcommand
                lel[0].send_keys(play_part[2])

            if play_part[1] == "click": ###tcommand
                lel[0].click()

# driver.save_screenshot("test.png")
driver.quit()
logging.info("finished")



        