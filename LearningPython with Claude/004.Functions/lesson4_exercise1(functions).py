# Exercise 1: Create a function that calculates profit
# Input: price and cost
# Output: profit per item (price - cost)

# Exercise 2: Create a function that calculates total profit
# Input: price, cost, and quantity sold
# Output: total profit

# Exercise 3: Create a function that checks if stock needs reordering
# Input: current_stock and minimum_stock
# Output: True if current_stock <= minimum_stock, False otherwise

# Let's test with this data:
price = 100
cost = 60
quantity_sold = 5
current_stock = 10
minimum_stock = 15


def profit(price, cost):
    result = price - cost
    return result

# Test the function
test_price = 100
test_cost = 60
profit_per_item = profit(test_price, test_cost)
print(f"Profit per item: ${profit_per_item}")

# Exercise 2:
def total_profit(price, cost, quantity_sold):
    result = (price * quantity_sold) - (cost * quantity_sold)
    return result


# Test the function
test_price = 100
test_cost = 60
test_quantity = 5
profit_total = total_profit(test_price, test_cost, test_quantity)
print(f"Profit per item: ${profit_total}")


# Exercise 3:
def alert(current_stock, minimum_stock):
    if current_stock <= minimum_stock:
        result = f'Current stock {current_stock} is less than minimum stock {minimum_stock}'
    else:
        result = False
    return result


# Test the function
current_stock = 10
minimum_stock = 15

alert_result = alert(current_stock, minimum_stock)

print(f'{alert_result}')
