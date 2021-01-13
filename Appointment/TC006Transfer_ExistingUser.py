from TestActionLibrary import A
# Appointment Process
TEU = A()
TEU.openBrowser()
TEU.randomGenerator()
TEU.login("admin", "pass123")
TEU.counteractivation()
TEU.quickAppointment()
#--------------------------------#
#Transfer process
TEU.Transfer()
TEU.logout()
TEU.closeBrowser()