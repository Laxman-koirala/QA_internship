from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import winsound

from selenium.webdriver.support.wait import WebDriverWait


class A:

   def openBrowser(self):
      options = Options()
      options.add_argument('--allow-running-insecure-content')
      options.add_argument('--ignore-certificate-errors')
      print(">>Open Browser: START")
      self.danpheEMR = webdriver.Chrome(r"C:\Users\laxma\Downloads\chromedriver\chromedriver.exe",options=options)
      self.danpheEMR.set_window_position(-2000, 0)
      self.danpheEMR.maximize_window()
      self.danpheEMR.get("https://demo.danphehealth.com/")
      time.sleep(3)
      print("Open Browser: END<<")

   def closeBrowser(self):
      print(">>Close Browser: START")
      self.danpheEMR.close()
      print("Close Browser: END<<")

   def login(self, userid, pwd):
      print(">>LogIn: START")
      self.danpheEMR.find_element_by_id("username_id").send_keys(userid)
      self.danpheEMR.find_element_by_id("password").send_keys(pwd)
      self.danpheEMR.find_element_by_id("login").submit()
      time.sleep(3)
      print("LogIn: END<<")

   def pageRefreshment(self):
      print(">>Page: START")
      element = WebDriverWait(self.danpheEMR, 5).until(EC.element_to_be_clickable(
         (By.LINK_TEXT, "Appointment")))
      element.click()
      self.danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(2)
      self.danpheEMR.refresh()
      time.sleep(2)

      print("Page: REFRESHED<<")

   def logout(self):
      print(">>LogOut: START")
      time.sleep(3)
      self.danpheEMR.find_element_by_css_selector(".dropdown-toggle:nth-of-type(1)>.username").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Log Out").click()
      time.sleep(3)
      print("LogOut: END<<")

