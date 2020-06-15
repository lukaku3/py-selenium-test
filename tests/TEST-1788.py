from dotenv import load_dotenv
from collections import OrderedDict
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from venv.sub import subClass

class MyTestCase(unittest.TestCase):
    selenium_server = 'http://localhost:4444/wd/hub'
    browser_path = '/usr/bin/google-chrome'
    env = False
    scaru_config = [];

    def setUp(self):
        load_dotenv()
        self.driver = subClass.select_browser(self, os.environ['BROWSER'])
        # self.driver.set_window_size(self.x, self.y)
        self.driver.implicitly_wait(10)
        self.env = os.environ["SCARU_ENV"]
        self.scaru_config = subClass.load_config(self, os.environ['JSON_PATH'])

    def test_something(self):
        print(self.scaru_config['url'])
        self.driver.get(self.scaru_config['url'])
        time.sleep(1)
        # subClass.login(self, self.scaru_config['users'][0])
        # self.assertEqual(True, True)
        # element = subClass.web_driver_wait_selector(self, 'input[type="search"]')
        # element.send_keys(self.scaru_config['client'][1]['name'])
        # self.driver.find_element_by_name('submitBtn').click()
        # self.driver.find_element_by_link_text(self.scaru_config['client'][1]['name']).click()
        # element = subClass.web_driver_wait_link_text(self, self.scaru_config['sidemenu'][0])
        # element.click()
        # print( self.scaru_config["past_data"]["open_modal"])
        # element = subClass.web_driver_wait_id(self, self.scaru_config["past_data"]["open_modal"])
        # element.click()
        # Select(self.driver.find_element_by_css_selector('select[name="param_type"]')).select_by_value('12')
        # element = self.driver.find_element_by_id('drag-drop-area')
        # # element.send_keys(os.environ['CSVDIR_PATH'], "{}{}".format(os.environ['CSVDIR_PATH'],self.scaru_config["past_data"]["csv12"][0]))
        # print("{}{}".format(os.environ['SCARU_ENV'],self.scaru_config["past_data"]["csv12"][0]))
        # # fpath = 'C:\\Users\\0987\\Downloads\\過去データ（ミロク）\\ミロク_勘定科目一覧.csv'.encode('cp932')
        # Imagepath = os.path.abspath('.\\sample.csv')
        # # element.send_keys(Imagepath)
        # self.driver.find_element_by_css_selector('div.up-btn label.file.over').click()
        # print(Imagepath)
        # send_keys(Imagepath)

        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
