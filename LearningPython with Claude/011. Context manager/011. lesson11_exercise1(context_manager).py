# EXERCISE: Create a Temperature Converter Context Manager
# It should:
# 1. Print "Converting temperatures..."
# 2. Allow operations to happen
# 3. Print "Conversion completed!"

from contextlib import contextmanager

@contextmanager
def temperature_converter():
    # Your code here: Print starting message
    print(f'Starting operation')
    yield  # This is where the code inside 'with' block will run
    
    # Your code here: Print completion message
    print('Operation completed')

# Test it like this:
with temperature_converter():
    celsius = 100
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

# Should output:
# Converting temperatures...
# 100°C is 212.0°F
# Conversion completed!