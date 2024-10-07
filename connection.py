import mysql.connector
db=mysql.connector.connect(user='root',password='',host='localhost',database='project')
cursor=db.cursor()
sql="""(create table libray(Book_name varchar(50), bookpirce int(10), Authorname varchar(50),publication varchar(50))"""
if cursor.execute(sql):
    print("The table is created")
    db.commit()
else:
    
    db.close()
        