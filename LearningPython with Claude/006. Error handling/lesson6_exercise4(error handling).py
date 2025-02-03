# More complex inventory system
warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {'price': 1000, 'stock': 5, 'location': 'A1'},
            'Phone': {'price': 500, 'stock': '10', 'location': 'A2'}  # Note: stock as string
        },
        'status': 'active'
    },
    'Zone B': {
        'items': {
            'Tablet': {'price': 300, 'stock': 0, 'location': 'B1'},
            'Watch': {'price': None, 'location': 'B2'}  # Note: missing stock, None price
        },
        'status': 'maintenance'
    }
}

# Create functions that:
# 1. Get item availability (handle: wrong zone, wrong item, invalid stock format)

def check_availability(zone_name, item_name):
    try:
        if zone_name not in warehouse:
            raise KeyError(f"Zone {zone_name} not found")
            
        if warehouse[zone_name]['status'] != 'active':
            raise ValueError(f"Zone {zone_name} is not active")
            
        # Now check item
        item = warehouse[zone_name]['items'].get(item_name)
        if item is None:
            raise KeyError(f"Item {item_name} not found in {zone_name}")
            
        # Check stock - handle string or missing stock
        try:
            stock = int(item.get('stock', 0))
        except (ValueError, TypeError):
            raise ValueError(f"Invalid stock format for {item_name}")
            
        return {
            'item': item_name,
            'zone': zone_name,
            'stock': stock,
            'location': item.get('location', 'Unknown')
        }
        
    except KeyError as e:
        return str(e)
    except ValueError as e:
        return str(e)

# Test cases
print(check_availability('Zone A', 'Laptop'))    # Should work
print(check_availability('Zone C', 'Laptop'))    # Wrong zone
print(check_availability('Zone A', 'Camera'))    # Wrong item
print(check_availability('Zone B', 'Tablet'))    # Zone in maintenance
