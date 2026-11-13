while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("8. Show all formulas")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 7:
        print("Thank you! Exiting the program.")
        break

    elif choice == 8:
        print("\n--- Temperature Conversion Formulas ---")
        print("1. Celsius to Fahrenheit: (C * 9/5) + 32")
        print("2. Fahrenheit to Celsius: (F - 32) * 5/9")
        print("3. Celsius to Kelvin: C + 273.15")
        print("4. Kelvin to Celsius: K - 273.15")
        print("5. Fahrenheit to Kelvin: (F - 32) * 5/9 + 273.15")
        print("6. Kelvin to Fahrenheit: (K - 273.15) * 9/5 + 32")
        continue

    elif choice >= 1 and choice <= 6:
        temp = float(input("Enter the temperature: "))

        if choice == 1:
            result = (temp * 9/5) + 32
            print("Temperature in Fahrenheit:", result)

        elif choice == 2:
            result = (temp - 32) * 5/9
            print("Temperature in Celsius:", result)

        elif choice == 3:
            result = temp + 273.15
            print("Temperature in Kelvin:", result)

        elif choice == 4:
            result = temp - 273.15
            print("Temperature in Celsius:", result)

        elif choice == 5:
            result = (temp - 32) * 5/9 + 273.15
            print("Temperature in Kelvin:", result)

        elif choice == 6:
            result = (temp - 273.15) * 9/5 + 32
            print("Temperature in Fahrenheit:", result)

    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
