# Decorator

def my_decorator(func):
    def wrap_func():
        print("*****************")
        func()
        print("*****************")
    return wrap_func

@my_decorator
def hello():
    print("hellooooooooo")

@my_decorator
def bye():
    print("byeeeeee")

print(bye())
print(hello())