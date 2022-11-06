#%(int(input("no")),input("name"),input("gender"))
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=mycon.cursor()
x=(input("no"))
y=input("name")
z=input("gender")

query="insert into test (NO,NAME,GENDER) values({},'{}','{}')".format(x,y,z)

cursor.execute(query)
mycon.commit()
mycon.close()
