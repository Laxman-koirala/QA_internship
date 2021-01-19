from SystemCheckAndExcell import XLshortcut
import pathlib
import os

def files(file,file1,rows,*args):
    if not args:
        XLshortcut.copyoriginal(file,file1)
    for r in range(2, rows + 1):
        Testcase = str(XLshortcut.readData(file1, 'Sheet1', r, 1))
        Status = XLshortcut.readData(file1, 'Sheet1', r, 2)
        RunNoR = (XLshortcut.readData(file1, 'Sheet1', r, 3))
        if Status != 'Passed':
            base_dir = str(pathlib.PureWindowsPath(r'C:\Testing_internshi\QA_internship'))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)

            try:
                exec(open(Pythonfilepath).read())
                XLshortcut.writeData(file1, 'Sheet1', r, 2, 'Passed')
            except:
                XLshortcut.writeData(file1, 'Sheet1', r, 2, 'Failed')
                XLshortcut.writeData(file1, 'Sheet1', r, 3, RunNoR + 1)




file= "SystemTestCasesCheckup.xlsx"  #path
file1 = "DuplicateSystemCheckup2.xlsx"
rows = XLshortcut.getTotalrows(file, 'Sheet1')
files(file,file1,rows)
files(file,file1,rows,2)

