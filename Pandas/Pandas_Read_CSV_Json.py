import pandas as pd

my_file = pd.read_json("Pandas\Employee_details2.json", orient="records")

print(my_file)
