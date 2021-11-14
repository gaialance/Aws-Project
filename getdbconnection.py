import pymysql;
import hashlib;

hostname = 'dbcontact.cy9adsgfk3k0.ap-southeast-1.rds.amazonaws.com'
name = 'admin'
password = 'password'
db_name = 'dbcontact'

def initializeDB():
    #table name
    try:
        db = pymysql.connect(host=hostname,user=name,password=password,port=3306,cursorclass=pymysql.cursors.DictCursor)
        db.cursor().execute('use dev')
        db.cursor().connection.commit()
        return db
    except Exception as e:
        return e
    

    # Get the service resource.
def verifytoken(token):
    try:
        db = initializeDB();
        cursor = db.cursor();
        cursor.execute('''
            SELECT iUSID,vaUSID,dtValidToken,siLoginType FROM Contact where vaCurrentToken = '%s'
            ''' %(str(token))) ;
        data = cursor.fetchall();
        if(len(data)> 0):
            return data
        else:
            return 'Token Invalid'
    except Exception as e:
        return str(e)
    finally:
        db.close();

def runSql(sqlstatement):
    try:
        db = initializeDB();
        cursor = db.cursor();
        cursor.execute(sqlstatement)
        data = cursor.fetchall();
        cursor.connection.commit()
        return data
    except Exception as e:
        return str(e)
    finally:
        db.close();

def hashingPassword(userName,password):
    # encode default will run UTF-8
    hash1 = hashlib.sha256(userName.upper().encode()).hexdigest()
    hash2 = hashlib.md5(password.lower().encode()).hexdigest()
    hash3 = hashlib.sha256((hash1 + hash2 +  'awsDB').encode()).hexdigest()

    return hash3

def salt(userName,password):
    return hashlib.sha256((userName.lower()+'saltAWS').encode()).hexdigest()    

def dropTable():
    db = initializeDB();
    cursor = db.cursor();
    sql = 'drop table Contact'
    cursor.execute(sql)
    data = cursor.fetchall();
    db.close();

def createTable():
    db = initializeDB();
    cursor = db.cursor();
    sql = '''
        CREATE TABLE Contact (
        iUSID int NOT NULL PRIMARY KEY,
        vaUSID varchar(255),
        vaUserName varchar(255),
        vaEmail varchar(255),
        vaPhone varchar(255),
        vaHashPassword1 varchar(255),
        vaHashPassword2 varchar(255),
        vaSalt varchar(255),
        siLoginType varchar(255),
        siAccStatus varchar(255),
        silock varchar(255),
        iAttempts varchar(255),
        dtCreateOn varchar(255),
        vaCurrentToken varchar(255),
        dtValidToken varchar(255),
        dtModifyOn varchar(255),
        vaModBy varchar(255)
    );
    '''
    cursor.execute(sql)
    data = cursor.fetchall();
    db.close();