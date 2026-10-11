# Q10: Monthly Sales Analysis for 12 months.

total_sales = 0.0
highest_sales = 0.0
lowest_sales = 0.0
high_sales_months = 0

for month in range(1, 13):
    sales = float(input("Enter sales for month " + str(month) + ": "))

    if sales < 0:
        print("Sales cannot be negative. Please run the program again with valid data.")
        break

    total_sales = total_sales + sales

    if month == 1:
        highest_sales = sales
        lowest_sales = sales
    else:
        if sales > highest_sales:
            highest_sales = sales
        if sales < lowest_sales:
            lowest_sales = sales

    if sales > 100000:
        high_sales_months = high_sales_months + 1

if month == 12 and sales >= 0:
    average_sales = total_sales / 12
    high_sales_percentage = (high_sales_months / 12) * 100

    print("Total annual sales: Rs.", round(total_sales, 2))
    print("Average monthly sales: Rs.", round(average_sales, 2))
    print("Highest monthly sales: Rs.", round(highest_sales, 2))
    print("Lowest monthly sales: Rs.", round(lowest_sales, 2))
    print("Months with sales above Rs. 1,00,000:", high_sales_months)
    print("Percentage of high-sales months:", round(high_sales_percentage, 2), "%")
