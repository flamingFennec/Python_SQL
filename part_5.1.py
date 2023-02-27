import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MCCTCRocks",
    database = 'ninja_turtles'
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO turtles (name, color, weapon, pizza, age) VALUES (%s, %s, %s, %s, %s)"

turtles = [("Rafpheal", "R4ed", "S6ai", False, 15),
           ("Donaetello", "Purp3le", "B7o", False, 15),
           ("Micheslangelo", "Oran2ge", "Nu5nchakus", False, 15),
           ("Raphgeal", "Re3d", "Sa5i", False, 15),
           ("Donaztello", "Pu4rple", "B3o", False, 15),
           ("Micheblangelo", "Ora5nge", "Nunchakus", False, 15),
           ("Rap6heal", "Red", "S4ai", False, 15),
           ("Dona5tello", "Pur3ple", "B5o", False, 15),
           ("Michelan3gelo", "Orang3e", "Nunchaku5s", False, 15),
           ("Donate6llo", "Purp3le", "5Bo", False, 15),
           ("Michel7angelo", "Ora5nge", "Nunchak3us", False, 15)]

mycursor.executemany(sqlFormula, turtles)

mydb.commit()