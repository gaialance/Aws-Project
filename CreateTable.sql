--SQL
CREATE TABLE Contact (
    iUSID int NOT NULL PRIMARY KEY,
    vaUSID varchar(255),
    vaUserName varchar(255),
    vaEmail varchar(255),
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

CREATE INDEX vaUSID_index
ON Contact (vaUSID);

INSERT INTO Contact (vaUSID,vaUserName,vaHashPassword1,vaHashPassword2,vaSalt,siLoginType,siAccStatus,silock,iAttempts,dtCreateOn)
VALUE ()