import pandas as pd

# ============================================
# 1. SERIES CREATION AND BASIC OPERATIONS
# ============================================

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

# Filtering series elements
print(my_series[my_series < 40])


# ============================================
# 2. SERIES FROM DICTIONARY
# ============================================

my_dict = {"Day1": 1065, "Day2": 12070, "Day3": 2000, "Day4": 1500}
my_calorie_tracker = pd.Series(my_dict)
print(my_calorie_tracker[my_calorie_tracker == 2000])


# ============================================
# 3. DATAFRAME CREATION AND MANIPULATION
# ============================================

my_dict = {"Name": ["Alice", "Bob", "Charlie"],
           "Age": [25, 30, 35],
           "City": ["New York", "Los Angeles", "Chicago"]}

my_dataframe = pd.DataFrame(my_dict, index=["Person1", "Person2", "Person3"])

# Update a row using loc
my_dataframe.loc["Person2", ["Age", "City", "Name"]] = [
    31, "Los Vegas", "Bob Smith"]
print(my_dataframe.iloc[1])

# Add a new column to the DataFrame
my_dataframe["pincode"] = [122001, 90001, 60601]

# Add a new row to the DataFrame
new_rows = pd.DataFrame(
    [{"Name": "David", "Age": 28, "City": "Houston", "pincode": 77001}, {"Name": "Dravid", "Age": 38, "City": "Kelle", "pincode": 87041}, {"Name": "Sachin", "Age": 40, "City": "Mumbai", "pincode": 10001}], index=["Person4", "Person5", "Person6"])


my_dataframe = pd.concat([my_dataframe, new_rows])
print(my_dataframe)


