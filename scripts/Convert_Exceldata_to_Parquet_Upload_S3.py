import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import os
from datetime import datetime

# S3 Bucket Config
S3_BUCKET = "your_bucket_name"
S3_BASE_PATH = "your_path"
AWS_REGION = "your_region"

# Boto3 client
s3_client = boto3.client("s3", region_name=AWS_REGION)

def convert_excel_to_parquet(excel_file_path):
    # Read Excel file
    df = pd.read_excel(excel_file_path)
    
    #required columns to include
    
    required_columns = [ 'Router IP', 'Source IPv4 Address', 'Source Transport Port','Post NAT Source IPv4 Address','Post NAPT Source Transport Port','Destination IPv4 Address','Destination port','Post NAT Destination IPv4 Address','Post NAPT Destination Transport Port','Proto']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Add partition columns (date)
    today = datetime.now()
    df["year"] = today.year
    df["month"] = today.month
    df["day"] = today.day

    # Convert to PyArrow Table
    table = pa.Table.from_pandas(df)

    # Save to Parquet file
    partition_path = f"year={today.year}/month={today.month}/day={today.day}/"
    local_parquet_path = f"partitioned_data/{partition_path}data.parquet"

    os.makedirs(os.path.dirname(local_parquet_path), exist_ok=True)
    pq.write_table(table, local_parquet_path)

    return local_parquet_path, partition_path

def upload_to_s3(local_path, partition_path):
    # Upload Parquet file to S3
    s3_path = f"{S3_BASE_PATH}/{partition_path}data.parquet"
    s3_client.upload_file(local_path, S3_BUCKET, s3_path)
    print(f"Uploaded to S3: s3://{S3_BUCKET}/{s3_path}")
    return s3_path

# Main process
if __name__ == "__main__":
    excel_file = ""  # Replace with your Excel file path
    local_parquet_path, partition_path = convert_excel_to_parquet(excel_file)
    upload_to_s3(local_parquet_path, partition_path)
