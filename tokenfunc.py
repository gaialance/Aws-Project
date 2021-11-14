from datetime import datetime, timedelta;
from getdbconnection import *;
import uuid;

def generateToken(username,password):
    sql = '''
          SELECT iUSID,vaUSID,vausername,vaemail,vaphone,vaCurrentToken,dtValidToken from Contact where vaUSID = '%s' and vaHashPassword2 = '%s' and siAccStatus = 1
          ''' % (username,hashingPassword(username,password))
    data = runSql(sql);
    tokenExpiry=''
    if (len(data) <= 0 ):
      return 'Invalid Username & Password';
    else:
      # create token
      tokenCode = str(uuid.uuid4())
      # make it valid for one hour
      hours_added = timedelta(hours=4)
      tokenExpiry = (datetime.now() + hours_added).strftime('%Y-%m-%d-%H:%M:%S')

      sql1 = '''
            UPDATE Contact SET vaCurrentToken = '%s',dtValidToken = '%s' where vaUSID = '%s' and vaHashPassword2 = '%s'
          ''' % (str(tokenCode),str(tokenExpiry),username,str(hashingPassword(username,password)))
      result = runSql(sql1);
      if(result == ()):
        return {'token':tokenCode,'tokenExpiry':tokenExpiry}
      else:
        return result
