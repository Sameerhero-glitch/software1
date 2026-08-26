zander_size = float(input("Enter the length of the zander in centimeters: "))

if zander_size < 42:
    missing_cm = 42 - zander_size
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing_cm:.1f} centimeters below the size limit.")

else:
    print("The zander meets the size limit.")

