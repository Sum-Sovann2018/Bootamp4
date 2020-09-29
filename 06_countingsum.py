b = True

print("Input a number:")
num = int( input() )

sum = num

while b:
    num = input("Input a number:")

    if num.isdigit():
        num = int( num )
        sum += num

    elif num == "stop":
        sum = int(sum)
        print("Sum =",sum)
        b = False

    else:
        print("The input must be a valid number!")
        continue
