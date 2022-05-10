import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kiku",
  password="elsd4988",
  database="epl"
)

sql = "CREATE TABLE total (id INT AUTO_INCREMENT PRIMARY KEY, season VARCHAR(255), datetime VARCHAR(255), hometeam VARCHAR(255), awayteam VARCHAR(255), FTHG INT, FTAG INT, FTR VARCHAR(255), HTHG INT, HTAG INT, HTR VARCHAR(255), HST INT, AST INT, HC INT, AC INT, HF INT, AF INT)"


mycursor = mydb.cursor()

mycursor.execute(sql)

mycursor.execute("show table")
for x in mycursor:
    print(x)
