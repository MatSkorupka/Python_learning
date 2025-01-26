store_data = {
    "locations": {
        "north": {
            "products": {
                "laptop": {"stock": 5, "reserved": 2, "price": 1000},
                "phone": {"stock": 10, "reserved": 3, "price": 800}
            },
            "staff": ["John", "Alice"],
            "status": "active"
        },
        "south": {
            "products": {
                "laptop": {"stock": 3, "reserved": 1, "price": 1000},
                "tablet": {"stock": 7, "reserved": 2, "price": 300}
            },
            "staff": ["Bob", "Carol"],
            "status": "maintenance"
        }
    },
    "global_discount": 0.1
}



# 1. Number of laptops in stock in north location
nb_of_laptops_north = store_data['locations']['north']['products']['laptop']['stock']
print(nb_of_laptops_north)

# 2. Status of south location
nb_of_laptops_south = store_data['locations']['south']['status']
print(nb_of_laptops_south)

# 3. Staff members in north location
nb_of_laptops_north2 = store_data['locations']['north']['staff']
print(nb_of_laptops_north2)

# 4. Price of tablet in south location
nb_of_laptops_south2 = store_data['locations']['south']['products']['tablet']['price']
print(nb_of_laptops_south2)