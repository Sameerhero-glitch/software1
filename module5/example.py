while True:
    print("Choose a calculation")
    print("1. Add")
    print("2. Minus")
    print("3. Multiplication")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == 4:
        print("Bye")   

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        answer = num1 + num2

    elif choice == "2":
        answer = num1 - num2

    elif choice == "3":
        answer = num1 * num2

    else:
        print("Invalid Choice")

    print("Answer:", answer)