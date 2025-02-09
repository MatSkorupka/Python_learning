# Create a decorator that:
# 1. Logs when function starts and ends
# 2. Measures execution time
# 3. Alerts if execution takes more than 1 second

import time

def monitor_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Starting operation: {func.__name__}")
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Operation completed: {func.__name__}")
        print(f"Execution time: {execution_time} seconds")
        
        if execution_time > 1:
            print("ALERT: Operation took more than 1 second!")
            
        return result
    return wrapper

# Test
@monitor_execution
def process_data(size):
    time.sleep(size)  # Simulates processing
    return f"Processed {size} seconds of data"

print(process_data(0.5))  # Should be fast
print("\n")
print(process_data(2))    # Should trigger alert



