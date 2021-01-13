from TestActionLibrary import A

RP = A()

RP.openBrowser()
RP.login("Admin", "pass123")
RP.randomGenerator()
RP.counteractivation()
RP.patientRegistration()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC007 PatientRegistration")
