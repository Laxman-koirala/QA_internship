from TestActionLibrary import A

PSEH = A()

PSEH.openBrowser()
PSEH.login("Admin", "pass123")
PSEH.randomGenerator()
PSEH.counteractivation()
PSEH.patientRegistration()
PSEH.PatientSearchEditAndViewHistory()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC008 Edit of patient details and view history")
