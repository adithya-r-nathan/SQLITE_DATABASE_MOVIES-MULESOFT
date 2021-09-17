import sqlite3

#connecting to the existing database movies
conn = sqlite3.connect('movies.db')


cursor = conn.cursor()

#selecting all the records from the table
cursor.execute('''SELECT * from MOVIES''')
#printing all the records from the table
result = cursor.fetchall();
print(result)

#selecting the particular row with the field where director is lingusamy
cursor.execute("SELECT MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR FROM MOVIES WHERE DIRECTOR = 'LINGUSAMY'")
#printing the rows where the director is lingusamy
print (cursor.fetchall() )


conn.commit()


conn.close()