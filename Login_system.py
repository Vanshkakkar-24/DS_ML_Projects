# Simple login system (with 3 attempts)

username = 'vansh@24'
password = 123456
attempt = 3

while attempt > 0:
    user = input("Enter your userame: ")
    pin = input("Enter your password: ")
    if user == username and pin == str(password):
        print("Access granted")
        break
    else:
        attempt -= 1
        print("Invalid credentials! ", attempt, " attempts left")
