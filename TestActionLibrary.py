from selenium import webdriver
import time
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from random import randint
from selenium.webdriver.support.wait import WebDriverWait


class A:
   global Age
   global First_name
   global LastName
   global ContactNo



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
      #self.danpheEMR.find_element_by_link_text("Appointment").click()
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

   def counteractivation(self):
      print(">>Activate Billing Counter: START")
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("my-app > div > ul > li:nth-child(6) > a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-md-2:nth-child(1) img").click()
      time.sleep(2)
      print("Activate Billing Counter: END<<")


   def quickAppointment(self):
      print(">>Create New Appointment: START")
      self.danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("New Patient").click()
      time.sleep(1)

      # cheking without additional bill

      self.danpheEMR.find_element_by_css_selector("div>div>div>div>div:nth-child(1)>div>div>div>div>label>span").click()
      subtotal = int(self.danpheEMR.find_element_by_css_selector("div:nth-child(1) > div > span > b").text)
      if not subtotal:
         possible_doctor = ['Dr. ELVIS KSAWIER', 'Dr. DAANISH C LASZLO', 'Dr. JIMMIE Obet', 'Dr. ADYAAN Snopia',
                            'Dr. EMRAN A MUJEEB']
         Doctor = possible_doctor[randint(0, len(possible_doctor) - 1)]
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").clear()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Doctor)
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         time.sleep(2)


     ## cheking with additional bill

      #random first name
      First_name =names.get_first_name()
      self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys(First_name)
      self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
      time.sleep(2)

      #random last_name
      possible_lastName = ['Lamsal','Koirala','Bhatta','Pandey','Thapa']
      LastName = possible_lastName[randint(0,len(possible_lastName)-1)]
      self.danpheEMR.find_element_by_css_selector(".col-md-3:nth-child(4) > .form-control").send_keys(LastName)
      time.sleep(1)

      #random age,contactno
      Age = randint(4, 109)
      global ContactNo
      ContactNo = randint(9841111111, 9849999999)
      self.danpheEMR.find_element_by_css_selector(".row > .form-control").send_keys(Age)
      self.danpheEMR.find_element_by_css_selector(".rad-holder > .mt-radio:nth-child(1) > span").click()
      self.danpheEMR.find_element_by_css_selector(".col-md-3 > .ng-invalid").click()
      self.danpheEMR.find_element_by_css_selector(".form-group > .pr-0:nth-child(2) > .ng-untouched").send_keys(
         ContactNo)
      time.sleep(2)

      ## checking with Membership discount
      # Random listed Membership
      possible_membership = self.danpheEMR.find_element_by_css_selector("membership-select > div > div > div > div > select")
      drp = Select(possible_membership)
      index_number = randint(1, len(drp.options)-1)
      drp.select_by_index(index_number)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[2]/div[2]/input").send_keys("Auto discount check")
      time.sleep(2)

      #random listed reason
      possible_reason = self.danpheEMR.find_element_by_css_selector("div:nth-child(3) > div > select")
      drp = Select(possible_reason)
      index_number = randint(0,len(drp.options)-1)
      drp.select_by_index(index_number)

      #random gender, select radio botton
      #possible_gender = ["#genderMale","#genderFemale","#genderOther"]
      #self.danpheEMR.find_element_by_css_selector(possible_gender[randint(0,len(possible_gender)-1)]).click()
      #status = self.danpheEMR.find_element_by_css_selector(possible_gender[randint(0,len(possible_gender)-1)]).is_selected()
      #print(status)

     ## payment mode checkup
      #random_possible listed payment type
      possible_reason = self.danpheEMR.find_element_by_css_selector("#pay_mode")
      drp = Select(possible_reason)
      index_number = randint(0, len(drp.options)-1)
      drp.select_by_index(index_number)
      paymentMode =str(self.danpheEMR.find_element_by_css_selector("#pay_mode").text)



      if paymentMode == 'Cheque' or paymentMode == 'Smart Card':
         self.danpheEMR.find_element_by_css_selector(' tr:nth-child(2) > td:nth-child(2) > textarea').send_keys("Cheque/smartcard of NMB Bank")

      if paymentMode =='CREDIT':
         self.danpheEMR.find_element_by_css_selector(' tr:nth-child(2) > td:nth-child(2) > textarea').send_keys("Credit under request of chairmain")

         ##Random credit organization
         possible_organization = self.danpheEMR.find_element_by_css_selector("#pay_mode")
         drp = Select(possible_organization)
         index_number = randint(1, len(drp.options)-1)
         drp.select_by_index(index_number)


      self.danpheEMR.find_element_by_css_selector(".btn-success").click()
      time.sleep(5)

      print("Create New Appointment: END<<")




   def verificationOfAppointmentInvoice(self):
      global ContactNo
      print(">>Verify of Appointment Invoice Details: START")
      time.sleep(5)

      #retriving text
      Invoice_contactno = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[5]/div/p").text
      InvoiceNoTemp = self.danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
      HospitalNo = self.danpheEMR.find_element_by_xpath(
         "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text

      Invoice_contactno = Invoice_contactno.partition("No: ")[2]
      InvoiceNo = InvoiceNoTemp.partition("BL")[2]
      recent_contact = []
      recent_contact.append(ContactNo)

      try:
         assert int(recent_contact[-1]) == int(Invoice_contactno)
      except:
         print("Telephone number isn't coordinate/match || Additional bug")

      finally:
         print("InvoiceNoTemp: ", InvoiceNoTemp)
         print("InvoiceNo: ", InvoiceNo)
         print("HospitalNo: ", HospitalNo)
         print(" Verify OPD Invoice Details: END<<", "HospitalNo", HospitalNo, "InvoiceNo", InvoiceNo)


      print("Verification of Appointment Invoice Details: END<<")











