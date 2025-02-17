def generate_chain_sales():
    """
    Generator for multiple store locations:
    - Track 3 stores: 'North', 'South', 'Central'
    - Each store has different sales patterns:
        * North: sells 0-3 books/day
        * South: sells 1-5 books/day
        * Central: sells 2-8 books/day
    - Restock when any store falls below 20 books
    - Track each store's profit (books sold * 20$)
    """
    stores = {
        'North': {'stock': 50, 'total_sales': 0, 'profit': 0, 'sales_range': (0, 3)},
        'South': {'stock': 50, 'total_sales': 0, 'profit': 0, 'sales_range': (1, 5)},
        'Central': {'stock': 50, 'total_sales': 0, 'profit': 0, 'sales_range': (2, 8)}
    }
    day = 1
    
    # Your code here


    while True:
        daily_report = {'day': day, 'stores': {}}
        
        for store_name, store_data in stores.items():
            # Get sales range for this store
            min_sales, max_sales = store_data['sales_range']
            sales = random.randint(min_sales, max_sales)
            
            # Update store data
            store_data['stock'] -= sales
            store_data['total_sales'] += sales
            store_data['profit'] += sales * 20
            
            # Restock if needed
            if store_data['stock'] < 20:
                store_data['stock'] += 50  # Restock more when low
            
            # Add to daily report
            daily_report['stores'][store_name] = {
                'stock': store_data['stock'],
                'sales_today': sales,
                'total_sales': store_data['total_sales'],
                'profit': store_data['profit']
            }
        
        yield daily_report
        day += 1

# Test
chain = generate_chain_sales()
for _ in range(3):
    print(next(chain))

