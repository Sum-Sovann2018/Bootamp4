def bin_to_hex(bin):

    print(f"bin_to_oct({bin})")
    try:
        return oct(int(str(bin), 2))[2:]

    except:
        return "This is not a binary number"

print(f"{bin_to_hex(11001101)}")