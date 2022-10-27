from random import choice
import random
from datetime import datetime, timedelta
import os

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
                    elif linelist[1] == 'Apr' or linelist[1] == 'Jun' or linelist[1] == 'Sep' or linelist[1] == 'Nov':
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
                    elif linelist[0] == 'Apr' or linelist[0] == 'Jun' or linelist[0] == 'Sep' or linelist[0] == 'Nov':
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
                        elif linelist[0] == 'Apr' or linelist[0] == 'Jun' or linelist[0] == 'Sep' or linelist[0] == 'Nov':
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