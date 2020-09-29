

b = True

while b:

    print("Press 1 to encode\nPress 2 to decode")
    num = int(input())

    if num == 1:
        print("Enter the string to encode:")

        str = input()
        char = ""

        for i in str:
            ascii = ord( i )

            if ascii >=65 and ascii <= 77:
                ascii = ascii + 13
                char += chr(ascii)

            elif ascii > 77 and ascii <= 90:
                ascii = ascii - 13
                char += chr(ascii)

            else:
                continue

        print("The decoded text is:"+ char)
        print("Do you want to continue? [Y/N]")

        s = input()

        if s == "Y":
            continue

        elif s == "N":
            b = False

        else:
            b = False

    elif num == 2:
        print("Enter the string to decode:")
        str = input()
        char = ""

        for i in str:
            ascii = ord( i )

            if ascii >=65 and ascii <= 77:
                ascii = ascii + 13
                char += chr(ascii)

            elif ascii > 77 and ascii <= 90:
                ascii = ascii - 13
                char += chr(ascii)

            else:
                continue

        print("The decoded text is:"+ char)
        print("Do you want to continue? [Y/N]")
        s = input()

        if s == "Y":
            continue

        elif s == "N":
            b = False

        else:
            b = False

    else:
        b = False






