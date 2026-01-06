# work with normal csv library from Python standard library

import csv

with open("sample_employee_data.csv") as file:
    data = csv.reader(file)
    experience_of_employees = []

    for row in data:
        if row[4] != "Experience_Years":
            experience_of_employees.append(int(row[4]))

    print(experience_of_employees)


# import pandas as pd

# data = pd.read_csv("sample_employee_data.csv")

# print(data)
