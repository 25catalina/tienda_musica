from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando
from flask_app.models.cancion import Cancion
from flask_app.models.usuario import Usuario



@app.route("/", methods=["GET", "POST"])
def registro():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("usuarios.html")

@app.route('/guardar', methods=["POST"])
def guardar():
    datos = {
        "titulo": request.form['nombre'],
        "artista": request.form['apellido']}
    Cancion.save(datos)
    return redirect("/nueva_cancion")


@app.route("/nueva_cancion")
def mostrar_canciones():
    canciones = Cancion.get_all()
    return render_template("canciones.html", canciones=canciones)

@app.route("/ver_cancion/<int:id>")
def ver_cancion(id):
    datos = {
        "id": id
    }
    canción = Cancion.obtener_uno(datos)
    return render_template("informacion_cancion.html", canción=canción)