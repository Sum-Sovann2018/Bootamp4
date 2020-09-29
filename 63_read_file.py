
def read_file(s):

    s = str(s)

    try:
        r_file = open(s)
        return f"{r_file.read()}\n{r_file.close()}"

    except:
        print("Invalid FILENAME")
        return 0

print(read_file("60_message_converter.py"))
