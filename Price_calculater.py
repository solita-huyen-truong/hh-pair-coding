print("Hello! Welcome to the price calculator!")

items_to_order= int(input("Please input how many items you would like to order:\n"))
price_of_item= float(input("Please input the price of item:\n"))

total_sum = round(items_to_order*price_of_item, 2)
print("Your order is ", total_sum, " dollars without tax")
