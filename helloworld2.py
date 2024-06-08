print("Welcome to my Project")
print("This is a calculator")
name = input("What is your name?: ")

print("Hello! " + name.upper())

print("Use + - * / to do Actions")
print("Press 'q' to quit")

print("Enjoy!")

while True:
    try:
        first = float(input("Type Your First NUMBER: "))  # Convert input to float
        second = float(input("Type the Next NUMBER: "))  # Convert input to float
        COMM = input("Please Select your desired Action (or 'q' to quit): ")
    except ValueError:  # Handling ValueError
        print("Invalid input! Please enter a valid number.")  # Handle invalid input
        continue  # Continue to the next iteration of the loop

    if COMM == "+":
        plus = first + second
        print("SUM:", plus)
    elif COMM == "-":
        diff = first - second
        print("DIFF:", diff)
    elif COMM == "*":
        pro = first * second
        print("PRODUCT:", pro)
    elif COMM == "/":
        if second == 0:
            print("Division by zero is not possible.")
        else:
            qus = first / second
            print("QUOTIENT:", qus)
    elif COMM.lower() == 'q':
        break

print("Thanks for using the calculator")