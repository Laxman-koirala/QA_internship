from TestActionLibrary import A

VNB = A()
VNB.openBrowser()
VNB.randomGenerator()
VNB.login("admin", "pass123")
VNB.counteractivation()
VNB.quickAppointment()
VNB.OPnormalbillingtransaction("X-Ray Chest PA view","Urine Calcium")
VNB.VerifivationOfNormalBilling()
VNB.logout()
VNB.closeBrowser()