import os

def write_file(filename, content):

    choice = ''
    lst = os.listdir()
    print(lst)


    for i in lst:
        if i == filename:
            while choice != 'N' or choice != 'Y':
                choice = input(f"Are you sure you want to replace {filename}? [Y/N]\n")

                if choice != 'N' and choice != 'Y':
                    print("Invalid Option")

                elif choice == 'Y':
                    f = open(filename, "w")
                    f.write(content)
                    f.close()
                    return 1

                elif choice == 'N':
                    return 0

                else:
                    break


    if choice != 'N' and choice != 'Y':
        for i in lst:
            if i != filename:
                f = open(filename, "w")
                f.write(content)
                f.close()
                return 1


write_file("Test_file", "Gabriel Gome")