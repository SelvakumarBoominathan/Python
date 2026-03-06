import pandas as pd
import os
from pathlib import Path

# Absolute path (Windows)
data = pd.read_csv("C:\\Users\\selva\\Downloads\\file.csv")

# Relative path (one level up)
data = pd.read_csv("../Downloads/file.csv")

# Current script's directory (recommended)
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Employee_details.csv")
data = pd.read_csv(file_path)

# Using pathlib (modern approach)
file_path = Path(__file__).parent / "Employee_details.csv"
data = pd.read_csv(file_path)

# Parent directory
parent_dir = Path(__file__).parent.parent
file_in_parent = parent_dir / "file_reader" / "main.py"
