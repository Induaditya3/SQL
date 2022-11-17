import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=con.cursor()

cursor.execute("CREATE TABLE EMPLOYEE(\
ECODE INT PRIMARY KEY NOT NULL,\
ENAME VARCHAR(50),\
ADDRESS VARCHAR(50),\
CONTACT VARCHAR(10),\
GRADE CHAR(2) DEFAULT 'A1',\
DOB DATE );")


con.commit()

con.close()
