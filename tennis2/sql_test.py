import sqlite3 as sql


conn = sql.connect(':memory:')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE players
					(date, name, rank)
				""")
cursor.execute("INSERT INTO players VALUES ('2012-05-05', 'Rafael Nadal', '1',)")

conn.commit()
conn.close()