smallest = None
largest = None


while True:

    number = input("Enter a number (or press Enter to quit): ")

    if number == "":
        break   
    number = float(number)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")