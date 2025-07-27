"""Simple command-line calculator supporting basic operations."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    op = input("Operation: ").strip()
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers")
        return

    try:
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print("Unsupported operation")
            return
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
