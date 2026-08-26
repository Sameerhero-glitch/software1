menu_list = "select option:\n1. add \n2. minus \n3. multiply \n0. exit \n"
selection = input(menu_list)

while selection != "0":
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))

    if selection == 1:
        print(f"Result: {first_number + second_number}")

    elif selection == 2:
        print(f"Result: {first_number - second_number}")

    elif selection == 3:
        print(f"Result: {first_number * second_number}")

    else:
         print(f"Incorrect option")

    menu_list = "select option:\n1. add \n2. minus \n3. multiply \n0. exit"
    selection = input(menu_list)