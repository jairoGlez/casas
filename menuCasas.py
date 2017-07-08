from casas import Casa

class Menu:
    casa = Casa()
    def __init__(self):
        while True:
            print("1) Mostrar Compradores")
            print("2) Agregar comprador")
            print("3) Buscar")
            print("0) Salir")
            op = input()

            if op == "1":
                self.mostrar()
            elif op == "2":
                self.agregar()
            elif op == "3":
                self.buscar()
            elif op == "0":
                break

    def mostrar(self):
        filas = self.casa.mostrarCompradores()
        for fila in filas:
            print("{0:20}{1:10}{2:15}{3:15}{4:2}".format(fila[0],fila[1],fila[2],fila[3],fila[4]))

    def agregar(self):
        email = input("Correo: ")
        nombre = input("Nombre: ")
        apellido1 = input("Apellido Paterno: ")
        apellido2 = input("Apellido Materno: ")
        idVendedor = input("ID del vendedor :")
        self.casa.nuevoComprador([email,nombre,apellido1,apellido2,idVendedor])

    def buscar(self):
        palabra = input("Escribe el correo: ")
        compradores = self.casa.buscar(palabra)

        for e in compradores:
            print("{0:20}{1:10}{2:15}{3:15}{4:2}".format(e["correo"],e["nombre"],e["apellido1"],e["apellido2"],e["idVendedor"]))
