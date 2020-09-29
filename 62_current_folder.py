import os

list = []
tuple = ()

for entry in os.scandir():
    if entry.is_file():
        tuple =tuple + (entry.name,"File",)

        list +=[(tuple)]

        tuple = ()
    else:
        tuple =tuple + (str(entry),"Folder",)

        list +=[(tuple)]

        tuple = ()


print(list)