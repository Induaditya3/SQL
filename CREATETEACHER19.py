import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")
cursor=con.cursor()

cursor.execute("CREATE TABLE TEACHER19(\
NO SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
NAME VARCHAR(15),\
AGE SMALLINT,\
DEPARTMENT VARCHAR(12),\
DATEOFJOIN DATE,\
SALARY SMALLINT,\
SEX CHAR(1));")

con.commit()

con.close()
