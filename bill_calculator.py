print("Welcome to the Tip Calculator!")

def amount_calculator():
    bill_amount = float(input("what is the bill amount?  $"))
    tip_percentage = float(input("What percentage of tip you woule like to give ? 10, 12 or 15 ? "))
    
    #if tip_percentage!=10 and tip_percentage!=12 and tip_percentage!=15:
        #return print("Enter the correct percentage.")
    
    
    tip = bill_amount * (tip_percentage / 100)
    share_count = int(input("How many persons are going to share? "))
    amount_to_pay_each =  round((bill_amount + tip) / share_count, 2)
    print(f"Each person should pay: ${amount_to_pay_each}" )

amount_calculator()
