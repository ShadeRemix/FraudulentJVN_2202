import filedate
import os
import time
import subprocess
import random
import datetime


# Generates random date
def randDate():
    # random date from a range from 1901 to 2446. These are the minimum and maximum dates possible on to be modifed, according to our testing.
    start_date = datetime.date(1902, 1, 1)
    end_date = datetime.date(2445, 12, 31)
    dateDifference = end_date - start_date
    Days = dateDifference.days
    randomDays = random.randrange(Days)
    random_date = start_date + datetime.timedelta(days=randomDays)
    # Change the format so that the final date is yyyy.m.d format
    formattedDate = random_date.strftime('%Y.%m.%d')
    return formattedDate


def changeTimeStamps():
	# changes created and birth time
	# gets current directory
	cwd = os.getcwd()
	# gets list of files in current directory
	files = []
	for path in os.listdir(cwd):
		if os.path.isfile(os.path.join(cwd,path)):
			files.append(path)
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
	#Get all subdirectories
    for (root,dirnames,files) in os.walk(cwd, topdown=True):
        #loop through a list of all subdirectory names
		for directory in dirnames:
			currentfiles = []
            #get the absolute path of current subdirectory in the for loop
			path = os.path.join(root,directory)
            #change to the current subdirectory in the loop
			os.chdir(path)
			for p in os.listdir(path):
				if os.path.isfile(os.path.join(path,p)):
					currentfiles.append(p)
			print(path)
			print(currentfiles)
			for file in currentfiles:
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
	


if __name__ == '__main__':
    userinput = input("Input 1 for current working directory, input 2 to select another directory: ")
    if userinput == '1':
        changeTimeStamps()
        # change log metadata
        logdir = '/var/log/'
        os.chdir(logdir)
        changeTimeStamps()
    elif userinput == '2':
        dirname = input("Case Sensitive Directory Name (example: test2): ")
        # Use os walk to list all folders
        for (root, dirnames, files) in os.walk('/', topdown=True):
            for directory in dirnames:
                # find a directory that matches that name then gets the directory path
                if directory == dirname:
                    path = os.path.join(root, directory)
                    # change the directory to targeted directory before changing time stamps
                    os.chdir(path)
                    changeTimeStamps()
                    # Exit program here so that does not exist line isnt printed.
                    exit()

        print(dirname + " does not exist.")
        # change log metadata
        logdir = '/var/log/'
        os.chdir(logdir)
        changeTimeStamps()

    else:
        print('Please input 1 or 2 only')
