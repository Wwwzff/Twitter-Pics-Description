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

def mostFrequent():
	db = pymysql.connect("localhost","root","123456","MiniProject3",3306)
	cursor = db.cursor()
	sql = "select `Descriptors`,count(*)a from userinfo group by `Descriptors` having count(`Descriptors`) order by a desc"
	cursor.execute(sql)
	result = cursor.fetchall()
	db.close()
	return result[0][0],'times:'+str(result[0][1])

searchbykewords('linkinpark')
picsperfeed()
print(mostFrequent())