import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()
cursor.execute("CREATE TABLE MOV17(\
NO SMALLINT,\
TITLE VARCHAR(50),\
TYPE VARCHAR(15),\
RATING VARCHAR(1),\
STARS VARCHAR(15),\
QTY SMALLINT,\
PRICE DECIMAL(4,2));")

con.close()
