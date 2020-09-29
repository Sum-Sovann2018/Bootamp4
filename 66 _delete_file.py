import os

def delete_file(name):

    try:
        b = True
        while b:
            str = input(f"Are you sure you want to delete {name}? [Y/N]")

            if str == "Y":
                os.remove(name)
                b = False

            elif str == "N":
                return 0
                b = False

            else:
                print("Invalid Option")
                continue

    except:

        print("That file or folder does not exist.")
        return 1

delete_file("hi.py")