# import pandas as pd


# print("Pandas version:", pd.__version__)

# # Sample Series from a list
# my_list = ["10", "20", "30", "40", "50"]

# my_series = pd.Series(my_list)

# print(my_series)

import pandas as pd


my_list = [10, 20, 30, 40, 50]

index_list = ['a', 'b', 'c', 'd', 'e']

my_series = pd.Series(my_list, index=index_list)

print(my_series.loc["c"])
