import pandas as pd


print("Pandas version:", pd.__version__)

# Sample Series from a list
my_list = [10, 20, 30, 40, 50, "Selva"]

my_series = pd.Series(my_list)

print(my_series)
