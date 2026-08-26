gender = input("Enter biological gender (male/female): ").lower()
hg_value = float(input("Enter hemoglobin value (g/l): "))

if gender == "male":
        if hg_value<134:
            print("Your hemoglobin is low.")

        elif hg_value>=167:
            print("Your hemoglobin is high.")

        else:
            print("Your hemoglobin is normal.")


elif gender == "female":
        if hg_value<117:
            print("Your hemoglobin is low.")

        elif hg_value>=155:
            print("Your hemoglobin is high.")

        else:
            print("Your hemoglobin is normal.")

else:
    print("Invalid gender.")