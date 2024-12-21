# LogFlow

**LogFlow** is an automated log management pipeline that transforms logs in Excel format into Parquet, uploads them to an S3 bucket, triggers AWS Lambda to run a Glue Crawler for metadata extraction, and makes the data searchable using Athena. The entire process is automated using AWS CloudFormation.

---

## Features

- **Excel to Parquet Conversion:** Converts Excel logs into Parquet format for efficient storage and querying.
- **Automated AWS Workflow:** Seamlessly integrates S3, Lambda, Glue Crawler, and Athena for end-to-end log management.
- **Serverless Architecture:** Utilizes AWS services to provide a highly scalable and cost-effective solution.
- **Searchable Logs:** Enables advanced log analysis using Amazon Athena.

---

## Architecture

1. **Excel Logs**: Input logs in `.xlsx` format.
2. **Parquet Conversion**: Transforms logs into `.parquet` format.
3. **S3 Bucket**: Stores the Parquet files.
4. **AWS Lambda**: Triggers Glue Crawler when new data is uploaded.
5. **AWS Glue Crawler**: Extracts metadata and updates the Glue Data Catalog.
6. **Amazon Athena**: Queries and searches the processed log data.

---

## Prerequisites

- AWS Account
- AWS CLI
- Python 3.x
- CloudFormation templates (included in the repository)
- IAM roles with required permissions

---

## Setup and Usage

### Step 1: Clone the Repository
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/Achanandhi-M/Logflow.git
cd Logflow
```

### Step 2: Deploy CloudFormation Stacks
Deploy the CloudFormation stacks to set up all required AWS resources:

1. Deploy the S3 bucket stack:
    ```bash
    aws cloudformation deploy --template-file CloudFormation/Create_S3_Bucket.yaml --stack-name LogFlowS3Stack
    ```

2. Deploy the Glue and Lambda stack:
    ```bash
    aws cloudformation deploy --template-file CloudFormation/Create_Glue_Lambda.yaml --stack-name LogFlowGlueLambdaStack
    ```

### Step 3: Convert and Upload Logs
Convert your Excel log file to Parquet and upload it to the S3 bucket:
```bash
python scripts/convert_excel_to_parquet.py 
```

### Step 4: Query Logs with Athena
1. Open the Amazon Athena console.
2. Select the database created by the Glue Crawler.
3. Start querying your log data using SQL.

---

## Directory Structure
```plaintext
logManagement/
│
├── CloudFormation/                        # Directory for CloudFormation templates
│   ├── Create_Glue_Lambda.yaml            # Template for creating Glue and Lambda resources
│   ├── Create_S3_Bucket.yaml              # Template for creating S3 bucket
│
├── lambda/                                # Directory for Lambda function code
│   └── trigger_glue_crawler.py            # Lambda function to trigger Glue Crawler
│
├── scripts/                               # Directory for helper scripts
│   └── convert_excel_to_parquet.py        # Script to convert Excel to Parquet and upload to S3
│
├── README.md                              # Project documentation
```

## Author

Developed by Your Achanandhi M