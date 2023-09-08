import cs50
import csv

db=cs50.SQL("sqlite:///roster.db")

'''Creating table inside databases by reading schema.sql'''
with open("schema.sql") as file:
    sql=file.read().split(";")
    sql.pop()
    for statement in sql:
        statement=statement.strip()
        print(statement)
        creation=db.execute(statement)
        if not creation:
            exit(1)

houses=[]
heads=[]
ihead=0
ihouse=0
id=0

''' Populating database by reading data from csv file'''
with open("students.csv") as f:
    reader=csv.DictReader(f)
    for row in reader:
        id+=1
        house=row["house"]
        head=row["head"]
        sname=row["student_name"]

        if house not in houses:
            houses.append(house)
            ihouse+=1
            fill_house=db.execute("INSERT INTO houses (id,house) VALUES (?, ?)",ihouse,house)
        if head not in heads:
            heads.append(head)
            ihead+=1
            fill_head=db.execute("INSERT INTO head (id,hname) VALUES (?, ?)",ihead,head)

        headId=db.execute("SELECT id FROM head WHERE hname= ?",head)
        houseId=db.execute("SELECT id FROM houses WHERE house= ?",house)
        fill_students=db.execute("INSERT INTO students (id,sname,headId,houseId) VALUES (?, ?, ?, ?)",id,\
                                 sname,headId[0]["id"],houseId[0]["id"])


print("done")