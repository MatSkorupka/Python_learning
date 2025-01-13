# Store Performance Data
stores = ['North', 'South', 'East']
items = ['Coffee', 'Tea', 'Snacks']
prices = [5, 4, 3]

weekly_sales = {
    'Monday': {
        'North': [20, 15, 10],
        'South': [15, 20, 25],
        'East': [10, 10, 15]
    },
    'Tuesday': {
        'North': [25, 20, 12],
        'South': [20, 15, 20],
        'East': [15, 15, 10]
    },
    'Wednesday': {
        'North': [15, 10, 8],
        'South': [25, 18, 22],
        'East': [12, 12, 18]
    }
}

# Exercise 1:
# Calculate total sales for each store
# Store results in a dictionary: {'North': X, 'South': Y, 'East': Z}

total_sales = dict.fromkeys(stores, 0)

for key, ws in zip(weekly_sales.keys(), weekly_sales.values()):
    for k,v in zip(ws.keys(), ws.values()):
        sum_v = sum(v)
        total_sales[k] += sum_v

print(total_sales)



# Exercise 2:
# Calculate total revenue for each item across all stores
# Remember: revenue = price * quantity

revenue = dict.fromkeys(items, 0)

for day in weekly_sales: 
    for store in weekly_sales[day]: 
        sales = weekly_sales[day][store] 
        for item_index, item in enumerate(items):
            revenue[item] += sales[item_index] * prices[item_index]

print(revenue)

# Exercise 3:
# Find best performing store for each item
# Result should show which store sold most of each item


best_store = dict.fromkeys(items, '')
max_sales = dict.fromkeys(items, 0)  

for day in weekly_sales:
    for store in weekly_sales[day]:
        sales = weekly_sales[day][store]  
        for item_index, item in enumerate(items):
            if sales[item_index] > max_sales[item]:
                max_sales[item] = sales[item_index]
                best_store[item] = store

print(best_store)