from flask import Flask, jsonify,request
from casas import Casa

app = Flask("bd")
casita = Casa()

@app.route("/")
def raiz():
    return("Servidor proyecto Casas")

@app.route("/casas")
def compradores():
    compradores = casita.mostrarCompradores()
    print(compradores)
    respuesta = jsonify(compradores)
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

@app.route("/nuevoComprador",methods=["POST"])
def nuevoComprador():
    print(request.form)
    correo = request.form["correo"]
    nombre = request.form["nombre"]
    apellido1 = request.form["apellido1"]
    apellido2 = request.form["apellido2"]
    vendedor = request.form["vendedor"]

    casita.nuevoComprador([correo,nombre,apellido1,apellido2,vendedor])

    respuesta = jsonify({"status":"Ok"})
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

app.run()
