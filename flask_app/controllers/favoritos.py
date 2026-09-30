from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando


from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito


@app.route("/")
def index():

   # Invocamos al método de clase get all para obtener todas las canciones
   canciones = Cancion.get_all()
   print(canciones)

   #Crea un archivo index.html para que se por lo pronto
   return render_template("index.html", canciones = canciones)

@app.route ("/crear_cancion", methods= ["POST"] )
def crear_datos():
    datos = {"titulo": request.form["titulo"],
            "artista": request.form["artista"]}
    Cancion.save(datos)
    return redirect('/')