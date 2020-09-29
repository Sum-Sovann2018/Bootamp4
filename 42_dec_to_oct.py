def dec_to_oct (dec):
    print(f"dec_to_oct({dec})")

    decs = oct(dec)
    decs = str(decs)

    return decs.replace("0o","")


print(dec_to_oct(98))