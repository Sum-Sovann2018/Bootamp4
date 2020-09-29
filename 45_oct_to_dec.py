def oct_to_dec(oct):

    print(f"oct_to_dec({oct})")
    try:
        return int(str(oct), 8)

    except:
        return "This is not an octal number"

print(f"{oct_to_dec(750)}")


