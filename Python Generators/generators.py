def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

print(make_list(100))

# this the exact same thing 
# print(list(range(10)))

# creating for Loop

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
special_for([1,2,3,4])


# Under the Hood Generator 
# Creating range function   

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self): 
        # able to loop bcz of __iter__ (iterable)
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 0)
for i in gen:
    print(i)


# Fibonacci Numbers

def fib(num):
    first = 0
    second = 1
    for i in range(num):
        third = first + second
        first = second
        print(second)
        second = third

# fib(20)

# another way with generator

def fib2(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


# for i in fib2(11):
#     print(i)

# another way with list

def fib3(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b 
    return result



print(fib3(11))