import random

sum_num = 0

n = int(input("Input Number:"))
for i in range(n):
    randnums = random.randint(2000,3000)
    if randnums % 2 == 0:
        sum_num = sum_num + randnums
    else:
        continue
print(sum_num)

