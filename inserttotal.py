import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="kiku",
  password="elsd4988",
  database="epl"
)

mycursor = mydb.cursor(prepared=True)

sql = "INSERT INTO total (season, datetime, hometeam, awayteam, FTHG, FTAG, FTR, HTHG, HTAG, HTR, HST, AST, HC, AC, HF, AF) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

f = open('epl.csv', 'r', encoding='latin1')
rd = csv.reader(f)
for row in rd :
  
  season = (row[0])
  datetime = (row[1])
  hometeam = (row[2])
  awayteam = (row[3])
  FTHG = (row[4])
  FTAG = (row[5])
  FTR = (row[6])
  HTHG = (row[7])
  HTAG = (row[8])
  HTR = (row[9])
  HST = (row[13])
  AST = (row[14])
  HC = (row[15])
  AC = (row[16])
  HF = (row[17])
  AF = (row[18])

  
  val = (season, datetime, hometeam, awayteam, FTHG, FTAG, FTR, HTHG, HTAG, HTR, HST, AST, HC, AC, HF, AF)

  mycursor.execute(sql, val)  
  

mydb.commit()


    




