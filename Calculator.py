import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

# Main function to run the calculator
def calculator():
    print("Scientific Calculator\n")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Square Root")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")

    choice = input("\nEnter choice (1-11): ")

    if choice in ('1', '2', '3', '4', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '7':
            print(num1, "^", num2, "=", power(num1, num2))

    elif choice in ('5', '6', '8', '9', '10', '11'):
        num = float(input("Enter a number: "))

        if choice == '5':
            print("Square of", num, "=", square(num))

        elif choice == '6':
            print("Cube of", num, "=", cube(num))

        elif choice == '8':
            print("Square root of", num, "=", square_root(num))

        elif choice == '9':
            print("Sine of", num, "=", sin(num))

        elif choice == '10':
            print("Cosine of", num, "=", cos(num))

        elif choice == '11':
            print("Tangent of", num, "=", tan(num))

    else:
        print("Invalid input")

# Call the calculator function to start the program
calculator()
