# Basic class structure
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_info(self):
        return f"Product: {self.name}, Price: ${self.price}"

# Creating objects (instances) of the class
laptop = Product("Laptop", 1000)
phone = Product("Phone", 500)

# Using the class
print(laptop.get_info())
print(phone.get_info())