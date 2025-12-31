number = int(input("Enter a number: "))

def modulo_operator(num):
  if num % 2 == 0:
    print(f"{num} is an even number.")
  else:
    print(f"{num} is an odd number.")

modulo_operator(number)