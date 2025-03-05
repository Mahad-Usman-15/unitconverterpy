# Program to convert temperatures
inputfromuser = float(input("Enter the Temperature: "))
print("Select the unit")
print("1. Celsius")
print("2. Fahrenheit")
choice = input("Select option (1 or 2): ")
print("Select the second unit")
print("1. Celsius")
print("2. Fahrenheit")
choice_1 = input("Select option (1 or 2): ")
if choice == "1" and choice_1 == "2":
    result = (1.8 * inputfromuser) + 32
    print(f"Converted temperature: {result}°F")
elif choice == "2" and choice_1 == "1":
    result = (inputfromuser - 32) / 1.8
    print(f"Converted temperature: {result}°C")
elif choice == "1" and choice_1 == "1":
    result = inputfromuser
    print(f"Converted temperature: {result}°C")
elif choice == "2" and choice_1 == "2":
    result = inputfromuser
    print(f"Converted temperature: {result}°F")
else:
    print("Invalid input")

# Program to convert lengths
inputfromuser = float(input("Enter the length: "))
print("Select the unit")
print("1. Meters")
print("2. Feet")
choice = input("Select option (1 or 2): ")
print("Select the second unit")
print("1. Meters")
print("2. Feet")
choice_1 = input("Select option (1 or 2): ")
if choice == "1" and choice_1 == "2":
    result = inputfromuser * 3.28084
    print(f"Converted length: {result} feet")
elif choice == "2" and choice_1 == "1":
    result = inputfromuser / 3.28084
    print(f"Converted length: {result} meters")
elif choice == "1" and choice_1 == "1":
    result = inputfromuser
    print(f"Converted length: {result} meters")
elif choice == "2" and choice_1 == "2":
    result = inputfromuser
    print(f"Converted length: {result} feet")
else:
    print("Invalid choice")