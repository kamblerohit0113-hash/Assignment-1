# Q6: Employee Performance Analyzer
# Categories: 85-100 Excellent; 70-<85 Good; 50-<70 Average; below 50 Poor.

highest = -1
lowest = 101

for employee_number in range(1, 7):
    score = float(input("Enter score for employee " + str(employee_number) + " (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. It will not be included in highest/lowest calculations.")
    else:
        if score >= 85:
            print("Excellent")
        elif score >= 70:
            print("Good")
        elif score >= 50:
            print("Average")
        else:
            print("Poor")

        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

if highest == -1:
    print("No valid scores were entered.")
else:
    print("Highest score:", highest)
    print("Lowest score:", lowest)
