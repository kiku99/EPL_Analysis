import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="kiku",
    password="elsd4988",
    database="epl"
)

sql = "CREATE TABLE ManUnitedWins (id INT AUTO_INCREMENT PRIMARY KEY, season VARCHAR(255), hometeam VARCHAR(255), awayteam VARCHAR(255), FTR VARCHAR(255))"
mycursor = mydb.cursor()
mycursor.execute(sql)

