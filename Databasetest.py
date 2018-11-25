import pymysql

def searchbykewords(keywords):
	db = pymysql.connect("localhost","root","123456","MiniProject3",3306)   #localhost,DBusername,password,DBname,Port
	cursor = db.cursor()
	sql = "select * from userinfo where `Twitter ID` = '"+keywords+"' or `Descriptors` = '"+keywords+"';"   # e.g. select * from userinfo where `Twitter ID` = *** or `Descriptors` = *** ;
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		print(i)
	db.close()

def picsperfeed():
	db = pymysql.connect("localhost","root","123456","MiniProject3",3306)
	cursor = db.cursor()
	sql = "select avg(Pictures) from userinfo;"
	cursor.execute(sql)
	result = cursor.fetchall()
	print(result[0][0])
	db.close()

picsperfeed()
searchbykewords('linkinpark')