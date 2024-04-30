import mysql.connector
import tkinter as tkk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor=mydb.cursor()


def register():
  try:
    
    
    query="INSERT INTO `user_account`(`username`,`email`,`password`) VALUES (%s,%s,%s)"
    mycursor.execute(query,(username.get(),email.get(),password.get()))
    mydb.commit()
  except Exception as e:
    print(e)


root=tkk.Tk()
root.title("register page")
root.config(width=500, height=500)

tkk.Label(root,text="Username").pack()
username=tkk.Entry(root)
username.pack()

tkk.Label(root,text="Email").pack()
email=tkk.Entry(root)
email.pack()

tkk.Label(root,text="password").pack()
password=tkk.Entry(root)
password.pack()

submit_button=tkk.Button(root,text="Submit",command=register)
submit_button.pack()

root.mainloop()
