import boto3
import json

def lambda_handler(event, context):
    # Glue client
    glue_client = boto3.client('glue')
    
    # The name of your Glue Crawler
    crawler_name = 'MyLogCrawler'
    
    try:
        # Trigger the Glue Crawler
        response = glue_client.start_crawler(
            Name=crawler_name
        )
        
        # Log the response
        print(f"Glue Crawler {crawler_name} started successfully: {response}")
        return {
            'statusCode': 200,
            'body': json.dumps('Crawler triggered successfully')
        }
    except Exception as e:
        print(f"Error starting Glue Crawler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
