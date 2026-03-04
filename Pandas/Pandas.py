
import pandas as pd


my_list = [10, 20, 30, 40, 50]

index_list = ['a', 'b', 'c', 'd', 'e']

my_series = pd.Series(my_list, index=index_list)

# Assigning a new value to an element using loc label
my_series.loc["c"] = 1000

print(my_series)


# Accessing elements using index labels
print(my_series.loc["c"])

# Accessing elements using integer position
print(my_series.iloc[1])

print(my_series[my_series < 40])


# series constructor with dictonaries (key value pairs)

my_dict = {"Day1": 1065, "Day2": 12070, "Day3": 2000, "Day4": 1500}

my_calorie_tracker = pd.Series(my_dict)


print(my_calorie_tracker[my_calorie_tracker == 2000])


# Creating dataframe from a dictionary of lists

my_dict = {"Name": ["Alice", "Bob", "Charlie"],
           "Age": [25, 30, 35],
           "City": ["New York", "Los Angeles", "Chicago"]}

my_dataframe = pd.DataFrame(my_dict, index=["Person1", "Person2", "Person3"])

print(my_dataframe)
