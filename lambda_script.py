import boto3 
import json

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Define S3 bucket and file key
    bucket_name = 'sentiment-analysis90124'
    file_key = 'sentiment.txt'

    # Retrieve the text file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    text = response['Body'].read().decode('utf-8')

    # Initialize Comprehend client
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    # Detect sentiment of the text
    comprehend_json_obj = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    
    # Convert the result to JSON format
    json_text = json.dumps(comprehend_json_obj, indent=4) 
    print("json_text:", json_text)
    
    # Extract the sentiment
    sentiment = comprehend_json_obj['Sentiment']
    
    # Return the sentiment
    return f"Sentiment: {sentiment}"
