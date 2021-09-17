import sqlite3

#Creating a database named movies
conn = sqlite3.connect('movies.db')


cursor = conn.cursor()

#Creating the table named movies with the required fields

sql ='''CREATE TABLE MOVIES(
   MOVIE_NAME CHAR(20) NOT NULL,
   LEAD_ACTOR CHAR(20),
   LEAD_ACTRESS CHAR(25),
   YEAR_OF_RELEASE INT(6),
   Director CHAR(20)
)'''
cursor.execute(sql)
#printing if the table is created successfully
print("Table created successfully........")


conn.commit()

conn.close()