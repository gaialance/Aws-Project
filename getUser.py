from getdbconnection import *;
def getUser(data):
    session = verifytoken(data['tokenCode'])
    if(session != 'Token Invalid'):
        sql = '''
            SELECT iUSID,vaUSID,vausername,vaemail,vaphone,siLoginType from Contact where iUSID = %d and siAccStatus = 1
            ''' % (int(data['USID']))
        data = runSql(sql)
        return data;
    else:
        return 'Wrong TokenCode'

def getallsort(data):
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

def getalluser(data):
    session = verifytoken(data['tokenCode'])
    if(session != 'Token Invalid'):
        sql = '''
            SELECT iUSID,vaUSID,vausername,vaemail,vaphone FROM Contact where siAccStatus = 1
        '''
        data = runSql(sql)
        return data;
    else:
        return 'Wrong TokenCode'




