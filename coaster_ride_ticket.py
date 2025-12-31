print("Welcome to the Roller Coaster Ride Ticketing System!")
def ticket_calculator():
    height = int(input("What is your height in cm? "))

    if height >= 120:
      print("Great!. you are eligible to ride the roller coaster.")
      age = int(input("What is your age? "))

      is_photo_needed = input("Do you want a photo taken? Y or N: ").upper()

      if age>=12 and age <=18:
        print("Your ticket price is $7.")
      elif age < 12 and age >=4:
        print("Your ticket price is $5.")
      elif age > 18:
        print("Your ticket price is $12.") 
      else:
        print("Your ticket price is $0.")

    else:
        print("Sorry, you have to be at least 120 cm to ride the roller coaster.")
        return
    
ticket_calculator()