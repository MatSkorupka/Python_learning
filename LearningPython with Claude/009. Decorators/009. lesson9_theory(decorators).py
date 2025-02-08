def my_decorator(func):
    def wrapper():
        print("Before any function")
        func()  # This will be whatever function we decorate
        print("After any function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

@my_decorator
def say_goodbye():
    print("Goodbye!")

# Testing both functions
say_hello()
print("\n")  # Just for spacing
say_goodbye()

# Output for say_hello():
# Before any function
# Hello!
# After any function

# Output for say_goodbye():
# Before any function
# Goodbye!
# After any function