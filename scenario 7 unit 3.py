import csv
import re

filename = "customers.csv"

# Read customer records
with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

# Display all customer details
print("Customer Records:")

for customer in customers:
    print(customer)

# Search using Account Number
account = input("\nEnter Account Number to search: ")

found = False

for customer in customers:
    if customer["AccountNumber"] == account:
        print("\nCustomer Found:")
        print(customer)
        found = True

if not found:
    print("Customer not found.")

# Validate account number using Regular Expression
pattern = r"^[0-9]{10}$"

if re.match(pattern, account):
    print("Valid Account Number")
else:
    print("Invalid Account Number")