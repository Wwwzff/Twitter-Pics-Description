# MiniProject3
This branch uses mysql and mongoDB to store information everytime users run the twitter API script. Slight changes are applied to the twitter api parts.
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
```
+----+---------------------+------------+----------+-------------+
| ID | Login Date          | Twitter ID | Pictures | Descriptors |
+----+---------------------+------------+----------+-------------+
|  1 | 2018-11-24 22:22:28 | linkinpark |       21 | black       |
|  2 | 2018-11-24 22:34:26 | linkinpark |       21 | black       |
+----+---------------------+------------+----------+-------------+
```
To make DATE change automatically, we need to modify defaults of this column:
```
modify column `Login Date` datetime null default current_timestamp;
```
To reset primary key:
```
truncate table TABLENAME;
```
To activate mysql from cmd:(under bin directory)
```
mysql -u root -p
```
To choose DB:
```
use MiniProject3;
```
