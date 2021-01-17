# Decorator Pattern 

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*****************")
        func(*args, **kwargs)
        print("*****************")
    return wrap_func

@my_decorator
def hello(greeting, name, emoji=':)'):
    print(greeting , emoji, name, )

@my_decorator
def bye():
    print("byeeeeee")

# hello2 = my_decorator(hello)
# print(hello2("Hi "))

# print(bye())
hello("Hi ", "Mainul Islam")