import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
select = "SELECT * FROM notes"
cursor.execute(select)
rows = cursor.fetchall()
for row in rows:
    print(row)


connection.commit()