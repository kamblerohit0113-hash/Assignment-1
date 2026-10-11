# Q7: ATM Withdrawal Analysis
# Successful requests must be positive, multiples of Rs. 500, and <= Rs. 20,000.

successful = 0
rejected = 0

for request_number in range(1, 11):
    amount = int(input("Enter withdrawal amount for request " + str(request_number) + ": "))

    if amount <= 0:
        print("Rejected: amount must be positive.")
        rejected = rejected + 1
    elif amount % 500 != 0:
        print("Rejected: amount must be a multiple of Rs. 500.")
        rejected = rejected + 1
    elif amount > 20000:
        print("Rejected: maximum withdrawal is Rs. 20,000.")
        rejected = rejected + 1
    else:
        print("Withdrawal Successful")
        successful = successful + 1

print("Successful transactions:", successful)
print("Rejected transactions:", rejected)
