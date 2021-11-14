import json;
from userFunction import *
from getUser import *
from tokenfunc import *
from datetime import datetime, timedelta;

# Paths that are avaible in this HTTP RESTFUL API
rawPaths = ["/getOTP","/createUser","/getContact","/getContactUSERID","/updateUser"]
# JSON file
f = open ('getOTP.json', "r")
 
# Reading from file
event = json.loads(f.read())
def lambda_handler(event, context):
    # TODO implement
    now = datetime.now().strftime('%Y-%m-%d-%H:%M:%S');
    #Validate the path is in the correct paths
    # remove the root directory to only get the functions
    # replace(RemoveString,ReplaceString,occurances)
    event['rawPath'] = event['rawPath'].replace('/Uat','',1)
    if( event['rawPath'] in rawPaths):
        indexFunction = rawPaths.index(event['rawPath'])
        #/getOTP
        if(indexFunction == 0):
            data = json.loads(event['body'])['creditials']
            result = generateToken(data['userID'],data['password'])
            if(len(result) > 0):
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'tokenCode':result['token'],
                        'Message':'Success',
                        'Transaction time':result['tokenExpiry']
                    })
                }
            else:
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'tokenCode':'',
                        'Message':'Failure',
                        'ExtMSG':result,
                        'Transaction time':now
                    })
                }
            return respone;
            
        # /CreateUser
        elif(indexFunction == 1):
            result = CreateUser(json.loads(event['body'])['data']);
            if(result == 'Create Successfull'):
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'Message':'Succcess',
                        'ExtMesg':result,
                        'Transaction time':now
                    })
                }
            else:
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'record':len(result),
                        'data':result,
                        'Message':'Failure',
                        'Transaction time':now
                    })
                }
            return respone
        # getContact
        elif(indexFunction == 2):
            data = event['queryStringParameters']
            result = getallsort(data)
            if(len(result) <= 0):
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'record':len(result),
                        'data':[],
                        'Message':'Success',
                        'ExtMesg':'No Record Found',
                        'Transaction time':now
                    })
                }
            else:
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'record':len(result),
                        'data':result,
                        'Message':'Succcess',
                        'Transaction time':now
                    })
                }
            return respone
        # getContactUSERID
        elif(indexFunction == 3):
            data = event['queryStringParameters']
            result = getUser(data)
            # result = getalluser()
            if(len(result) <= 0):
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'ExtMesg':result,
                        'Message':'Succcess',
                        'Transaction time':now
                    })
                }
            else:
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'record':len(result),
                        'data':result,
                        'Message':'Succcess',
                        'Transaction time':now
                    })
                }
            return respone
        elif(indexFunction == 4):
            result = UpdateUser(json.loads(event['body'])['data']);
            if(result == 'Update Successful'):
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'Message':"Success",
                        'ExtMesg':result,
                        'Transaction time':now
                    })
                }
            else:
                respone = {
                    "statusCode":200,
                    "body": json.dumps({
                        'Message':'Failure',
                        'ExtMesg':result,
                        'Transaction time':now
                    })
                }
            return respone
        else:
            return event
        # default AWS got filter just in cases just do validation on this
    else:
        return {
            'statusCode': 400,
            'ErrorCode':'Invalid path ('+event["rawPath"]+')',
            'Transaction time':now
        }
        
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }

print(lambda_handler(event,'abc'))
