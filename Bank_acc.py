import sys
if len(sys.argv) != 3:
    print("Usage: python bank_balance.py <initial_balance> <deposit_amount>")
    sys.exit(1)
initial_balance = float(sys.argv[1])
deposit_amount = float(sys.argv[2])
updated_balance = initial_balance + deposit_amount
print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
print("Updated Balance:", updated_balance)
