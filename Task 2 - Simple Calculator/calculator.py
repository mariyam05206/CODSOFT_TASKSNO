# Simple Calculator
# Task 2

print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Floor Division (//)")
print("7. Power (**)")

choice = input("Enter your choice (1-7): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")

elif choice == "5":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Cannot find modulus with zero.")

elif choice == "6":
    if num2 != 0:
        print("Result:", num1 // num2)
    else:
        print("Error: Cannot divide by zero.")

elif choice == "7":
    print("Result:", num1 ** num2)

else:
    print("Invalid choice.")
