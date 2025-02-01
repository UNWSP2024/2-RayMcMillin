# Ray McMillin
# 1/31/25
#Item Prices with sales tax
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    item1 = float(input("Enter the price of item 1: $"))
    item2 = float(input("Enter the price of item 2: $"))
    item3 = float(input("Enter the price of item 3: $"))
    item4 = float(input("Enter the price of item 4: $"))
    item5 = float(input("Enter the price of item 5: $"))
    # then displays the subtotal of the sale, 
    subtotal = item1 + item2 + item3 + item4 + item5
    # the amount of sales tax, and the total.  
    sales_tax = subtotal * 0.07
    total = subtotal + sales_tax
    print("\nSubtotal: ${:.2f}".format(subtotal))
    print("Sales Tax: ${:.2f}".format(sales_tax))
    print("Total: ${:.2f}".format(total))
    # Assume the sales tax is 7 percent.

calculate_total_purchase()
