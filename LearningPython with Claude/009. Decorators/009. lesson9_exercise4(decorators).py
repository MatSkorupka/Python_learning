import time

def primary_logging(priority):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start = time.time()
                print(f'{priority.upper()} - Starting {func.__name__}')
                
                result = func(*args, **kwargs)  # Execute function
                
                end = time.time()
                duration = end - start
                
                if duration > 1:
                    print(f'WARNING: Long duration - {duration:.2f} seconds')
                else:
                    print(f'Duration: {duration:.2f} seconds')
                
                return result
                
            except Exception as e:
                print(f"Error in {func.__name__}: {str(e)}")
                raise  # Re-raise the exception after logging
                
        return wrapper
    return decorator

@primary_logging("Company")
def company_task(duration):
    time.sleep(duration)
    print("Doing company work")

@primary_logging("Personal")
def regular_task(duration):
    time.sleep(duration)
    print("Doing regular work")

# Test
try:
    company_task(2)  # Should show warning for long duration
    regular_task(0.5)  # Should be normal
    regular_task("invalid")  # Should show error
except:
    pass