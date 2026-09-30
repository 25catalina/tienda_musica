from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.cancion import Cancion



@app.route("/canciones", methods=["GET"])
def registro_cancion():
    canciones = Cancion.get_all()
    return render_template("canciones.html", canciones=canciones)

@app.route('/guardar_cancion', methods=["POST"])
def guardar_cancion():
    
    datos = {
        "titulo": request.form['titulo'],
        "artista": request.form['artista']
    }
    Cancion.save(datos)
    return redirect("/canciones")