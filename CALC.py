print("Welcome to my Project")

print("This is a calculator")
name = input("What is your name?: ")

print("Hello! " + name.upper())

print("Use + - * / to do Actions")
print("Press 'q' to quit")

print("Enjoy!")

while True:
    try:
        first = str(input("Type Your First NUMBER (or 'q' to quit): "))
        if first == "q":
            break
        second = float(input("Type the Next NUMBER: "))
        COMM = input("Please Select your desired Action ")

    except ValueError:

        print("Invalid input! Please enter a valid number.")
        continue

    if COMM == "+":
        plus = float(first) + second
        print("SUM:", plus)
    elif COMM == "-":
        diff = float(first) - second
        print("DIFF:", diff)
    elif COMM == "*":
        pro = float(first) * second
        print("PRODUCT:", pro)
    elif COMM == "/":
        if second == 0:
            print("Division by zero is not possible.")
        else:
            qus = float(first) / second
            print("QUOTIENT:", qus)
    elif COMM.lower() == 'q':
        break

print("Thanks for using the calculator")
