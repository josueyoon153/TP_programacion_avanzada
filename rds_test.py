import psycopg2
engine = psycopg2.connect(
	database= "databasetp-1",
	user= "postgres",
	password = "udesatp1",
	host = "databasetp-1.cxypcj5ews3d.us-east-1.rds.amazonaws.com",
	port = '5432'
)

cursor = engine.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tabla ( id INT PRIMARY KEY );""")

cursor.execute("""SELECT * FROM tabla""")
rows = cursor.fetchall()
for row in rows:
	print(row)
print('termino primera query')

cursor.execute("""INSERT INTO tabla(id) VALUES(4)""")
cursor.execute("""SELECT * FROM tabla""")
rows = cursor.fetchall()
for row in rows:
	print(row)
print('termino segundo query')