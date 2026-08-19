# Unit Converter

def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")

    choice = input("Enter your choice: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 0.621371
        print(f"{value} km = {result:.2f} miles")

    elif choice == "2":
        result = value * 1.60934
        print(f"{value} miles = {result:.2f} km")

    elif choice == "3":
        result = value * 3.28084
        print(f"{value} meters = {result:.2f} feet")

    elif choice == "4":
        result = value * 0.3048
        print(f"{value} feet = {result:.2f} meters")

    else:
        print("Invalid choice!")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")

    choice = input("Enter your choice: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 2.20462
        print(f"{value} kg = {result:.2f} pounds")

    elif choice == "2":
        result = value * 0.453592
        print(f"{value} pounds = {result:.2f} kg")

    elif choice == "3":
        result = value / 1000
        print(f"{value} grams = {result:.2f} kg")

    elif choice == "4":
        result = value * 1000
        print(f"{value} kg = {result:.2f} grams")

    else:
        print("Invalid choice!")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice: ")
    value = float(input("Enter temperature: "))

    if choice == "1":
        result = (value * 9 / 5) + 32
        print(f"{value}°C = {result:.2f}°F")

    elif choice == "2":
        result = (value - 32) * 5 / 9
        print(f"{value}°F = {result:.2f}°C")

    elif choice == "3":
        result = value + 273.15
        print(f"{value}°C = {result:.2f} K")

    elif choice == "4":
        result = value - 273.15
        print(f"{value} K = {result:.2f}°C")

    else:
        print("Invalid choice!")


def time_converter():
    print("\n--- Time Converter ---")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    print("3. Minutes to Seconds")
    print("4. Seconds to Minutes")

    choice = input("Enter your choice: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 60
        print(f"{value} hours = {result:.2f} minutes")

    elif choice == "2":
        result = value / 60
        print(f"{value} minutes = {result:.2f} hours")

    elif choice == "3":
        result = value * 60
        print(f"{value} minutes = {result:.2f} seconds")

    elif choice == "4":
        result = value / 60
        print(f"{value} seconds = {result:.2f} minutes")

    else:
        print("Invalid choice!")


def main():
    while True:

        print("\n==============================")
        print("       UNIT CONVERTER")
        print("==============================")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Time")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == "1":
                length_converter()

            elif choice == "2":
                weight_converter()

            elif choice == "3":
                temperature_converter()

            elif choice == "4":
                time_converter()

            elif choice == "5":
                print("Thank you for using Unit Converter!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")


main()
