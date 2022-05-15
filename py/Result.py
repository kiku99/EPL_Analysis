import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="kiku",
    password="elsd4988",
    database="epl"
)

mycursor = mydb.cursor()
# 각 시즌별 팀 승리 횟수 출력. 여기서는 Liverpool 승리 횟수 출력
mycursor.execute("select season, count(season) from LiverpoolWins group by season")
myresult = mycursor.fetchall()
liverpoolWins=[]
for x in myresult:
    liverpoolWins.append(x)
    print(x)
