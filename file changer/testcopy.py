import filedate
import os



os.popen('cp test.txt test.txt1')
os.popen('rm test.txt')
os.popen('mv test.txt1 test.txt')

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
