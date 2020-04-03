#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","240792","kgannotation" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO user(userId,
   firstName, lastName, emailAddress, userType)
   VALUES (2, 'Sam', 'Ford', 'sam.ford@unt.edu', 'System Architect')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()