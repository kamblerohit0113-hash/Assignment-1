# Q9: Generate two number patterns for n = 5.

print("Pattern 1:")
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end="")
    print()

print("Pattern 2:")
for row in range(1, 6):
    for number in range(1, row + 1):
        print(row, end="")
    print()
