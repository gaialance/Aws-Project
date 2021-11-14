from getdbconnection import *;
def getUser(data):
    checkUsid = data.get('USID',{})
    checktoken = data.get('tokenCode',{})
    # require data found
    if(checkUsid and checktoken):
        session = verifytoken(data['tokenCode'])
        if(session != 'Token Invalid'):
            sql = '''
                SELECT iUSID,vaUSID,vausername,vaemail,vaphone,siLoginType from Contact where iUSID = %d and siAccStatus = 1
                ''' % (int(data['USID']))
            data = runSql(sql)
            return data;
        else:
            return 'Wrong TokenCode'
    else:
        return '''Data Error :%s %s''' % (
            ('USID is missing' if checkUsid == {} else ''),
            ('tokenCode is missing' if checktoken == {} else '')
        )

def getallsort(data):
    checktoken = data.get('tokenCode',{})
    if(checktoken):
        session = verifytoken(data['tokenCode'])
        if(session != 'Token Invalid'):
            sql = '''
                SELECT iUSID,vaUSID,vausername,vaemail,vaphone,
                CASE 
                    WHEN siAccStatus = 1 THEN 'Active' 
                    ELSE 'Inactive' 
                END AS Status 
                FROM Contact
                group by vausername,dtCreateOn,Status,iusid,vausid,vaemail,vaphone
                order by vausername asc
            '''
            data = runSql(sql)
            return data;
        else:
            return 'Wrong TokenCode'
    else:
        return 'Data Error : %s' % (('tokenCode is Mising' if checktoken == {} else ''))

def getalluser(data):
    checktoken = data.get('tokenCode',{})
    if(checktoken):
        session = verifytoken(data['tokenCode'])
        if(session != 'Token Invalid'):
            sql = '''
                SELECT iUSID,vaUSID,vausername,vaemail,vaphone FROM Contact where siAccStatus = 1
            '''
            data = runSql(sql)
            return data;
        else:
            return 'Wrong TokenCode'
    else:
        return 'Data Error : %s' % (('tokenCode is Mising' if checktoken == {} else ''))




