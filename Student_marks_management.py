student_info = {}
while (True):
    print("1. Add student")
    print("2. Update marks")
    print("3. Display highest, lowest and average marks")
    print("4. Display all records")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        student_info[name] = marks
        print("Student added!!")
    elif ch == 2:
        name = input("Enter name to update mark: ")
        marks = int(input("Enter marks to update: "))
        student_info[name] = marks
        print("Marks updated!!")
    elif ch == 3:
        sum = 0
        c = 0
        min = 100
        max = 0
        for i in student_info:
            sum += student_info[i]
            c += 1
            if student_info[i] < min:
                min = student_info[i]
            if student_info[i] > max:
                max = student_info[i]
        print("Highest marks: ", max)
        print("Lowest marks: ", min)
        print("Average marks: ", sum/c)
    elif ch == 4:
        for i in student_info:
            print(i, " : ", student_info[i])
    elif ch == 5:
        break
    else:
        print("Wrong choice entered!!")