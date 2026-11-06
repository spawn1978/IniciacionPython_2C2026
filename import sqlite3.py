import sqlite3

con = sqlite3.connect('inventario.db')
cur = con.cursor()  


cur.execute('''CREATE TABLE IF NOT EXISTS elementos
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT )''')
cur.execute('''INSERT INTO elementos (nombre, descripcion, cantidad, precio, categoria) VALUES
               ('Sandia', 'Fruta roja', 1, 1000.0, 'Frutas'),
               ('Mandarina', 'Fruta naranja', 2, 2000.0, 'Frutas'),
               ('Naranja', 'Fruta amarilla', 3, 30000, 'Frutas')''')
con.commit()