import filedate
import os
import time
import subprocess
import random

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
        modified = str(random.randint(1902, 2445)) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1,31)) + 
	    ' ' + str(random.randint(0,23)) + ':' + str(random.randint(0,59)) + ':' + str(random.randint(0,59)),
	    accessed = str(random.randint(1902, 2445)) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1,31)) + 
	    ' ' + str(random.randint(0,23)) + ':' + str(random.randint(0,59)) + ':' + str(random.randint(0,59))
    )
    after = filedate.File(filename)
    print(after.get())
