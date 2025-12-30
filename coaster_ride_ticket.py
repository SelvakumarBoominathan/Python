print("Welcome to the Roller Coaster Ride Ticketing System!")
def ticket_calculator():
    height = int(input("What is your height in cm? "))

    if height >= 120:
      print("Great!. you are eligible to ride the roller coaster.")
    else:
        print("Sorry, you have to be at least 120 cm to ride the roller coaster.")
        return
    
ticket_calculator()