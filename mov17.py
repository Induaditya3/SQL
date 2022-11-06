import csv
import mysql.connector as sql

con=sql.connect(host="localhost",user="root",passwd="",database="ADI")

cursor=con.cursor()
with open("MOV17.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        NO,TITLE,TYPE,RATING,STARS,QTY,PRICE=row
        
        query="INSERT INTO MOV17 (NO,TITLE,TYPE,RATING,STARS,QTY,PRICE) VALUES({},'{}','{}','{}','{}',{},{});".format(int(NO),TITLE,TYPE,str(RATING),STARS,int(QTY),float(PRICE))
        cursor.execute(query)
        con.commit()                                                                                                        
con.close()
