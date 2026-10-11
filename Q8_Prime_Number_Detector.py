# Q8: Print all prime numbers between 1 and 50.

print("Prime numbers between 1 and 50:")

for number in range(2, 51):
    divisor = 2
    is_prime = True

    while divisor < number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

    if is_prime:
        print(number, end=" ")

print()
