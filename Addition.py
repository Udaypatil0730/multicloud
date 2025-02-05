idef greet(name):
    """Function to greet a user."""
    return f"Hello, {devopd-multicloud}! Welcome to Git and GitHub learning."

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

if __name__ == "__main__":
    user_name = input("Enter your name: Uday ")
    print(greet(user_name))

    num1 = int(input("Enter first number: 20"))
    num2 = int(input("Enter second number: 30"))
    print(f"Sum: {add_numbers(num1, num2)}")
