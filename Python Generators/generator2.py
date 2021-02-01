# Generator 

def generator_function(num):
    for i in range(num):
        yield i # pauses the function and remember the recent value 
        # or track the state

gen = generator_function(100)

next(gen)
next(gen)
print(next(gen))

for item in generator_function(100):
    print(item)