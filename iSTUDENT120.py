import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=con.cursor()

cursor.execute("CREATE TABLE STUDENT120(\
NO SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
NAME VARCHAR(15),\
STIPEND DECIMAL(5,2),\
STREAM VARCHAR(15),\
AVGMARK DECIMAL(3,1),\
GRADE CHAR(1),\
CLASS CHAR(3));")

con.commit()

con.close()
