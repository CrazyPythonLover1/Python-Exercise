def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

print(make_list(100))

# this the exact same thing 
# print(list(range(10)))