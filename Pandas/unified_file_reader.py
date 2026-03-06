import pandas as pd
from pathlib import Path

def read_data(file_path, **kwargs):
    """
    Unified function to read data from multiple sources
    
    Supports:
    - Local files: "data/file.csv", "../downloads/file.json"
    - URLs: "https://example.com/file.csv"
    - GitHub: "https://raw.githubusercontent.com/..."
    - Cloud storage: "s3://bucket/file.csv", "gs://bucket/file.csv"
    """
    try:
        file_ext = Path(file_path).suffix.lower()
        
        # Remote files (URLs, cloud storage)
        if file_path.startswith(('http://', 'https://', 's3://', 'gs://', 'abfs')):
            if file_ext in ['.csv', '.txt']:
                return pd.read_csv(file_path, **kwargs)
            elif file_ext == '.json':
                return pd.read_json(file_path, **kwargs)
            elif file_ext in ['.xlsx', '.xls']:
                return pd.read_excel(file_path, **kwargs)
            elif file_ext == '.parquet':
                return pd.read_parquet(file_path, **kwargs)
            else:
                return pd.read_csv(file_path, **kwargs)
        
        # Local files
        else:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            if file_ext in ['.csv', '.txt']:
                return pd.read_csv(file_path, **kwargs)
            elif file_ext == '.json':
                return pd.read_json(file_path, **kwargs)
            elif file_ext in ['.xlsx', '.xls']:
                return pd.read_excel(file_path, **kwargs)
            elif file_ext == '.parquet':
                return pd.read_parquet(file_path, **kwargs)
            else:
                return pd.read_csv(file_path, **kwargs)
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# Usage examples
if __name__ == "__main__":
    # Local file
    df = read_data("Employee_details.csv")
    
    # File from different directory
    df = read_data("../file_reader/main.py")
    
    # From GitHub
    df = read_data("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
    
    # From API
    df = read_data("https://jsonplaceholder.typicode.com/posts")
    
    # With parameters
    df = read_data("file.csv", usecols=['Name', 'Age'], nrows=10)
    
    # Cloud storage
    # df = read_data("s3://bucket/file.csv")
    # df = read_data("gs://bucket/file.parquet")
