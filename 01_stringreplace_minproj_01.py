

b = True


while b:

    print("Please input a paragraph:\n")
    P = input()

    p_lower = P.lower()

    print("\nPlease input a Search String:\n")
    sch_str = input()


    results = 0
    sub_len = len(sch_str)

    for i in range(len(p_lower)):
        if p_lower[i:i+sub_len] == sch_str:
            results += 1

    print("\nThere are ",results," occurrences.")

    print("\nDo you want to replace the text [Y/N]?\n")
    s = input()

    if s == "Y" or s == "y":
        print("Please input a replacement string:\n")
        rep = input()

        print("\nHow many occurrences do you want to replace?")
        acc_time = int(input())

        new_p = ""
        count = 0

        for i in p_lower.split():
            if i == sch_str and count < acc_time:

                new_p += rep + " "
                count += 1

            else:

                new_p += i + " "

        print(acc_time,"words has been replaced from the paragrap\n")
        print(new_p)

        b = False

    elif s == "N" or s == "n":
        print("Oh!you don’t like to replace, Do you want to check again [Y/N]?\n")

        s1 = input()

        if s1 == "Y" or s1 == "y":
            continue

        elif s1 == "N" or s1 == "n":
            b = False

        else:
            b = False

    else:
        print("\n“Please give proper input”\n")
        print("Do you want to replace the text [Y/N]?\n")
        s1 = input()

        if s1 == "Y" or s1 == "y":
            continue

        elif s1 == "N" or s1 == "n":
            print("\nOh!you don’t like to replace, Do you want to check again [Y/N]?\n")
            s2 = input()

            if s2 == "Y" or s2 == "y":
               continue

            elif s2 == "N" or s2 == "n":
               b = False

            else:
               b = False
        else:
            b = False








