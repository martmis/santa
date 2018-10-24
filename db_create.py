import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE santas (name TEXT, mail TEXT)')
print "Table created successfully";
conn.close()