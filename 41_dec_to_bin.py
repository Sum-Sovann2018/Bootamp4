
def dec_to_bin (dec):
   print(f"dec_to_bin({dec})")

   decs = bin(dec)
   decs = str(decs)

   return decs.replace("0b","")


print(dec_to_bin(50))