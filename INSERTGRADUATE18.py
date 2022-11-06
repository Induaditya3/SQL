import csv
import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()
with open("GRADUATE18.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        SNO,NAME,STIPEND,SUBJECT,AVERAGE,RANK=row
        
        query="INSERT INTO GRADUATE18 (SNO,NAME,STIPEND,SUBJECT,AVERAGE,RANK) VALUES({},'{}',{},'{}',{},{});".format(int(SNO),NAME,int(STIPEND),SUBJECT,int(AVERAGE),int(RANK))
        cursor.execute(query)
        con.commit()                                                                                                        
con.close()
