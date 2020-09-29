str = input("Input a text:")

if str:
    length = round( len( str ) / 2)

    p1 = str[ 0:length ]
    p2 = str[length:]

    print(p1.upper()+""+p2)


else:
    print("The string is empty.")
