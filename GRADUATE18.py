import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()

cursor.execute("CREATE TABLE GRADUATE18(\
SNO SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
NAME VARCHAR(10),\
STIPEND SMALLINT,\
SUBJECT VARCHAR(12),\
AVERAGE SMALLINT,\
RANK SMALLINT);")


con.close()
