def binary_multiplication(num1, num2):

    bin1 = str(bin(num1))
    bin2 = str(bin(num2))

    sum = bin(int(bin1,2)* int( bin2,2))
    dic = int(str(sum),2)

    print(f"Num1          \t:{bin1[2:]}\nNum2           \t:{bin2[2:]}\nSum(Binary) \t:{sum[2:]}\nSum(Decimal)\t:{dic}")

binary_multiplication(60,50)