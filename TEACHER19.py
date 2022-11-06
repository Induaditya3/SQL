import csv
import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()
with open("TEACHER19.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        NAME,AGE,DEPARTMENT,DATEOFJOIN,SALARY,SEX=row
        
        query="INSERT INTO TEACHER19 (NAME,AGE,DEPARTMENT,DATEOFJOIN,SALARY,SEX) VALUES('{}',{},'{}','{}',{},'{}');".format(NAME,int(AGE),DEPARTMENT,DATEOFJOIN,int(SALARY),SEX)
        cursor.execute(query)
        con.commit()                                                                                                        
con.close()
