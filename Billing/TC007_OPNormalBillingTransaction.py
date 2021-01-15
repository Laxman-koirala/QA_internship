from TestActionLibrary import A

NBT = A()
NBT.openBrowser()
NBT.randomGenerator()
NBT.login("admin", "pass123")
NBT.counteractivation()
NBT.quickAppointment()
NBT.OPnormalbillingtransaction("X-Ray Chest PA view","Urine Calcium")
NBT.logout()
NBT.closeBrowser()
