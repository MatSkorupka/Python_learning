# Regular function
def create_list(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

# Generator function
def create_generator(n):
    for i in range(n):
        yield i

# Compare usage:
list_numbers = create_list(5)      # Creates all numbers at once
gen_numbers = create_generator(5)   # Creates numbers one at a time

print(list_numbers)                # [0, 1, 2, 3, 4]
print(next(gen_numbers))           # 0
print(next(gen_numbers))           # 1



