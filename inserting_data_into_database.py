import sqlite3

#connecting to the existing database
conn = sqlite3.connect('movies.db')


cursor = conn.cursor()

#inserting the data in the table movies
cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('RUN', 'MADHAVAN', 'MEERA JASMINE', 2002, 'LINGUSAMY')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('PAIYAA', 'KARTHI', 'TAMMANAH', 2010 , 'LINGUSAMY')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('THANI ORUVAN', 'JAYAM RAVI', 'NAYANTHARA', 2015, 'MOHAN RAJA')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('KATHAKALI', 'VISHAL', 'CATHERINE THERASA', 2016, 'PANDIYA RAJ')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('VISWASAM', 'AJITH', 'NAYANTHARA', 2019, 'SIVA')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('THUPPAKKI', 'VIJAY', 'KAJAL AGARWALL', 2012, 'A R MURGADOSS')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('PETTA', 'RANJINIKANTH', 'SIMRAN', 2019, 'KARTHIK SUBBURAJ')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('SETHUPATHI', 'VIJAY SETHUPATHI', 'RAMYA NAMBEESAN', 2016, 'ARUN KUMAR')''')

cursor.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('KARNAN', 'DHANUSH', 'RAJISHA VIJAYAN', 2021, 'MARI SELVARAJ')''')



conn.commit()
#printing if the datas are successfully inserted
print("Records inserted........")


conn.close()