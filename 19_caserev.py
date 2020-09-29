
str = input("Enter a string:")

if str.isalpha():
   for i in str:
      ascii = ord(i)
      if ascii >= 97:
         ascii = ascii - 32
         print(chr(ascii),end="")

      elif ascii <= 97:
         ascii = ascii + 32
         print(chr(ascii),end="")

      else:
         print("The string is empty.")
else:
   print("The string is empty.")



