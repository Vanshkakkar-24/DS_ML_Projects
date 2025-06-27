import numpy as np
while True:
    travel = int(input("Enter travel expenses: "))
    elec = int(input("Enter electricity expenses: "))
    food = int(input("Enter food expenses: "))
    cloth = int(input("Enter clothing expenses: "))
    rent = int(input("Enter rent expenses: "))
    expense = np.array([travel, elec, food, cloth, rent])
    category = np.array(['Travel', 'Electricity', 'Food', 'Cloth', 'Rent'])
    print("-----Expense report-----")
    print()
    for i in range(5):
        print(f"{category[i]} expense: {expense[i]}")
    print()
    print(f"Total expense: {expense.sum()}")
    print(f"Average expense: {expense.sum()/5}")
    print(f"Highest expense: {expense.max()}")
