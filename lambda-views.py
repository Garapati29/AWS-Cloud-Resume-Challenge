# Importing necessary libraries
import json
import boto3
# Initializing the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Getting the DynamoDB table named 'cloud-resume-challenge'
table = dynamodb.Table('cloud-resume-challenge')
def lambda_handler(event, context):
  # Retrieving an item from the DynamoDB table based on the provided Key
    response = table.get_item(Key={
        'id':'1'
    })
  # Extracting the 'views' attribute from the retrieved item
    views = response['Item']['views']
    views = views + 1
   # Printing the updated value of 'views'
    print(views)
  # Updating the item in the DynamoDB table with the incremented 'views'
    response = table.put_item(Item={
            'id':'1',
            'views': views
    })
  # Returning the updated value of 'views'
    return views
