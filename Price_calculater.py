
def calculate_tax_per_state(total_without_tax, state_code):
    tax_rates = {
    "UT": 0.0685,
    "NV": 0.08,
    "TX": 0.0625,
    "AL": 0.04,
    "CA": 0.0825
    }
    
    if state_code in tax_rates.keys():
        return round(total_without_tax * tax_rates[state_code], 2)
    else:
        print("The state you entered is not supported")

def calculate_discount(total_sum):
    discounted_amt = 0
    if total_sum >= 50000:
        discounted_amt = total_sum * 0.15
    elif total_sum >= 10000:
        discounted_amt = total_sum * 0.1
    elif total_sum >= 7000:
        discounted_amt = total_sum * 0.07
    elif total_sum >= 5000:
        discounted_amt = total_sum * 0.05
    elif total_sum >= 1000:
        discounted_amt = total_sum *0.03
    else: 
        print("The total is too small for a discount.")
        pass 
    print("The total_sum ", total_sum, " is eligible for a ", discounted_amt, "dollar of discounted amount")
    return discounted_amt
    

def main():
    print("Hello! Welcome to the price calculator!")
    
    items_to_order= int(input("Please input how many items you would like to order:\n"))
    price_of_item= float(input("Please input the price of item:\n"))
    
    total_without_tax = round(items_to_order * price_of_item, 2)
    print("Your order is ", total_without_tax, " dollars without tax")
    
    discounted_amt = calculate_discount(total_without_tax)
    
    tax_state = input("Please add your state for taxation purposes:")
    
    tax_amount = calculate_tax_per_state(total_without_tax - discounted_amt, tax_state)
    
    total_sum = total_without_tax - discounted_amt + tax_amount

    print(f'Your order is {total_sum} including tax.')
    
    happy = str(input("Are you happy with your order? Please answer Y/N in order to send the order forward \n")).upper()
    
    if happy == "Y":
        print("Thank you for your order, this is your confirmation")
    
    if happy == "N":
        print("Please start all over again by refreshing the page!")

if __name__ == '__main__':
    main()
