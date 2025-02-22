import time
from contextlib import contextmanager

conversion_count = 0
previous_temp = None

@contextmanager
def temperature_converter():
    global conversion_count, previous_temp
    try:
        # Setup
        print("Starting temperature conversion...")
        start_time = time.time()

        yield  # Code block executes here
        
        # Cleanup
        end_time = time.time()
        
        # Update count and check temperature change
        conversion_count += 1
        
        if previous_temp is not None:
            if fahrenheit > previous_temp:
                change = "increased"
            elif fahrenheit < previous_temp:
                change = "decreased"
            else:
                change = "stayed the same"
            print(f"Temperature {change} from previous conversion")
        
        print(f"Conversion completed in {end_time - start_time:.2f} seconds!")
        print(f"That was conversion number {conversion_count}")
        
        previous_temp = fahrenheit

    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        raise

# Test with multiple conversions
with temperature_converter():
    celsius = 100
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

with temperature_converter():
    celsius = 50
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")