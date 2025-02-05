def greet(name):
    """Function to greet a user."""
    return f"Hello, {name}! Welcome to Git and GitHub learning."

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum: {add_numbers(num1, num2)}")
