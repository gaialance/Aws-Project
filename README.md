# Aws-Project
This is a web APIs demo to retrieve Contact Info based on specific category This project will be done via RESTFULL API format in JSON with AWS lambda API. Coding Language used will be in python for easier understanding

# Note
This project is used Python for development purpose there will be a slight different in coding the index.py will be move to lambda and change to lamda_function.py<br />
`Note that i read Stuff from Json that are taken when lambda functions return event`<br />
For easier Debugging i use python and run on VS code studio for error logging as well as reading where is the error


# Aws-Services Used
1. Lambda
2. RDS



## Main Details:
1. vaUserID(User login Display Name)
2. vaPhone (phone number)
3. vaEmail Address 

## Additional info:
1. IUSID (index running no for user)
2. vaUserID
3. vaHashPassword1
4. vaHashPassword2
5. vaSalt (used to store the salt used for login purspose)
6. siLoginType (1 admin , 2 normal user)
7. siAccStatus (1 active , 0 inactive)
8. silock (after number of attemp lock user)
9. iAttempts (number of attemp used to login)
10. dtCreateOn (Date of creation)
11. vaCurrentToken (current token value)
12. dtValidToken (Token validation date)
13. dtModifyOn (Date of modification)
14. vaModBy (modify by who)

## Basic Features include : 
1. /getOTP (Get Method) get a token based on the user name password 
2. /getContact (Get Method) which can get all user that is currently active
3. /getContactUSERID (Get Method) with url iUSID = 1 which get a user based on the usID
4. /updateUser which update user info and deletion will be peform here also
5. VerifyToken get the token and return the valid session details

## Api Calls
## Flows
`Always get OTP first then pass the token code return to the other functions`

## Error Handling
***Message will have Failure if failed to perform an action***<br />
Respone
```
{"Message": "Failure", "ExtMesg": "User Doesnt Exists", "Transaction time": "2021-11-14-14:04:33"}
```

## [/getOTP] (https://abiyok5ae1.execute-api.ap-southeast-1.amazonaws.com/Uat/getOTP) :
Request
```
{
    "creditials":{
        "userID":"Admin1",
        "password":"test123"
    }
}
```
Respone
```
{
    "tokenCode": "0189f9b5-a831-487b-834b-232f65acad49",
    "Message": "Success",
    "Transaction time": "2021-11-14-17:53:48"
}
```

## [/getContact] (https://abiyok5ae1.execute-api.ap-southeast-1.amazonaws.com/Uat/getContact?tokenCode=`tokenCode`)
    

## [/getContactUSERID] (https://abiyok5ae1.execute-api.ap-southeast-1.amazonaws.com/Uat/getContactUSERID?tokenCode=`tokenCode` &USID=8)
Respone
```
{
    "record": 1,
    "data": [
        {
            "iUSID": 8,
            "vaUSID": "User 1",
            "vausername": "Test User 1",
            "vaemail": "huiyilim32@gmail.com",
            "vaphone": "0149290547",
            "siLoginType": "2"
        }
    ],
    "Message": "Succcess",
    "Transaction time": "2021-11-14-13:34:51"
}
```
## [/updateUser] (https://abiyok5ae1.execute-api.ap-southeast-1.amazonaws.com/Uat/updateUser)
request
```
{
    "data":{
        "tokenCode":"996309de-192f-4f7e-8551-44bf601cd090",
        "iUSID":2,
        "userID":"User 1",
        "Username":"Test User 1",
        "Password":"normal123",
        "email":"huiyilim32@gmail.com",
        "phone":"0149290547",
        "siLoginType":1,
        "siAccStatus":1
        }
}
```
respone
```
{
    "Message": "Success",
    "ExtMesg": "Update Successful",
    "Transaction time": "2021-11-14-13:39:52"
}
```
