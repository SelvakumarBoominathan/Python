print("Welcome to the Roller Coaster Ride Ticketing System!")

def ticket_calculator():
    
    try:
       height = int(input("What is your height in cm? "))
    except ValueError:
       print("Please enter a valid number for height.")
       return

  # Check height requirement
    if height <= 120:
      print("Sorry, you have to be at least 120 cm to ride the roller coaster.")
      return
    
    # If height requirement is met
    print("Great! You are eligible to ride the roller coaster.")
    
    # Calculate ticket price based on age
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Please enter a valid number for age.")
        return
    
    # Determine ticket price
    if age<12:
        bill =5
    elif age < 18:
        bill = 7
    else:
        bill = 10

    # Ask about photo option
    if input("Do you want a photo taken? Y or N: ").upper() == "Y":
        bill +=3

    # Final bill output
    print(f"Your final bill is ${bill}. Enjoy the ride!")
    
ticket_calculator()