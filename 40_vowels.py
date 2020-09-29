
def vowels(str):

    print(f" vowels({str})")
    count = 0

    if str == " " or str.isdigit():
        return f"{count}\nNO VOWELS"


    else:
        cons = " "
        vowels = " "

        for i in str:

            if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":

                cons += i
                count += 1

            elif i == " ":
                continue

            else:
                vowels += i


        return f" {count}\n{cons.lower()}\n{vowels.upper()}"


print(vowels("what is that ?"))