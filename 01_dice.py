



import random

s = 0
sum = 0
b = True

print("Welcom to the dices game!\n")
while b  :

    num = input("Enter the number of dices you want to roll: ")
    if num.isdigit():
        num = int(num)
        if num <= 8 and num >= 1:
            if num == 1 :
                s = random.randint( 1 , 6 )
                sum += s
                print(f"\nRESULT:{sum}\n")
                break

            for i in range(1 , num + 1) :
                s = random.randint( 1 , 6 )
                sum += s
                print( f"\nDice{i}:{s}")

            print("\n==========")
            print(f"\nRESULT:{sum}")
            print("\n==========")
            break

        else:
            print("\nUSAGE: the number must be between 1 and 8\n")
            continue

    else:
        print("\nUSAGE: the number must be between 1 and 8\n")
        continue
