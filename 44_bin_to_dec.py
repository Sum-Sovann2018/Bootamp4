def bin_to_dec(bin):

    print(f"bin_to_dec({bin})")
    try:
        return int(str(bin), 2)

    except:
        return "This is not a binary number"

print(f"{bin_to_dec(110011)}")