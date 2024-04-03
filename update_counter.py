import boto3

def update_counter(counter):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('resume-blp')    

    counter += 1
    table.update_item(
        Key={'id': 0},
        UpdateExpression='SET visits = :newcounter',
        ExpressionAttributeValues={
            ':newcounter': counter
        }
    )
