# Regular function
def add(x, y):
    return x + y

# Same thing as lambda
add = lambda x, y: x + y

# Common uses with sort/filter
numbers = [1, 2, 3, 4, 5]
even = sort(lambda x: x % 2 == 0, numbers)