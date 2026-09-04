file = open("students.txt", "w")
file.close()

while True:
    print("\nStudent Management System")
    print("1. Write Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Count Students")
    print("5. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        fee = input("Enter Fee: ")

        file = open("students.txt", "a")
        file.write(roll + "," + name + "," + course + "," + fee + "\n")
        file.close()

        print("Student added successfully!")

    elif option == 2:
        file = open("students.txt", "r")

        print("\nStudent Details:")

        for line in file:
            print(line)

        file.close()

    elif option == 3:
        roll = input("Enter Roll Number to search: ")

        file = open("students.txt", "r")
        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == roll:
                print("\nStudent Found!")
                print("Roll Number:", data[0])
                print("Name:", data[1])
                print("Course:", data[2])
                print("Fee:", data[3])
                found = True

        file.close()

        if found == False:
            print("Student not found")

    elif option == 4:
        file = open("students.txt", "r")

        count = 0

        for line in file:
            count = count + 1

        file.close()

        print("Total Students:", count)

    elif option == 5:
        print("Exit")
        break

    else:
        print("Invalid option")