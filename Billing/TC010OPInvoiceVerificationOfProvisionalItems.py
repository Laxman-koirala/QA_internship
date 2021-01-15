from TestActionLibrary import A

IVOP = A()
IVOP.openBrowser()
IVOP.randomGenerator()
IVOP.login("admin", "pass123")
IVOP.counteractivation()
IVOP.quickAppointment()
IVOP.OPnormalbillingtransaction("X-Ray Chest PA view","Urine Calcium",'x')
IVOP.provisionalItemBilling()
IVOP.VerifivationOfNormalBilling()
IVOP.logout()
IVOP.closeBrowser()