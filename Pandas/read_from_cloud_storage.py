import pandas as pd

# AWS S3 (requires: pip install s3fs boto3)
# data = pd.read_csv("s3://bucket-name/path/file.csv")
# connection setup: AWS credentials in ~/.aws/credentials

# Google Cloud Storage (requires: pip install gcsfs)
# data = pd.read_csv("gs://bucket-name/path/file.csv")
# connection setup: GOOGLE_APPLICATION_CREDENTIALS environment variable

# Azure Blob Storage (requires: pip install adlfs)
# data = pd.read_csv("abfs://container@account.dfs.core.windows.net/path/file.csv")

# Unified reader for cloud storage
def read_cloud(path, file_type='csv', **kwargs):
    """Read from cloud storage (S3, GCS, Azure)"""
    if file_type == 'csv':
        return pd.read_csv(path, **kwargs)
    elif file_type == 'json':
        return pd.read_json(path, **kwargs)
    elif file_type == 'parquet':
        return pd.read_parquet(path, **kwargs)
    elif file_type == 'excel':
        return pd.read_excel(path, **kwargs)

# Usage examples:
# data = read_cloud("s3://bucket/file.csv")
# data = read_cloud("gs://bucket/file.parquet", file_type="parquet")
# data = read_cloud("abfs://container@account/file.json", file_type="json")
