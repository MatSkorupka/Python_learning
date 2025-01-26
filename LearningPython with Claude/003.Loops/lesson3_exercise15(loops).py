warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {'quantity': 50, 'price': 1000, 'min_stock': 20, 'max_stock': 100},
            'Phone': {'quantity': 100, 'price': 500, 'min_stock': 30, 'max_stock': 150}
        },
        'temperature': 20,
        'status': 'active'
    },
    'Zone B': {
        'items': {
            'Tablet': {'quantity': 75, 'price': 300, 'min_stock': 25, 'max_stock': 120},
            'Watch': {'quantity': 150, 'price': 200, 'min_stock': 50, 'max_stock': 200}
        },
        'temperature': 22,
        'status': 'active'
    }
}

# Exercise 1: Stock Level Check
# For each item, calculate how close it is to max_stock as a percentage
# Example: if quantity is 75 and max_stock is 100, it's 75% full

check = dict() 

for store in warehouse.keys():
    for item, value in warehouse[store].items():
        if item == 'items':
            for i, v in value.items():
                check[i] = v['quantity'] / v['max_stock'] * 100

print(check)

# Exercise 2: Restock Alerts
# Find items where quantity is less than or equal to min_stock
# Print how many items need to be ordered to reach max_stock

check2 = dict() 

for store in warehouse.keys():
    for item, value in warehouse[store].items():
        if item == 'items':
            for i, v in value.items():
                if v['quantity'] <= v['min_stock']:
                    items_needed = v['max_stock'] - v['quantity']
                    check2[i] = items_needed

for item, needed in check2.items():
    print(f"Restock alert: Order {needed} more {item}")

# Exercise 3: Zone Capacity
# For each zone calculate:
# - Current total items
# - Maximum possible items (sum of max_stock)
# - How much more could be stored (difference)

zone_stats = {
    'Zone A': {'current': 0, 'maximum': 0, 'available': 0},
    'Zone B': {'current': 0, 'maximum': 0, 'available': 0}
}

for store in warehouse.keys():
    for item, value in warehouse[store]['items'].items():
        zone_stats[store]['current'] += value['quantity']
        zone_stats[store]['maximum'] += value['max_stock']

for store in zone_stats:
    zone_stats[store]['available'] = zone_stats[store]['maximum'] - zone_stats[store]['current']

for zone, stats in zone_stats.items():
    print(f"\n{zone}:")
    print(f"- Current total items: {stats['current']}")
    print(f"- Maximum capacity: {stats['maximum']}")
    print(f"- Available space: {stats['available']}")