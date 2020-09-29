def dec_to_oct (dec):
    print(f"dec_to_hexa({dec})")

    decs = hex(dec)
    decs = str(decs)

    return decs.replace("0x","").upper()


print(dec_to_oct(1500))