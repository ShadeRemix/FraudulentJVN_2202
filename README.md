# 2202_Assignment1

![image](https://user-images.githubusercontent.com/94280261/196103466-61a045df-fdfc-478f-86da-a6a4f2497bcd.png)


# User Manual

Installation:
This program uses the filedate module, make sure it is installed before running the program.

pip install filedate

# Running the tool

sudo python3 FraudulentJVN.py

note: Some permission errors might occur when not running using sudo.

![image](https://user-images.githubusercontent.com/94280261/199173220-6bf3f4d1-a323-4d1d-bc73-66c0484c6fbc.png)


# File Metadata

Upon running the program, it will prompt the user to enter 1 or 2.

Option 1 targets the current directory the program is in and this will change all the file metadata and it's subdirecotry files.

Option 2 makes the user specify the target directory for the program to target and change all metadata of files and subdirecotry files.

note: Specifying option 2 and selecting the "/" root directory changes all files in the system, this may also cause some permission errors to occur as not all files in Linux can be modified even when ran as root!

### Before
![image](https://user-images.githubusercontent.com/94280261/199173378-7a2338bf-4701-4150-aec6-b6838b922bc7.png)

### After
![image](https://user-images.githubusercontent.com/94280261/199173391-fd024cdc-bc15-4e7e-9553-c97cdb12ae20.png)

## How it works

The program uses the filedate module in python to change the Access and modify time of files.
For the created and birth time, our program copies the file, shreds the original file (to prevent restoration) then moves the copied file to the original one, effectively replacing the original file.

![image](https://user-images.githubusercontent.com/94280261/199173489-5c28073f-744d-488e-bad1-1c9f295be482.png)

# Logs

After the file metadata has been changed, the program will scramble the timestamps in /var/log/

### syslog before
![image](https://user-images.githubusercontent.com/94280261/199173604-816d0b42-bf0e-4e49-80d3-9c64172c9297.png)

### syslog after
![image](https://user-images.githubusercontent.com/94280261/199173622-88148c66-b6c3-4b4b-b53b-048cb6e0e861.png)
