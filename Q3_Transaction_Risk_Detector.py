# Q3: Customer Transaction Risk Detector
# Rules: up to Rs. 10,000 = Low; up to Rs. 50,000 = Medium; above = High.

low_count = 0
medium_count = 0
high_count = 0

for transaction_number in range(1, 11):
    amount = float(input("Enter transaction amount " + str(transaction_number) + ": "))

    if amount < 0:
        print("Invalid transaction amount.")
    elif amount <= 10000:
        print("Low Risk")
        low_count = low_count + 1
    elif amount <= 50000:
        print("Medium Risk")
        medium_count = medium_count + 1
    else:
        print("High Risk")
        high_count = high_count + 1

print("Low-risk transactions:", low_count)
print("Medium-risk transactions:", medium_count)
print("High-risk transactions:", high_count)
