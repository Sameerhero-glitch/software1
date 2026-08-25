money = float(input("Give Money: "))

cost_of_coffee = 5

if money >= cost_of_coffee:
    print("You can buy Coffee")

    if money >= 20:
        print("You can also buy cake")


    takeout = input("Coffee to go?")

    if takeout == "yes":
        print("User is taking the coffee to go")

    if takeout == "no":
        print("User is having the coffee in the cafe")