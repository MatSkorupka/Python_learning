def data_pipeline():
    """
    Generator that simulates an ETL pipeline:
    - Extract: Generate raw data (sales records)
    - Transform: Clean and enrich the data
    - Load: Prepare for loading to database
    
    Each record contains:
    - timestamp
    - product_id
    - quantity
    - price
    - calculated total
    - status (processed/error)
    """
    import random
    from datetime import datetime, timedelta
    
    current_time = datetime.now()
    product_prices = {'A': 100, 'B': 200, 'C': 300}

    while True:
        try:
            # Extract
            product_id = random.choice(['A', 'B', 'C'])
            quantity = random.randint(1, 10)
            
            # Transform
            price = product_prices[product_id]
            total = price * quantity
            
            # Load
            record = {
                'timestamp': current_time,
                'product_id': product_id,
                'quantity': quantity,
                'price': price,
                'total': total,
                'status': 'processed'
            }
            
            current_time += timedelta(hours=1)
            yield record
            
        except Exception as e:
            yield {
                'timestamp': current_time,
                'status': 'error',
                'error_message': str(e)
            }

# Test it
pipeline = data_pipeline()
for _ in range(5):
    print(next(pipeline))