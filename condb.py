import  cgi
import mysql.connector
import os
con=mysql.connector.connect(username="root",password='',host="localhost",database="csc_pammal")
cursor=con.cursor()
form=cgi.FieldStorage()
enrol_no=form.get("enrol_no")
std_name=form.get("std_name")
course=form.get("course")
staff_name=form.get("staff_name")
rating=form.get("rating")
more=form.get("more")
value=(enrol_no,std_name,course,staff_name,rating,more)
insert_query="insert into feedback values(%i,%s,%s,%s,%i,%ld)"
exe=cursor.execute (insert_query,value)
os.system('cls')
print(exe)
os.system('cls')
con.commit()
cursor.close()
con.close()
print("data recorded successfully")

