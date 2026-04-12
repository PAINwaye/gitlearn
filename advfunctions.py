import re

# ---------------- ITERATOR ----------------
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

def run_iterator():
    n = int(input("Enter max number: "))
    counter = CountUp(n)
    print("Iterator Output:")
    for i in counter:
        print(i)


# ---------------- GENERATOR ----------------
def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

def run_generator():
    n = int(input("Enter limit: "))
    print("Even numbers:")
    for num in even_numbers(n):
        print(num)


# ---------------- DECORATOR ----------------
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello from decorated function!")

def run_decorator():
    say_hello()


# ---------------- CLOSURE ----------------
def outer_function(msg):
    def inner_function():
        print("Message:", msg)
    return inner_function

def run_closure():
    msg = input("Enter a message: ")
    closure_func = outer_function(msg)
    closure_func()


# ---------------- REGEX ----------------
def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")

def run_regex():
    email = input("Enter email: ")
    check_email(email)


# ---------------- MENU ----------------
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Iterator Example")
        print("2. Generator Example")
        print("3. Decorator Example")
        print("4. Closure Example")
        print("5. Regex Example")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_iterator()
        elif choice == '2':
            run_generator()
        elif choice == '3':
            run_decorator()
        elif choice == '4':
            run_closure()
        elif choice == '5':
            run_regex()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
if __name__ == "__main__":
    main()