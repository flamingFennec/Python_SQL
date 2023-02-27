import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database = 'ninja_turtles'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM turtles")

# myresult = mycursor.fetchall()
myresult = mycursor.fetchone()

# print(myresult)

for row in myresult:
    print(row)