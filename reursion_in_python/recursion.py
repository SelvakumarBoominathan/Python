
# Recursion: A function that calls itself to solve a smaller instance of the same problem.
def fibonacci(n):
  if n<=1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
print(fibonacci(6))

