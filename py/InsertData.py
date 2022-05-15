import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="kiku",
    password="elsd4988",
    database="epl"
)

mycursor = mydb.cursor(prepared=True)
# 팀 별 승리 데이터를 테이블에 삽입. 여기서는 Liverpool의 정보를 삽입
sql = "INSERT INTO LiverpoolWins (season, hometeam, awayteam, FTR) VALUES (%s, %s, %s, %s)"


f = open('LiverpoolWins.csv', 'r', encoding='latin1')
rd = csv.reader(f)

for row in rd :
    season = (row[0])
    hometeam = (row[1])
    awayteam = (row[2])
    FTR = (row[3])

    val = (season, hometeam, awayteam, FTR)

    mycursor.execute(sql, val)  

mydb.commit()