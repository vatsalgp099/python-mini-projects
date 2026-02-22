def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

result = 0
op = True

first_number = int(input("Enter the first number: "))

while op:
    operation = input("+\t-\t*\t/\nPick an operation: ")
    second_number = int(input("Enter the second number: "))

    if operation == "+":
        result = add(first_number, second_number)
    elif operation == "-":
        result = subtract(first_number, second_number)
    elif operation == "*":
        result = multiply(first_number, second_number)
    elif operation == "/":
        result = divide(first_number, second_number)
    else:
        print("Invalid operation")

    print(result)

    choice = input(f"Type 'y' to continue with {result} , to exit type 'n' ")

    if choice == "y":
        op = True
        first_number = result
    elif choice == "n":
        op = False



