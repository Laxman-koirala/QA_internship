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

   def randomGenerator(self):

      global First_name
      global LastName
      global Age
      global ContactNo
      global Doctor

      First_name = names.get_first_name()
      Age = randint(4, 109)
      ContactNo = randint(9841111111, 9849999999)

      #random last name
      possible_lastName = ['Lamsal', 'Koirala', 'Bhatta', 'Pandey', 'Thapa']
      LastName = possible_lastName[randint(0, len(possible_lastName) - 1)]

      # Random Doctor selector
      possible_doctor = ['Dr. ELVIS KSAWIER', 'Dr. DAANISH C LASZLO', 'Dr. JIMMIE Obet', 'Dr. ADYAAN Snopia',
                         'Dr. EMRAN A MUJEEB']

      Doctor = possible_doctor[randint(0, len(possible_doctor) - 1)]



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

         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").clear()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Doctor)
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         time.sleep(2)


     ## cheking with additional bill
      self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys(First_name)
      self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-md-3:nth-child(4) > .form-control").send_keys(LastName)
      time.sleep(1)

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
      print(">>Verify of Appointment Invoice Details: START")
      time.sleep(5)

      #retriving text
      invoice_contactno = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[5]/div/p").text
      invoiceNoTemp = self.danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
      HospitalNo = self.danpheEMR.find_element_by_xpath(
         "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text

      invoice_contactno = invoice_contactno.partition("No: ")[2]
      invoiceNo = invoiceNoTemp.partition("BL")[2]
      recent_contact = []
      recent_contact.append(ContactNo)

      try:
         assert int(recent_contact[-1]) == int(invoice_contactno)
      except:
         print("Telephone number isn't coordinate/match || Additional bug")

      finally:
         print("InvoiceNoTemp: ", invoiceNoTemp)
         print("InvoiceNo: ", invoiceNo)
         print("HospitalNo: ", HospitalNo)
         print("Verification of Appointment Invoice Details: END||OPD<<")





   def phoneBookReAppointment(self):
      self.danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(2)

      self.danpheEMR.find_element_by_css_selector("my-app>div>ul>li:nth-child(2)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".ag-row-first>div:nth-child(6)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-xs-12>div:nth-child(2)>div>div>input").clear()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-xs-12>div:nth-child(2)>div>div>input").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-xs-12>div:nth-child(2)>div>div>input").send_keys(Doctor)
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".col-xs-12>div:nth-child(2)>div>div>input").send_keys(Keys.TAB)
      time.sleep(2)

      self.danpheEMR.find_element_by_css_selector(".col-xs-12>div.btn-wrapper>input").click()

   def listedVisitReAppointment(self):
      self.danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("my-app>div>ul>li:nth-child(4)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".ag-row-first>div:nth-child(6)>a").click()
      time.sleep(2)

      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>div>div>div:nth-child(1)>div:nth-child(2)>div>div>input").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>div>div>div:nth-child(1)>div:nth-child(2)>div>div>input").send_keys(Doctor)
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>div>div>div:nth-child(1)>div:nth-child(2)>div>div>input").send_keys(Keys.TAB)
      time.sleep(2)

      self.danpheEMR.find_element_by_css_selector(".btn.blue.btn-success").click()

   def followup(self):
      self.danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("my-app>div>ul>li:nth-child(3)>a").click()
      time.sleep(2)
      findme= self.danpheEMR.find_element_by_css_selector(".ag-paging-page-summary-panel>button:nth-child(5)")
      time.sleep(1)

      ## Scroll down the page till the selected element is visual
      self.danpheEMR.execute_script("arguments[0].scrollIntoView();",findme)
      self.danpheEMR.find_element_by_xpath("//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[20]/div[12]/span/a[1]").click()

      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div.danphe-followup-visit>div:nth-child(2)>button").click()
      time.sleep(2)

   def Transfer(self):

      #back after registration
      self.danpheEMR.find_element_by_css_selector("#billing-reciept>p>span>button").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div.page-content-wrapper>div>div>my-app>div>ul>li:nth-child(3)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[12]/span/a[1]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").clear()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Doctor)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
      time.sleep(2)

      # random listed reason
      possible_reason = self.danpheEMR.find_element_by_css_selector("div:nth-child(3) > div > select")
      drp = Select(possible_reason)
      index_number = randint(0, len(drp.options) - 1)
      drp.select_by_index(index_number)


      ## payment mode checkup

      # random_possible listed payment type
      possible_reason = self.danpheEMR.find_element_by_css_selector("#pay_mode")
      drp = Select(possible_reason)
      index_number = randint(0, len(drp.options) - 1)
      drp.select_by_index(index_number)
      paymentMode = str(self.danpheEMR.find_element_by_css_selector("#pay_mode").text)

      if paymentMode == 'Cheque' or paymentMode == 'Smart Card':
         self.danpheEMR.find_element_by_css_selector(' tr:nth-child(2) > td:nth-child(2) > textarea').send_keys(
            "Cheque/smartcard of NMB Bank")

      if paymentMode == 'CREDIT':
         self.danpheEMR.find_element_by_css_selector(' tr:nth-child(2) > td:nth-child(2) > textarea').send_keys(
            "Credit under request of chairmain")

         ##Random credit organization
         possible_organization = self.danpheEMR.find_element_by_css_selector("#pay_mode")
         drp = Select(possible_organization)
         index_number = randint(1, len(drp.options) - 1)
         drp.select_by_index(index_number)

      self.danpheEMR.find_element_by_css_selector(".btn-success").click()
      time.sleep(5)

   def patientRegistration(self):

      # Emergency contact
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Register Patient").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("ng-component>div>ul>li:nth-child(5)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div.input-group>div>label:nth-child(3)>span").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(2)>div>input").send_keys(First_name)
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(3)>div>input").send_keys(LastName)
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(4)>div>input").send_keys(ContactNo)
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(5)>div>input").send_keys('Father')
      self.danpheEMR.find_element_by_css_selector("div>div.col-md-12>div:nth-child(2)>input").click()
      time.sleep(2)

      # guarantor
      self.danpheEMR.find_element_by_css_selector("ng-component>ng-component>div>ul>li:nth-child(3)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>input").send_keys('Friend')
      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>input").send_keys('Rajesh dai')
      self.danpheEMR.find_element_by_css_selector(" div>div:nth-child(1)>div:nth-child(6)>input").click()
      time.sleep(2)

      # Address
      self.danpheEMR.find_element_by_css_selector("ng-component>ng-component>div>ul>li:nth-child(2)>a").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(2)>div>input").send_keys('Bhoisi Tol')
      self.danpheEMR.find_element_by_css_selector("div.row.clearfix>div:nth-child(6)>div>input").send_keys('New Road')
      self.danpheEMR.find_element_by_css_selector("div:nth-child(1)>form>div>div>div:nth-child(2)>input").click()
      time.sleep(2)

      #Basic information
      self.danpheEMR.find_element_by_css_selector("ng-component>ng-component>div>ul>li:nth-child(1)>a").click()
      self.danpheEMR.find_element_by_id("regPatFirstName").send_keys(First_name)
      self.danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys(LastName)
      self.danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(Age)
      self.danpheEMR.find_element_by_xpath("//input[@type='tel']").send_keys(ContactNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div/label/span").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@value='Register Patient']").click()

   def PatientSearchEditAndViewHistory(self):

      #searching by phone number
      time.sleep(5)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(ContactNo)
      time.sleep(2)
      assert str(ContactNo) == self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                                    "/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      global HospitalNo
      HospitalNo = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                        "/div/div/div/div[3]/div[2]/div/div/div/div").text
      print(HospitalNo)

      # start editing
      self.danpheEMR.find_element_by_xpath("//*[@id='myGrid']/div/div[1]/div/div[3]"
                                           "/div[2]/div/div/div[1]/div[6]/a[1]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector("#regPatFirstName").clear()
      self.danpheEMR.find_element_by_css_selector("#regPatFirstName").send_keys(names.get_first_name())
      self.danpheEMR.find_element_by_xpath("//input[@value='Update Patient Information']").click()
      time.sleep(2)
      # History
      self.danpheEMR.find_element_by_xpath("//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[6]/a[2]").click()























