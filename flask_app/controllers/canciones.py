from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash

#importamos la clase que estamos controlando

from flask_app.models.cancion import Cancion
from flask_app.models.favorito import Favorito
from flask_app.models.usuario import Usuario



@app.route("/canciones", methods=["GET"]) #la primera ruta de canciones se debe llamar "/canciones" por que el python es medio especial y debes ser mas especifica
def registro_cancion():
    canciones = Cancion.get_all()
    return render_template("canciones.html", canciones=canciones)

@app.route('/guardar_cancion', methods=["POST"]) 
#catita del futuro, las definicines o nombres de la rutas deben ser DIFERENTES a las de los otros py de controllers, por que el python confunde y no funciona
#por eso esta ruta se llama "/guardar_cancion" y la de usuarios se llama "/guardar"
def guardar_cancion():
    
    datos = {
        "titulo": request.form['titulo'],
        "artista": request.form['artista']
    }
    Cancion.save(datos)
    return redirect("/canciones") 
#no te olvides catita que la ruta de redireccionamiento te puede llevar a la ruta que quieres sin tanto relleno

@app.route("/canciones/<int:id>")
def mostrar_cancion(id):
    datos = {"id": id}
    cancion = Cancion.get_one(datos)
    fans = Usuario.get_fans_de(datos)
    usuarios = Usuario.get_all()
    return render_template("mostrar_cancion.html",
                           cancion = cancion,
                           fans = fans,
                           usuarios = usuarios)


@app.route("/guardar_favorito_cancion", methods=["POST"])
def guardar_favorito_cancion():
    usuario_id = request.form['usuario_id']
    cancion_id = request.form['cancion_id']
    datos = {"usuario_id": usuario_id, "cancion_id": cancion_id}
    Favorito.save(datos)
    return redirect(f"/canciones/{cancion_id}")