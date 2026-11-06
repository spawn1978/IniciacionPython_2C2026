import sqlite3

con = sqlite3.connect('inventario.db')
cur = con.cursor()  


cur.executescript('DROP TABLE IF EXISTS elementos')
con.commit()