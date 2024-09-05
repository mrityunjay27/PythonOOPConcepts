"""
In Python, a decorator is a design pattern that allows you
to modify the functionality of a function by wrapping it in another function.

The outer function is called the decorator,
which takes the original function as an argument and returns a modified version of it.
"""


# 1. Nested function
def outer(x):
    def inner(y):
        return x + y

    return inner


add_five = outer(5)
result = add_five(6)
print(result)  # prints 11


# 2. Passing function in args.
def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)  # prints 10


# 3. Decorators
def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()

    # return the inner function
    return inner


# define ordinary function
def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()


# 4. Decorator with @

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()  # -> make_pretty(ordinary)()


# 5. Decorator

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)  # smart_divide(divide)(2,3)

divide(2, 0)
