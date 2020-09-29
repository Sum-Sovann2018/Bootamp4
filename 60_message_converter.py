def message_converter(str):

    res = ""

    for i in str:
        res += hex(int(ord(i)))[2:].upper()

    print(res)

message_converter("Hello")