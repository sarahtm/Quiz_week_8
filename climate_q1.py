import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

cursor.execute("SELECT year, co2, temperature FROM ClimateData;")
data = cursor.fetchall()

conn.close()
        
years = []
co2 = []
temperature = []

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temperature.append(row[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temperature, 'r*-')
plt.ylabel("Temperature (C)")
plt.xlabel("Year (decade)") 

plt.savefig("co2_temp_1.png") 
plt.show()