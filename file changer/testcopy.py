import filedate
import os
import time
import subprocess



#os.popen('cp test.txt test.txt1;rm test.txt;mv test.txt1 test.txt')

subprocess.call("cp test.txt test.txt1;rm test.txt;mv test.txt1 test.txt", shell=True)

a = 'test.txt'
a_file = filedate.File(a)

a_file.set(
	#created = '1999.01.01 13:00:00',
	modified = '1999.01.01 13:00:00',
	accessed = '1999.01.01 13:00:00'
	#birth = '1999.01.01 13:00:00'
)

after = filedate.File(a)
print(after.get())
