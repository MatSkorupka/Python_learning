warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {
                'quantity': 50,
                'price': 1000,
                'sales_last_month': 30,
                'cost': 800
            },
            'Phone': {
                'quantity': 100,
                'price': 500,
                'sales_last_month': 45,
                'cost': 350
            }
        }
    },
    'Zone B': {
        'items': {
            'Tablet': {
                'quantity': 75,
                'price': 300,
                'sales_last_month': 25,
                'cost': 200
            },
            'Watch': {
                'quantity': 150,
                'price': 200,
                'sales_last_month': 60,
                'cost': 120
            }
        }
    }
}

# Exercise 1: Sales Performance
# Calculate for each item:
# - Revenue (sales * price)
# - Profit (revenue - (sales * cost))
# Print items sorted by profit

item_list = []
for store in warehouse.keys():
    for k in warehouse[store].keys():
        for item in warehouse[store][k].keys():
            item_list.append(item)

revenue = dict.fromkeys(item_list, 0)
profit = dict.fromkeys(item_list, 0)


for store in warehouse.keys():
    for k in warehouse[store].keys():
        for item, value in warehouse[store][k].items():
            revenue[item] += value['sales_last_month'] * value['price']
            profit[item] += revenue[item] - (value['sales_last_month'] * value['cost'])



print("\nRevenue by item:")
for item, value in revenue.items():
    print(f"{item}: ${value}")

print("\nProfit by item:")
for item, value in profit.items():
    print(f"{item}: ${value}")


# Exercise 2: Turnover Rate
# Calculate for each item:
# - What percentage of stock was sold last month
# Print which items need attention (< 20% turnover)

item_list = []
for store in warehouse.keys():
    for k in warehouse[store].keys():
        for item in warehouse[store][k].keys():
            item_list.append(item)

quantity_value = dict.fromkeys(item_list, 0)
percentage = dict.fromkeys(item_list, 0)

for store in warehouse.keys():
    for k in warehouse[store].keys():
        for item, value in warehouse[store][k].items():
            quantity_value[item] += value['sales_last_month'] 
            percentage[item] += value['sales_last_month'] / value['quantity']

for items, values in percentage.items():
    if values < 0.2:
        print(f'Pay attention on {items}, becouse turnover value is {values}')


# Exercise 3: Basic Inventory Metrics
# For each zone calculate:
# - Total revenue
# - Average profit margin ((price - cost)/price * 100)
# - Best selling item (by quantity)

store_list = []
item_list = []
for store in warehouse.keys():
    store_list.append(store)
    for item in warehouse[store]['items'].keys():  # Fix: use 'items' directly
        item_list.append(item)

revenue_zone = dict.fromkeys(store_list, 0)
best_selling = dict.fromkeys(store_list, {'item': '', 'sales': 0})  # Track best selling item
margin_zone = dict.fromkeys(store_list, 0)

for store in warehouse.keys():
    total_price = 0
    total_cost = 0
    items_count = 0
    
    for item, value in warehouse[store]['items'].items():
        revenue_zone[store] += value['sales_last_month'] * value['price']
        
        if value['sales_last_month'] > best_selling[store]['sales']:
            best_selling[store] = {
                'item': item,
                'sales': value['sales_last_month']
            }
        
        total_price += value['price']
        total_cost += value['cost']
        items_count += 1
    
    margin_zone[store] = ((total_price - total_cost) / total_price) * 100

for store in store_list:
    print(f"\n{store}:")
    print(f"Total revenue: ${revenue_zone[store]}")
    print(f"Average profit margin: {margin_zone[store]:.1f}%")
    print(f"Best selling item: {best_selling[store]['item']} ({best_selling[store]['sales']} units)")



