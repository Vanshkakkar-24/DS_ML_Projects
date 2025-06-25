# Age Checker

age = int(input("Enter your age: "))
if age > 0:
    if age >= 18:
        print("You are eligible for voting and driving")
    elif age < 18:
        print("You are not eligible for voting and driving")
else:
    print("Enter a valid age")