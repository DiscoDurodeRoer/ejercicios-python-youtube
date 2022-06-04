import pymysql

db = pymysql.connect("localhost","root","","pokemondb")

cursor = db.cursor()

cursor.execute("SELECT * from pokemon")

# Fetch all the rows in a list of lists.
resultados = cursor.fetchall()
for row in resultados:
    id = row[0]
    name = row[1]
    print ("ID: ", id, ", nombre: ", name)

db.close()