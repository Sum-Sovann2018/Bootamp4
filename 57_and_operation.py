def and_operation(hex1, hex2):

    res1 = bin(int(hex1,16))[2:]
    res2 = bin(int(hex2,16))[2:]

    print(f"{res1}\n{res2}\n")
    res = ""

    for i in range(len(res1)):
        res += "1" if int(res1[i])*int(res2[i]) == 1 else "0"

    print(res)
and_operation("33","3D")