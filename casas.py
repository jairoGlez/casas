import sqlite3

db = sqlite3.connect("casas.db")
c = db.cursor()

def mostrarCompradores():
    r = c.execute("SELECT * FROM comprador")
    r = r.fetchall()

    for fila in r:
        print (fila)

def nuevoComprador(datos):
    c.execute("INSERT INTO comprador (email,nombre,apellido1,apellido2,idVendedor) VALUES (?,?,?,?,?)",(datos[0],datos[1],datos[2],datos[3],datos[4]))
    db.commit()

nuevoComprador(["toño78@hotmail.com","antonio","jimenez","torrez",5])
mostrarCompradores()
