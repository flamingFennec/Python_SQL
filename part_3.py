import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database = 'ninja_turtles'
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO turtles (name, color, weapon, pizza, age) VALUES (%s, %s, %s, %s, %s)"

# leonardo = ("leonardo", "Blue", "Katana", True, 15)
# mycursor.execute(sqlFormula, leonardo)

turtles = [("Rapheal", "Red", "Sai", True, 15),
           ("Donatello", "Purple", "Bo", True, 15),
           ("Michelangelo", "Orange", "Nunchakus", True, 15)]

mycursor.executemany(sqlFormula, turtles)
mydb.commit()