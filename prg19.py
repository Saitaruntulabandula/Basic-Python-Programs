import os.path, time
print("Creation time : " , time.ctime(os.path.getmtime("prg19.py")))
print("Modification Time : ", time.ctime(os.path.getctime('prg19.py')))