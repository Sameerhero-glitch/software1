correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break

    attempts += 1

    if attempts == 5:
        print("Access denied")

    else:
        print("Incorrect username or password. Please try again.")