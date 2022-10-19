import filedate
import os
import time
import subprocess
import random
import datetime

#Generates random date
def randDate(): 
	#random date from a range from 1901 to 2446. These are the minimum and maximum dates possible on to be modifed, according to our testing.
	start_date = datetime.date(1902,1,1)
	end_date = datetime.date(2445,12,31)
	dateDifference = end_date - start_date
	Days = dateDifference.days
	randomDays = random.randrange(Days)
	random_date = start_date + datetime.timedelta(days=randomDays)
	#Change the format so that the final date is yyyy.m.d format
	formattedDate = random_date.strftime('%Y.%m.%d')
	return formattedDate

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
        modified = randDate() + ' ' + str(random.randint(0,23)) + ':' + str(random.randint(0,59)) + ':' + str(random.randint(0,59)),
	    accessed = randDate() + ' ' + str(random.randint(0,23)) + ':' + str(random.randint(0,59)) + ':' + str(random.randint(0,59))
    )
    after = filedate.File(filename)
    print(after.get())
