import uuid;
import hashlib;
from getdbconnection import *;
from datetime import date;

def getUser(iusid):
    sql = '''
        SELECT iUSID,vaUSID,vausername,vaemail,vaphone,siLoginType from Contact where iUSID = %d and siAccStatus = 1
          ''' % (int(iusid))
    data = runSql(sql)
    return data;

def getallsort():
    sql = '''
        SELECT iUSID,vaUSID,vausername,vaemail,vaphone FROM Contact where siAccStatus = 1 group by vausername,dtcreateat,iusid,vausid,vaemail,vaphone order by vausername asc
    '''
    data = runSql(sql)
    return data;

def getalluser():
    sql = '''
        SELECT iUSID,vaUSID,vausername,vaemail,vaphone FROM Contact order where siAccStatus = 1
    '''
    data = runSql(sql)
    return data;




