import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="kiku",
    password="elsd4988",
    database="epl"
)
# 팀 별 승리를 저장하는 테이블 생성. 여기서는 Liverpool의 테이블 생성
sql = "CREATE TABLE LiverpoolWins (id INT AUTO_INCREMENT PRIMARY KEY, season VARCHAR(255), hometeam VARCHAR(255), awayteam VARCHAR(255), FTR VARCHAR(255))"
mycursor = mydb.cursor()
mycursor.execute(sql)