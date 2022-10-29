import datetime
import os
import random
import subprocess
from datetime import datetime, timedelta
from random import choice
import filedate


def changelog():
    """
    This function changes the timestamps in the log directory into random date and time
    :return: none
    """
    entries = os.listdir('/var/log/')
    # user_input = input("Which log files do you want?\n" + str(entries) + '\n')
    day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days31 = [*range(1, 32, 1)]  # 31 day mths
    days30 = [*range(1, 31, 1)]  # 30 day mths
    daysFeb = [*range(1, 30, 1)]  # february
    min_year = 2000
    max_year = datetime.now().year
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    linefile = ''
    randomdatetime = start + (end - start) * random.random()
    for filesinlog in entries:
        linefile = ''
        try:
            with open("/var/log/" + filesinlog, 'r') as file:
                count = 0
                # reading each line in syslog
                if filesinlog == 'alternatives.log':
                    for line in file:
                        linelist = line.split()
                        # linelist[1] is argument 1 in alternative.log for date, linelist[2] is arg 2 for time
                        # using strftime to format the datetime by removing the microseconds > ("%Y-%m-%d %H:%M:%S")
                        # need to include for randomdatetime to work, otherwise will have missing argument
                        randomdatetime = start + (end - start) * random.random()
                        linelist[1] = str(randomdatetime.strftime("%Y-%m-%d"))
                        # if random month chosen was Feb(only 29 days at most
                        linelist[2] = str(randomdatetime.strftime("%H:%M:%S"))
                        newline = " ".join(linelist)
                        line = line.replace(line, newline)
                        linefile = linefile + line + "\n"
                elif filesinlog == 'vmware-network.log':
                    for line in file:
                        linelist = line.split()
                        # need to include for randomdatetime to work, otherwise will have missing argument
                        randomdatetime = start + (end - start) * random.random()
                        linelist[0] = choice(day)
                        # linelist[1] is argument 1 in vmware-network.log for month, linelist[2] is arg for day
                        linelist[1] = choice(months)
                        # if random month chosen was Feb(only 29 days at most)
                        if linelist[1] == 'Feb':
                            linelist[2] = str(choice(daysFeb))
                        elif linelist[1] == 'Apr' or linelist[1] == 'Jun' or linelist[1] == 'Sep' or linelist[
                            1] == 'Nov':
                            linelist[2] = str(choice(days30))
                        else:
                            linelist[2] = str(choice(days31))
                        linelist[3] = str(randomdatetime.strftime("%H:%M:%S"))
                        linelist[5] = str(randomdatetime.strftime("%Y"))
                        newline = " ".join(linelist)
                        line = line.replace(line, newline)
                        linefile = linefile + line + "\n"
                else:
                    for line in file:
                        linelist = line.split()
                        # need to include for randomdatetime to work, otherwise will have missing argument
                        randomdatetime = start + (end - start) * random.random()
                        # linelist[0] is argument 0 in syslog, month, linelist[1] is arg 1, day
                        linelist[0] = choice(months)
                        # if random month chosen was Feb(only 29 days at most)
                        if linelist[0] == 'Feb':
                            linelist[1] = str(choice(daysFeb))
                        elif linelist[0] == 'Apr' or linelist[0] == 'Jun' or linelist[0] == 'Sep' or linelist[
                            0] == 'Nov':
                            linelist[1] = str(choice(days30))
                        else:
                            linelist[1] = str(choice(days31))
                        linelist[2] = str(randomdatetime.strftime("%H:%M:%S"))
                        newline = " ".join(linelist)
                        line = line.replace(line, newline)
                        linefile = linefile + line + "\n"
            with open('/var/log/' + filesinlog, 'w') as file:
                file.write(linefile)
            print("Log for %s has been edited" % filesinlog)
        except UnicodeDecodeError:
            print(filesinlog + " cannot be edited!")
        except IsADirectoryError:
            print(filesinlog + " is a directory! Going into Subdir!")
            sub_dir_file = os.listdir("/var/log/" + filesinlog)
            for file_in_subdir in sub_dir_file:
                try:
                    with open("/var/log/" + filesinlog + "/" + file_in_subdir, 'r') as sub_file:
                        for line in sub_file:
                            linelist = line.split()
                            # need to include for randomdatetime to work, otherwise will have missing argument
                            randomdatetime = start + (end - start) * random.random()
                            # linelist[0] is argument 0 in syslog, month, linelist[1] is arg 1, day
                            linelist[0] = choice(months)
                            # if random month chosen was Feb(only 29 days at most)
                            if linelist[0] == 'Feb':
                                linelist[1] = str(choice(daysFeb))
                            elif linelist[0] == 'Apr' or linelist[0] == 'Jun' or linelist[0] == 'Sep' or linelist[
                                0] == 'Nov':
                                linelist[1] = str(choice(days30))
                            else:
                                linelist[1] = str(choice(days31))
                            linelist[2] = str(randomdatetime.strftime("%H:%M:%S"))
                            newline = " ".join(linelist)
                            line = line.replace(line, newline)
                            linefile = linefile + line + "\n"
                    with open('/var/log/' + filesinlog + '/' + file_in_subdir, 'w') as file:
                        file.write(linefile)
                    print("Log for %s has been edited in" % file_in_subdir)
                except IndexError:
                    print(file_in_subdir + " in directory " + filesinlog + " cannot be edited!")
                except UnicodeDecodeError:
                    print(file_in_subdir + " in directory " + filesinlog + " cannot be edited!")
                except IsADirectoryError:
                    print(file_in_subdir + " is a directory in " + filesinlog + " too deep for any valuable logs!")
        except IndexError:
            print(filesinlog + " cannot be edited!")

    print("Log modification has been completed!")


# Generates random date
def randDate():
    """
    This functions creates a random date in between year 1902 and year 2445 and returns it
    :return: A string of a random date between 1902 and 2445
    """
    # random date from a range from 1901 to 2446. These are the minimum and maximum dates possible on to be modified,
    # according to our testing.
    start_date = datetime.date(1902, 1, 1)
    end_date = datetime.date(2445, 12, 31)
    date_difference = end_date - start_date
    days = date_difference.days
    random_days = random.randrange(days)
    random_date = start_date + datetime.timedelta(days=random_days)
    # Change the format so that the final date is yyyy.m.d format
    formatted_date = random_date.strftime('%Y.%m.%d')
    return formatted_date


def changeTimeStamps():
    """
    This function changes the timestamps of the file modified, access, created and birth dates.
    :return: none
    """
    # changes created and birth time
    # gets current directory
    cwd = os.getcwd()
    # gets list of files in current directory
    files = []
    for path in os.listdir(cwd):
        if os.path.isfile(os.path.join(cwd, path)):
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
            modified=randDate() + ' ' + str(random.randint(0, 23)) + ':' + str(random.randint(0, 59)) + ':' + str(
                random.randint(0, 59)),
            accessed=randDate() + ' ' + str(random.randint(0, 23)) + ':' + str(random.randint(0, 59)) + ':' + str(
                random.randint(0, 59))
        )
        after = filedate.File(filename)
        print(after.get())
    # Get all subdirectories

    for (root, dirnames, files) in os.walk(cwd, topdown=True):
        # loop through a list of all subdirectory names
        for directory in dirnames:
            currentfiles = []
            # get the absolute path of current subdirectory in the for loop
            path = os.path.join(root, directory)
            # change to the current subdirectory in the loop
            os.chdir(path)
            for p in os.listdir(path):
                if os.path.isfile(os.path.join(path, p)):
                    currentfiles.append(p)
            print(path)
            print(currentfiles)
            for file in currentfiles:
                filename = file
                # calling cp to copy file to file1
                # then shred file
                # then mv file1 to file
                subprocess.call(
                    "cp " + filename + " " + filename + "1;shred " + filename + ";mv " + filename + "1 " + filename,
                    shell=True)
                a_file = filedate.File(filename)
                # changes modify and access
                a_file.set(
                    modified=randDate() + ' ' + str(random.randint(0, 23)) + ':' + str(
                        random.randint(0, 59)) + ':' + str(
                        random.randint(0, 59)),
                    accessed=randDate() + ' ' + str(random.randint(0, 23)) + ':' + str(
                        random.randint(0, 59)) + ':' + str(
                        random.randint(0, 59))
                )
        after = filedate.File(filename)
        print(after.get())


if __name__ == '__main__':
    userinput = input("Input 1 for current working directory, input 2 to select another directory: ")
    if userinput == '1':
        changeTimeStamps()
        # change log contents
        changelog()
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
                    # Exit program here so that does not exist line isn't printed.
                    exit()

        print(dirname + " does not exist.")
        # change log contents
        changelog()
        # change log metadata
        logdir = '/var/log/'
        os.chdir(logdir)
        changeTimeStamps()

    else:
        print('Please input 1 or 2 only')
