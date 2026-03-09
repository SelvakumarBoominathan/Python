import pandas as pd

df = pd.read_csv("Pandas\Employee_details.csv",  index_col="Name")

# Display the first few rows of the DataFrame
print(df.iloc[1:4])

# Display the last few rows of the DataFrame
# print(df.tail())

# Display the column names of the DataFrame
# python list of column names will be printed
# print(df.columns)

# printing the "Name" column of the DataFrame without index
# print(df["Name"].to_string(index=False))

# printing the "Name" and "Salary" columns of the DataFrame without index. to see multiple columns we need to pass a list of column names to the DataFrame
# print(df[["Name", "Salary"]].to_string(index=False))

