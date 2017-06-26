from flask import Flask, jsonify
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
    return(respuesta)

app.run()
