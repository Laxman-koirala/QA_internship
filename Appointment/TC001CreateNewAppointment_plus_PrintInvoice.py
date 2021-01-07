from TestActionLibrary import A

CNA = A()
CNA.openBrowser()
CNA.login("billing1", "pass123")
CNA.counteractivation()
CNA.quickAppointment()
CNA.logout()
CNA.closeBrowser()
