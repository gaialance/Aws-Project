import uuid;
from getdbconnection import *;
from datetime import datetime;

def getIndex():
    query = '''select iUSID from Contact order by iUSID desc'''
    data = runSql(query)
    return data[0]['iUSID'];

def CreateUser(data):
    checktokenCode = data.get('tokenCode',{})
    checkuserID = data.get('userID',{})
    checkUsername = data.get('Username',{})
    checkemail = data.get('email',{})
    checkphone = data.get('phone',{})
    checkPassword = data.get('Password',{})
    if (checktokenCode and checkuserID and checkUsername and checkemail and checkphone and checkPassword):
        session = verifytoken(data['tokenCode'])
        if(session != 'Token Invalid'):
            # got session and token verify do create
            if(int(session[0]['siLoginType']) == 1):
                index = (getIndex()+1);
                sql = '''
                    INSERT INTO Contact (iUSID,vaUSID,vaUserName,vaemail,vaphone,vaHashPassword1,vaHashPassword2,vaSalt,siLoginType,siAccStatus,silock,iAttempts,dtCreateOn)
                    VALUE (%d,'%s','%s','%s','%s','%s','%s','%s','%d',%d,%d,%d,'%s') 
                    ''' % (index,data['userID'],data['Username'],data['email'],data['phone'],str(uuid.uuid4()),hashingPassword(data['userID'],data['Password']),salt(data['userID'],data['Password']),2,1,0,0,datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
                data = runSql(sql)
                if(len(data) == 0):
                    return "Create Successfull"
                else:
                    return "Error while Creation"+data
            else:
                return 'You have no Permission to Create'
        else:
            return session
    else:
        return 'Error Data: %s %s %s %s %s %s' % (
                ('tokenCode is Missing' if checktokenCode == {} else '')
                ,('userID is Missing' if checkuserID == {} else '')
                ,('Username is Missing' if checkUsername == {} else '')
                ,('email is Missing' if checkemail == {} else '')
                ,('phone is Missing' if checkphone == {} else '')
                ,('Password is Missing' if checkPassword == {} else '')    
        )

def UpdateUser(data):
    
    checktokenCode = data.get('tokenCode',{})
    checkuserID = data.get('userID',{})
    checkUsername = data.get('Username',{})
    checkemail = data.get('email',{})
    checkphone = data.get('phone',{})
    checksiLoginType = data.get('siLoginType',{})
    checksiAccStatus = data.get('siAccStatus',{})
    if (checktokenCode and checkuserID and checkUsername and checkemail and checkphone and checksiLoginType and checksiAccStatus):
        session = verifytoken(data['tokenCode'])
        if(session != 'Token Invalid'):
            # got session and token verify
            # get user from data
            # got session and token verify do create
            if(int(session[0]['siLoginType']) == 1):
                sql = '''
                    SELECT iUSID,vaUSID,vaUserName,email,vaPhone,siLoginType FROM Contact where iUSID = '%s' 
                    ''' % (data['iUSID'])
                result = runSql(sql)
                
                if(len(result) > 0):
                    # User Exist can perform update
                    sql = '''
                        UPDATE Contact
                        SET VaUSERNAME = '%s',
                        VaEmail = '%s',
                        vaPhone = '%s',
                        siLoginType = %d,
                        siAccStatus = %d,
                        vamodby = '%s',
                        dtModifyOn = '%s'
                        where iUSID = '%d'
                    ''' % ((data['Username'] if data['Username'] != '' else result['vaUserName'])
                    ,(data['email'] if data['email'] != '' else result['VaEmail'])
                    ,(data['phone'] if data['phone'] != '' else result['vaPhone'])
                    ,(data['siLoginType'] if data['siLoginType'] != '' else result['siLoginType'])
                    ,(data['siAccStatus'] if data['siAccStatus'] != '' else result['siAccStatus'])
                    ,session[0]['vaUSID']
                    ,datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
                    ,data['iUSID'])
                    data = runSql(sql);
                    if(data == ()):
                        return 'Update Successful'
                    else:
                        return 'Update Failed Error :'+data;
                else:
                    return 'User Doesnt Exists'
            else:
                return 'You have no Permission to Update'
        else:
            return session
    else:
        return 'Error Data: %s %s %s %s %s %s %s %s' % (
            ('tokenCode is Missing' if checktokenCode == {} else '')
            ,('userID is Missing' if checkuserID == {} else '')
            ,('Username is Missing' if checkUsername == {} else '')
            ,('email is Missing' if checkemail == {} else '')
            ,('phone is Missing' if checkphone == {} else '')
            ,('siLoginType is Missing' if checksiLoginType == {} else '')
            ,('siAccStatus is Missing' if checksiAccStatus == {} else '')
        )
        


