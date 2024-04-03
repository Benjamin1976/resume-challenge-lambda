import boto3

def lambda_handler(event, context):
    visits = read_counter()
    print("1.0 visits from read: ", visits)
    visits += 1
    print("2.0 visits to update: ", visits)
    update_counter(visits)
    visits = read_counter()
    print("3.0 new read of visits from function: ", visits)
    return visits


def read_counter():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('resume-blp')    

    response = table.get_item(Key={'id': 0})
    item = response['Item']
    print("visit from db: ", item['visits'])
    return item['visits']


def update_counter(visits):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('resume-blp')    

    print("2.1 visit from db: ", visits)
    table.update_item(
        Key={'id': 0},
        UpdateExpression='SET visits = :newcounter',
        ExpressionAttributeValues={
            ':newcounter': visits
        }
    )
    print("2.2 new visit count: ", visits)



