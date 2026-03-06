import pandas as pd

# CSV from GitHub
data_github = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

# Google Sheets (convert to CSV export)
sheet_id = "1mHIWnDdW9cALRz3pPTe2XFaYmvNwkBgDC_d0HEpx16k"
data_sheet = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# Excel from URL
data_excel = pd.read_excel("https://example.com/file.xlsx")

# JSON from URL
data_json = pd.read_json("https://jsonplaceholder.typicode.com/posts")

# API endpoint
data_api = pd.read_json("https://api.github.com/users/github")

# CSV with parameters
data = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv",
    usecols=['Name', 'Age', 'Survived'],
    nrows=10
)
