# Advanced Conditions - Part 2

product_name = "Gaming Laptop"
base_price = 1500
storage = "1TB"
ram = "16GB"
gpu = "High-end"
bundle_items = ["Mouse", "Headset"]
shipping_country = "Germany"
payment_method = "Credit"

# Exercise 1: Product Package Pricing
# Calculate final price based on:
# - Base price
# - Storage upgrade: 1TB +200, 2TB +400
# - RAM upgrade: 16GB +100, 32GB +300
# - GPU tier: High-end +500, Medium +200
# - Bundle discount: 2 items -10%, 3+ items -15%
# Print final configuration price

storage_1TB = 200
storage_2TB = 400

ram_16GB = 100
ram_32GB = 300

GPU_high_end = 500
GPU_medium = 200

bundle_items_2 = 0.90
bundle_items_3 = 0.85

final_price = base_price

if storage == '1TB':
    final_price += storage_1TB 
elif storage == '2TB':
    final_price += storage_2TB

if ram == '16GB':
    final_price += ram_16GB
elif ram == '32GB':
    final_price += ram_32GB

if gpu == 'High-end':
    final_price += GPU_high_end
elif gpu == 'Medium':
    final_price += GPU_medium

if len(bundle_items) == 2:
    final_price *= bundle_items_2
elif len(bundle_items) >= 3:
    final_price *= bundle_items_3

print(final_price)



# Exercise 2: Shipping Eligibility
# Determine shipping method available:
# - "Premium": High-end GPU + price > 2000 + credit payment
# - "Express": Any GPU upgrade + price > 1500 OR bundle 3+ items
# - "Standard": All other paid orders
# - "Not Available": Certain countries
# Print available shipping method

RESTRICTED_COUNTRIES = []

if gpu == "High-end" and price > 2000 and payment_method == 'Credit':
    print('Premium')
elif (gpu in ["High-end", "Medium"] and price > 1500) or len(bundle_items) >= 3:
    print('Express')
elif price > 0 and shipping_country not in RESTRICTED_COUNTRIES:
    print('Standard')
elif shipping_country in RESTRICTED_COUNTRIES:
    print('Not Available')




# Exercise 3: Configure Bundle Offer
# Create appropriate bundle offer:
# - If high-end GPU: Offer premium bundle (software + warranty)
# - If medium GPU + 32GB RAM: Offer gaming bundle (games + accessories)
# - If 1TB+ storage: Offer backup bundle (external drive + cloud storage)
# - If none above: Offer basic bundle (basic accessories)
# Print recommended bundle

PREMIUM_BUNDLE = 'software + warranty'
GAMING_BUNDLE = 'games + accessories'
BACKUP_BUNDLE = 'external drive + cloud storage'
BASIC_BUNDLE = 'basic accessories'


if gpu == 'High-end':
    print(PREMIUM_BUNDLE)
elif gpu == 'Medium' and ram == '32GB':
    print(GAMING_BUNDLE)
elif storage == "1TB" or storage == "2TB":
    print(BACKUP_BUNDLE)
else:
    print(BASIC_BUNDLE)