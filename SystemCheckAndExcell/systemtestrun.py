from SystemCheckAndExcell import XLshortcut
import pathlib
import os

def files(file,file1,rows,*args):
    if args:
        file = file1
    for r in range(2, rows + 1):
        Testcase = str(XLshortcut.readData(file, 'Sheet1', r, 1))
        Status = XLshortcut.readData(file, 'Sheet1', r, 2)
        RunNoR = (XLshortcut.readData(file, 'Sheet1', r, 3))
        if Status != 'Passed':
            base_dir = str(pathlib.PureWindowsPath(r'C:\Testing_internship\QA_internship'))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)

            try:
                exec(open(Pythonfilepath).read())
                XLshortcut.writeData(file, 'Sheet1', r, 2, 'Passed', file1)
            except:
                XLshortcut.writeData(file, 'Sheet1', r, 2, 'Failed', file1)
                XLshortcut.writeData(file, 'Sheet1', r, 3, RunNoR + 1, file1)
                pass

file= "SystemTestCasesCheckup.xlsx"  #path
file1 = "DuplicateSystemCheckup1.xlsx"
rows = XLshortcut.getTotalrows(file, 'Sheet1')
files(file,file1,rows)
files(file,file1,rows,2) # args can be anything

