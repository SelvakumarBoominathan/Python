import pandas as pd
import requests
from io import StringIO

# SharePoint URL
sharepoint_url = "https://yourcompany.sharepoint.com/sites/yoursite/Shared%20Documents/file.csv"

# Method 1: Direct URL (if public)
data = pd.read_csv(sharepoint_url)

# Method 2: With authentication
def read_sharepoint(url, username, password):
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))

# Usage
# data = read_sharepoint(sharepoint_url, "user@company.com", "password")
