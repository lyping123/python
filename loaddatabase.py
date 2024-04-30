import mysql.connector
import tkinter as tkk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor=mydb.cursor()

qry="SELECT * FROM user_account"
mycursor.execute(qry)
rows=mycursor.fetchall()

for row in rows:
    print(row)


