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
To reset whole table including primary key:
```
truncate table TABLENAME;
```
To activate mysql from cmd:(under bin directory)
```
net start mysql
mysql -u root -p
```
To choose DB:
```
use DBNAME;
```
## MongoDB Structures
Commands using windows cmd are mostly same with mysql's.
```
{ "_id" : ObjectId("5bfb0e593523132d306622b5"), "Login Date" : "Sun Nov 25 16:04:25 2018", "twitter ID" : "linkinpark", "Pictures" : 20, "Descriptor" : "black" }
{ "_id" : ObjectId("5bfb26853523132014e44a09"), "Login Date" : "Sun Nov 25 17:47:33 2018", "twitter ID" : "linkinpark", "Pictures" : 21, "Descriptor" : "black" }
```
* Local time is added using python library.
## DBtests
* Calculate avg number of pictures everytime a user uses this API.
* Search by keywords for which Twitter they've specified or what descriptors they've got.
* Find which descriptor most frequently appears.
