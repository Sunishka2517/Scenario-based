import csv

filename = "mobiles.csv"

# Read mobile details
with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    mobiles = list(reader)

# Display all mobile records
print("Mobile Records:")
for mobile in mobiles:
    print(mobile)

# Search by Brand Name
brand = input("\nEnter Brand Name to search: ")

found = False

for mobile in mobiles:
    if mobile["Brand"].lower() == brand.lower():
        print("\nMobile Found:")
        print(mobile)
        found = True

if not found:
    print("Mobile not found.")