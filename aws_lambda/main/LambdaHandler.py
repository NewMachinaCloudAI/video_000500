import json

HTTP_GET_METHOD = 'GET'
HTTP_POST_METHOD = 'POST'

def handle_get_request(event):
    print("Handle_get_request Processing")
    print("Get UserKey->" + event['queryStringParameters']['userKey'] )
    return True
    
def handle_post_request(event):
    print("Handle_post_request Processing")
    jsonBody = json.loads(event['body'])
    print("Post UserKey->" + str(jsonBody['userKey']) )
    print("Post ChatQuestion->" + str(jsonBody['chatQuestion']) )
    return True

def lambda_handler(event, context):
    print("API Gateway Invoked")
    print( event )
    
    method = event['httpMethod']
    
    if method == HTTP_GET_METHOD:
        handle_get_request(event)
        
    elif method == HTTP_POST_METHOD:
        handle_post_request(event)
        
    else:
        print( "Unspported Method->" + method )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
