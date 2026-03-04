
import pandas as pd


my_list = [10, 20, 30, 40, 50]

index_list = ['a', 'b', 'c', 'd', 'e']

my_series = pd.Series(my_list, index=index_list)

# Assigning a new value to an element using loc label
#my_series.loc["c"] = 1000

#print(my_series)


# Accessing elements using index labels
#print(my_series.loc["c"])

# Accessing elements using integer position
#print(my_series.iloc[1])

print(my_series[my_series >=40])




