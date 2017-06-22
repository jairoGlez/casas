import sqlite3

class Casa:
    db = sqlite3.connect("casas.db")
    c = db.cursor()

    def mostrarCompradores(self):
        r = self.c.execute("SELECT * FROM comprador")
        r = r.fetchall()
        lista = []

        for fila in r:
            lista.append(fila)

        return lista

    def nuevoComprador(self,datos):
        self.c.execute("INSERT INTO comprador (email,nombre,apellido1,apellido2,idVendedor) VALUES (?,?,?,?,?)",(datos[0],datos[1],datos[2],datos[3],datos[4]))
        self.db.commit()
