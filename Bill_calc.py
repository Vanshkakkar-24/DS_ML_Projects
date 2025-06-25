# Electricity bill generator (based on units)

units = int(input("Enter your units consumed: "))
if units <= 100:
    bill = units * 3
    print("Your bill amount is: ", bill)
elif units <= 200:
    bill = (100 * 3) + (units - 100) * 5
    print("Your bill amount is: ", bill)
else:
    bill = (100 * 3) + (100 * 5) + (units - 200) * 8
    print("Your bill amount is: ", bill)