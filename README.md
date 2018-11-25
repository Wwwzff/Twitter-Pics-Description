# MiniProject3
This branch uses mysql and mongoDB to store information everytime users run the twitter API script. 
## MySQL Database structures
The table are created using commands below:
```
create table userinfo(
    -> `ID` INT UNSIGNED AUTO_INCREMENT,
    -> `Login Date` DATE,
    -> `Twitter ID` VARCHAR(40) NOT NULL,
    -> `Pictures` INT,
    -> `Descriptprs` VARCHAR(40),
    -> PRIMARY KEY (`ID`)
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
To make DATE change automatically, we need to modify defaults of this column. Using command below:
```
modify column `Login Date` datetime null default current_timestamp;
```
