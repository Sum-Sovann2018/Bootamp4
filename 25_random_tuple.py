
import random

def random_tuples(num1):
    num1 = int(num1)
    sum = 0
    tuples = ( )
    print(f"random_tuple({num1})\n")
    for i in range(1,num1 + 1):

        randoms = random.randint(0,100)

        sum = int(sum + randoms)
        tuples = tuples + (randoms,)

        print(f"Random number {i}: {randoms}")



    print(f"\n{tuples}\n")
    return sum

print(random_tuples(5))