
import psycopg2 as dbapi

con = dbapi.connect("dbname='datos' user='postgres' host='localhost' password='abcd1234'")
cur = con.cursor()
sql = "select * from dioses where nombre = 'zeus'"
cur.execute(sql)

for fila in cur.fetchall():
    print(fila)
    print(fila[1])

#sql = "insert into dioses (nombre, poder) values ('hefesto', 'forja')"
#cur = con.cursor()
#cur.execute(sql)

cur.close()
#con.commit()
con.close()
