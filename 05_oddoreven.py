print("Input a number:")
num = input()

if num.isdigit():
    num = int( num )
    print("Even Number" if num %2==0
          else "Odd Number")
else:
    print("Not a valid Numbe")