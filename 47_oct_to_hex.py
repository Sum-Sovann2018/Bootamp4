
def oct_to_hex(oct):

    print(f"oct_to_hex({oct})")
    try:
        return hex(int(str(oct), 8))[2:].upper()

    except:
        return "This is not an octal number"

print(f"{oct_to_hex(1271)}")