# Build a version 2 of a calculator that adds,subtracts,multiplies,divides


print("Hello and Welcome to the Calculator ")

# Methods that return calculation

def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Make a choice, call the method and return the output to screen
print("What would you like to do today?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Menu System to select add, sub, mult, div
while True:
    choice = input("Enter input number 1/2/3/4: ")

    if choice in ("1","2","3","4"):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        if choice == "1":
            print(add(num1,num2))
        elif choice == "2":
            print(subtract(num1,num2))
        elif choice == "3":
            print(multiply(num1,num2))
        elif choice == "4":
            print(divide(num1,num2))
        break
    else:
        print("You did not enter a valid input")
# Output the Numbers

