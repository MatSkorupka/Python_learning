def debug_info(prefix=""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            print(f"{prefix}Starting {func.__name__}")
            
            result = func(*args, **kwargs)
            
            end = time.time()
            print(f"{prefix}Finished in {end-start:.2f}s")
            
            return result
        return wrapper
    return decorator

@debug_info(prefix="DEBUG: ")
def process_data(size):
    time.sleep(size)
    return f"Processed {size}s of data"

# Test it
print(process_data(2.55))