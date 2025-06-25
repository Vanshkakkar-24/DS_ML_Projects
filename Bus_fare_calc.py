# Bus ticket fare calculator (with age-based discount)

base_fare = int(input("Enter the base fare: "))
age = int(input("Enter your age: "))
if age < 5 and age >= 0:
    print("Your ticket is free!!")
elif age >= 5 and age <=18:
    fare = base_fare * 0.7
    print("Your ticket fare will be: ", fare, " rupees")
elif age > 60:
    fare = base_fare * 0.5
    print("Your ticket fare will be: ", fare, " rupees")
else:
    print("Your ticket fare is: ", base_fare)