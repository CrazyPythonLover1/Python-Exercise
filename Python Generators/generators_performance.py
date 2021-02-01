# Uses of Generator 

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f' It took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        # range func gives One by One item and hold it in memory
        # and removes any old number from memory
        i*5

@performance
def long_time2():
    for i in list(range(100000000)):
        i*5


long_time()  