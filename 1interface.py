import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=mycon.cursor()
cursor.execute("select * from test")
data=cursor.fetchall()
for row in data:
    print(row)
mycon.close()
