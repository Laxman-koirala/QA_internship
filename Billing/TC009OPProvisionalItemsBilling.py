from TestActionLibrary import A

PIB = A()
PIB.openBrowser()
PIB.randomGenerator()
PIB.login("admin", "pass123")
PIB.counteractivation()
PIB.quickAppointment()
PIB.OPnormalbillingtransaction("X-Ray Chest PA view","Urine Calcium",'x')
PIB.provisionalItemBilling()
PIB.logout()
PIB.closeBrowser()