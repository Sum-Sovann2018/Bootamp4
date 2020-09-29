
oddSum = 0
evenSum = 0
num = input("Input a number:")

if num.isdigit():
    num = int( num )

    for i in range( 1, num + 1 ):

        if i % 2 == 0:
            evenSum += i

        else:
            oddSum += i

else:
    print("Invalid Input")

print("Sum of odd numbers = ",evenSum)
print("Sum of even numbers = ",oddSum)

