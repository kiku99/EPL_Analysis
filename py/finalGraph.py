import mysql.connector
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
    host="localhost",
    user="kiku",
    password="elsd4988",
    database="epl"
)

plt.figure(figsize=(30, 10))
plt.grid()
plt.xlabel('seasons',labelpad=15)
plt.ylabel('wins', labelpad= 15)
plt.plot(ad[0], ad[1], label='arsenal')
plt.plot(ld[0], ld[1], label='liverpool')
plt.plot(cd[0], cd[1], label='chelsea')
plt.plot(md[0], md[1], label='man united')
plt.legend()
plt.show()