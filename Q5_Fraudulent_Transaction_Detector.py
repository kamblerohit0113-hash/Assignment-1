# Q5: Transactions above Rs. 1,00,000 are suspicious.

suspicious_count = 0
suspicious_total = 0.0

for transaction_number in range(1, 9):
    amount = float(input("Enter transaction amount " + str(transaction_number) + ": "))

    if amount < 0:
        print("Invalid transaction amount.")
    elif amount > 100000:
        print("Suspicious transaction")
        suspicious_count = suspicious_count + 1
        suspicious_total = suspicious_total + amount
    else:
        print("Normal transaction")

print("Number of suspicious transactions:", suspicious_count)
print("Total value of suspicious transactions: Rs.", suspicious_total)
