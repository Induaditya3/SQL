import csv
import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()
with open("STUDENT120.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        NAME,STIPEND,STREAM,AVGMARK,GRADE,CLASS=row
        
        query="INSERT INTO STUDENT120 (NAME,STIPEND,STREAM,AVGMARK,GRADE,CLASS) VALUES('{}',{},'{}',{},'{}','{}');".format(NAME,float(STIPEND),STREAM,\
                                                                                                                           float(AVGMARK),GRADE,CLASS)
        cursor.execute(query)
        con.commit()                                                                                                        
con.close()
