# Library fine calculator (based on overdue days)

overdue_days = int(input("Enter your overdue days: "))
if overdue_days <= 0:
    fine = 0
    print("Your due amount is: ", fine)
elif overdue_days <= 5:
    fine = overdue_days * 1
    print("Your due amount is: ", fine)
elif overdue_days <= 10:
    fine = (5 * 1) + (overdue_days - 5) * 2
    print("Your due amount is: ", fine)
else:
    fine = (5 * 1) + (5 * 2) + (overdue_days - 10) * 5
    print("Your due amount is: ", fine)