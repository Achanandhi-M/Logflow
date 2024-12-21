import boto3

def lambda_handler(event, context):
    athena_client = boto3.client('athena')
    
    # Extract partition info from S3 event
    for record in event['Records']:
        s3_key = record['s3']['object']['key']
        bucket_name = record['s3']['bucket']['name']
        
        # Example: Extract year, month, day from S3 path
        key_parts = s3_key.split('/')
        year = key_parts[-4].split('=')[1]
        month = key_parts[-3].split('=')[1]
        day = key_parts[-2].split('=')[1]
        
        # Athena SQL query to add partition
        sql_query = f"""
        ALTER TABLE logs ADD PARTITION (
            year='{year}', month='{month}', day='{day}'
        ) LOCATION 's3://{bucket_name}/{"/".join(key_parts[:-1])}/';
        """
        
        # Execute the query in Athena
        response = athena_client.start_query_execution(
            QueryString=sql_query,
            QueryExecutionContext={
                'Database': ''  # Replace with your Athena DB
            },
            ResultConfiguration={
                'OutputLocation': f's3://{bucket_name}/query-results/'  # Replace with your bucket
            }
        )
        print(f"Partition added: {response}")
