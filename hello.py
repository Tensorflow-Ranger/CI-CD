def say_hello():
    print("Hello, world!")

def verify_number(value):
    """
    Verify if the given value is a number (int or float).
    Returns True if it's a number, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    say_hello()
    # Example usage
    print(verify_number("123"))     # True
    print(verify_number("12.34"))   # True
    print(verify_number("abc"))     # False
