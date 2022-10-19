import filedate
import os
import time
import subprocess

# changes created and birth time
# gets current directory
cwd = os.getcwd()
# gets list of files in current directory
files = os.listdir(cwd)
print(cwd)
print(files)
# Changes time of all files in list
for file in files:
    filename = file
    # calling cp to copy file to file1
    # then shred file
    # then mv file1 to file
    subprocess.call("cp " + filename + " " + filename + "1;shred " + filename + ";mv " + filename + "1 " + filename,
                    shell=True)
    a_file = filedate.File(filename)
    # changes modify and access
    a_file.set(
        modified='1999.01.01 13:00:00',
        accessed='1999.01.01 13:00:00'
    )
    after = filedate.File(filename)
    print(after.get())
