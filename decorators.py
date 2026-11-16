def hellodeco(func):
    def inner():
        print("Hello")
        func()
        print("Welcome")
    return inner

@hellodeco
def greet():
    print("Hi")

greet()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))


def decor1(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def decor2(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decor1
@decor2
def multiply(a, b):
    return a * b

print(multiply(4, 5))


