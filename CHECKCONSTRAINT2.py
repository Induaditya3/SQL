import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=con.cursor()

cursor.execute("CREATE TABLE EMPLOYEE3(\
ECODE INT PRIMARY KEY NOT NULL,\
ENAME VARCHAR(50),\
ADDRESS VARCHAR(50),\
CONTACT VARCHAR(10),\
SALARY DECIMAL(8,2) CHECK(SALARY>50000),\
DOB DATE,\
DOJ DATE CHECK(DOJ>DOB) );")


con.commit()

con.close()
