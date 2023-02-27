import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database = 'ninja_turtles'
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM turtles WHERE color = 'red'"

# sql = "SELECT * FROM turtles WHERE name LIKE 'Don%'"

sql = "SELECT * FROM turtles WHERE name LIKE '%el%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)