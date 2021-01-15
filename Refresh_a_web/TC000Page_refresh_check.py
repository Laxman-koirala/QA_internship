from TestActionLibrary import A
PR = A()

PR.openBrowser()
PR.login("billing1", "pass123")
PR.pageRefreshment()

PR.logout()
PR.closeBrowser()

#Bug number 1