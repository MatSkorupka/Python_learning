# 'w' - Write mode (overwrites existing file)
with open('test.txt', 'w') as file:
    file.write('Hello')  # Creates new file or overwrites existing

# 'r' - Read mode (default)
with open('test.txt', 'r') as file:
    content = file.read()  # Reads existing file

# 'a' - Append mode (adds to end of file)
with open('test.txt', 'a') as file:
    file.write(' World')  # Adds to existing content

# 'r+' - Read and Write mode
with open('test.txt', 'r+') as file:
    content = file.read()  # Can read
    file.write(' New text')  # Can also write