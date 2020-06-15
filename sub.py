import json
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

class subClass():
    def display(self, driver):
        print("this is subClass.display()")

    def load_config(self, fpath):
        json_config = {}
        with open(fpath, "r", encoding="utf-8") as f:
            json_data = json.load(f) #[self.env]
            json_config = json_data[self.env]
            json_config['sidemenu'] = json_data['sidemenu']
            json_config['past_data'] = json_data['past_data']
        return json_config

    def select_browser(self, browser):
        if (browser == 'chrome'):
            # ----- launch visible
            #        self.driver = webdriver.Remote(
            #           command_executor= self.selenium_server,
            #            desired_capabilities=DesiredCapabilities.CHROME)
            # ----- launch background start
            opts = Options()
            # opts.binary_location = self.browser_path
            # opts.add_argument('--headless')
            opts.add_argument('--disable-gpu')
            opts.add_argument('--no-sandbox')
            return webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=opts)
            # ----end
        else:
            profile = webdriver.FirefoxProfile()
            # profile.set_preference("browser.cache.disk.enable", False)
            # profile.set_preference("browser.cache.memory.enable", False)
            # profile.set_preference("browser.cache.offline.enable", False)
            # profile.set_preference("network.http.use-cache", False)
            profile.set_preference("browser.privatebrowsing.autostart", True)
            driver = webdriver.Firefox(executable_path=os.path.abspath("geckodriver"), firefox_profile=profile)
            self.addCleanup(driver.quit)
            return driver

    def login(self, user):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'mail')))
        self.driver.find_element_by_name('mail').clear()
        element.send_keys(user[0])
        self.driver.find_element_by_name('password').send_keys(user[1])
        self.driver.find_element_by_id('login-button').click()

    def web_driver_wait_selector(self, selector):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def web_driver_wait_name(self, tag_name):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, tag_name)))

    def web_driver_wait_link_text(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text)))

    def web_driver_wait_id(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, text)))

    # def drop_files(self, element, files, offsetX=0, offsetY=0):
    #     JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"
    #     for(f in files):
    #         if not os.path.isfile(f):
    #             continue
    #         elm_input = self.driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    #     pass