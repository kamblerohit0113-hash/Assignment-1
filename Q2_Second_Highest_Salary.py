# Q2: Find the highest and second-highest distinct salary without sort().

salary1 = float(input("Enter salary of employee 1: "))
salary2 = float(input("Enter salary of employee 2: "))
salary3 = float(input("Enter salary of employee 3: "))
salary4 = float(input("Enter salary of employee 4: "))
salary5 = float(input("Enter salary of employee 5: "))

highest = salary1
second_highest = 0
has_second = False

if salary2 > highest:
    second_highest = highest
    has_second = True
    highest = salary2
elif salary2 < highest:
    second_highest = salary2
    has_second = True

if salary3 > highest:
    second_highest = highest
    has_second = True
    highest = salary3
elif salary3 < highest and (not has_second or salary3 > second_highest):
    second_highest = salary3
    has_second = True

if salary4 > highest:
    second_highest = highest
    has_second = True
    highest = salary4
elif salary4 < highest and (not has_second or salary4 > second_highest):
    second_highest = salary4
    has_second = True

if salary5 > highest:
    second_highest = highest
    has_second = True
    highest = salary5
elif salary5 < highest and (not has_second or salary5 > second_highest):
    second_highest = salary5
    has_second = True

print("Highest salary:", highest)
if has_second:
    print("Second-highest distinct salary:", second_highest)
else:
    print("No second-highest distinct salary exists.")
