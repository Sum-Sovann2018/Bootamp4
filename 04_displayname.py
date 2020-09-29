name = input("Enter your name:")
time = int(input("Enter number of times to display:"))

if name.isalpha():
   for i in range(time):
        print(name)
else:
    print("No name entered")