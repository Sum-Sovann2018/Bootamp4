A = int(input("Input your age:"))

if A >= 18:
    print("You are eligible to vote")

elif A>=0 and A < 18:
    print("You aren't adult yet...Sorry can't vote")

else:
    print("Age must be a positive digit")

