import filedate

a = 'testfile.txt'
a_file = filedate.File(a)

a_file.set(
    created = "2022.01.01 13:00:00",
    modified = "2022.01.01 14:00:00",
    accessed = "2022.01.01 15:00:00"
)

after = filedate.File(a)
print(after.get())