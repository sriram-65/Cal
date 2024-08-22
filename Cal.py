def print_header():
    print("=" * 40)
    print(" " * 10 + "Calculator by Sriram")
    print("=" * 40)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def exponentiation(x, y):
    return x ** y

def print_operations():
    print("\nSelect an operation:")
    print("-" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("-" * 40)

def calculator():
    print_header()
    
    while True:
        print_operations()
        
        choice = input("Enter your choice (1/2/3/4/5/6) or 'q' to quit: ").strip()
        
        if choice == 'q':
            print("\n" + "=" * 40)
            print(" " * 10 + "Thank you for using the calculator!")
            print("=" * 40)
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            print("-" * 40)

            if choice == '1':
                result = add(num1, num2)
                operation = "+"

            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"

            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"

            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            elif choice == '5':
                result = modulus(num1, num2)
                operation = "%"

            elif choice == '6':
                result = exponentiation(num1, num2)
                operation = "**"

            print(f"\nResult: {num1} {operation} {num2} = {result}")
            print("=" * 40)
        else:
            print("\nInvalid input! Please try again.")
            print("-" * 40)

# Run the calculator
calculator()
