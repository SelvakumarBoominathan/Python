import csv

with open("sample_employee_data.csv") as file:
  data = csv.reader(file)
  experience = []
  for row in data:
    experience.append(row[4])
  print(experience)