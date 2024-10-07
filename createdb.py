import mysql.connector
con=mysql.connector.connect(username="root",password='',host="localhost",database="student")
cursor=con.cursor()
sql=""" update demo
set std = '11'
where name="paul" """
try:
    cursor.execute(sql)
    cursor.commit()
except:
    print("error")
    cursor.close()
