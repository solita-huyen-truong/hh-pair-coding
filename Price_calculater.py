tax_rates = {
    "UT": 0.0685,
    "NV": 0.08,
    "TX": 0.0625,
    "AL": 0.04,
    "CA": 0.0825
    }

def calculate_tax_per_state(total_without_tax, state_code):
    
    if state_code in tax_rates.keys():
        return round(total_without_tax * tax_rates[state_code], 2)
    else:
        print("The state you entered is not supported")

def insert_state():
    state_code = ''
    while True:
        state_code = input("Please add your state for taxation purposes:")
        if state_code in tax_rates.keys():
            return state_code
        print(f"The state {state_code} is not supported, please choose again UT, NV, TX, AL, or CA!")
    
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
    
def calculate_shipping_cost(shipping_option):
    shipping_rate = {
        "posti": 6.99,
        "matkahuolto": 3.99,
        "budbee": 9.99
    }

    if shipping_option in range(1,len(shipping_rate)+1):
        return list(shipping_rate.values())[shipping_option-1]

def validate_larger_than_zero(number):
    return number > 0

def main():
    print("Hello! Welcome to the price calculator!")
    
    while True: 
        items_to_order = 0
        price_of_item = 0 

        while True:
            items_to_order= int(input("Please input how many items you would like to order:\n"))
            if validate_larger_than_zero(items_to_order):
                break
            print("The quantity should not be smaller than 0")
        
        while True:
            price_of_item= float(input("Please input the price of item:\n"))
            if validate_larger_than_zero(price_of_item):
                break
            print("The price should not be smaller than 0")
        
        total_without_tax = round(items_to_order * price_of_item, 2)
        print("Your order is ", total_without_tax, " dollars without tax")
        
        discounted_amt = calculate_discount(total_without_tax)
        
        tax_state = insert_state()
        
        tax_amount = calculate_tax_per_state(total_without_tax - discounted_amt, tax_state)
        
        total_sum = total_without_tax - discounted_amt + tax_amount

        print(f'Your order is {total_sum} including tax.')
        
        # What kind of shippement you would like to have
        # Options 1) Posti 2) Matkahuolto 3) Budbee
        #the user inputs a number?
        shipping_option = 0 

        while True:
            shipping_option = int(input("What kind of shippement you would like to have? Input number from 1 to 3\n 1.Posti \n 2.Matkahuolto \n 3.Budbee \n"))
            if shipping_option in range(1,4):
                break
            print("You choose a wrong number, please choose again!")

        shipping_rate = calculate_shipping_cost(shipping_option)
        final_price_with_shipping_fee = total_sum + shipping_rate
        #The sum of the shipment is added to the price
        happy = str(input("Are you happy with your order? Please answer Y/N in order to send the order forward \n")).upper()
        
        if happy == "Y":
            print("Thank you for your order, this is your confirmation")
            print(f"Your order (including tax {tax_amount}$, shipping cost {shipping_rate}$, and discounted amount -{discounted_amt}$) costs {final_price_with_shipping_fee}$")
            break
        
        if happy == "N":
            print("Please start all over again!")



if __name__ == '__main__':
    main()
