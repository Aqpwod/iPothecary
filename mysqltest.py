#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="localhost",  # your host 
                     user="cory",       # username
                     passwd="ipothecary",     # password
                     db="pills")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
# print the first and second columns      

    
cur.execute("INSERT INTO pilltimes (name,container,number,time) VALUES (%s,%s,%s,%s)",
            ('Bill',0,2,31230)) #DayOfWeekHourMinute
db.commit()

cur.execute("SELECT * FROM pilltimes")
for row in cur.fetchall() :
    print(row[0])
    
print("Done")
