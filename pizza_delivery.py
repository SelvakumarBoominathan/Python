print("Welcome to pizza delivery app!")

pizza_prizes = {"S": 15, "M": 20, "L": 25}


while True:
    size = input("What size pizza do you want? S, M, or L ").upper()
    if size in pizza_prizes:
        price = pizza_prizes[size]
        break
    else:
      print("Invalid input. Please enter S, M, or L.")


def pepperoni(size, price): 
  if size == "S":
    return price+2
  else:
    return price+3
  
def extra_cheese(price):
   return price+1



if input("Do you want pepperoni? Y or N ").upper() == "Y":
  price = pepperoni(size, price)


if input("Do you want extra cheese? Y or N ").upper() == "Y":
   price = extra_cheese(price)

print(f"Your final bill is : ${price}.")



