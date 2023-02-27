import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database = 'ninja_turtles'
)

mycursor = mydb.cursor()

#Check to see if databases exists
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE DATABASE ninja_turtles")

# mycursor.execute("CREATE TABLE turtles (name VARCHAR(225), color VARCHAR(225), weapon VARCHAR(225), pizza BOOLEAN, age INT(3))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)