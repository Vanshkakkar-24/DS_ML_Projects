# Grade Calculator

marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("You have score A grade!!")
elif marks >=75 and marks < 90:
    print("You have scored B grade!!")
elif marks >= 50 and marks < 75:
    print("You have scored C grade!!")
elif marks >=0 and marks < 50:
    print("You have scored D grade!!")
else:
    print("Enter valid marks")