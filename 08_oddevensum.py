oddSum = 0
evenSum = 0

even_count = 0
odd_count = 0

num = input("Input a number:")

if num.isdigit():
    num = int( num )

    for i in range( 1 , num  ):

        if i % 2 == 0:
            evenSum += i
            even_count += 1

        else:
            oddSum += i
            odd_count += 1

    print("Sum of odd numbers =",float(oddSum/odd_count))
    print("Sum of even numbers =",float(evenSum/even_count))

else:
    print("Invalid Input")


