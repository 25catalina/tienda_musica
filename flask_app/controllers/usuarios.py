from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando
from flask_app.models.favorito import Favorito
from flask_app.models.usuario import Usuario
from flask_app.models.cancion import Cancion

@app.route("/")
#se va a la ruta principal y redirige a la ruta de usuarios, por que la ruta del menu no se puede llamar "/"por que se va a confundir con las rutas de todos lo py de controllers, por eso se llama "/usuarios"
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios", methods=["GET"]) #solo es GET por que no se va a mandar nada, solo se va a mostrar la pagina de usuarios
def registro():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/guardar', methods=["POST"]) 
#recuerda catita que donde se guarda la info de los usuarios es en la ruta "/guardar" por que es la ruta que se manda en el formulario de "usuarios.html"
def guardar():
    datos = {
        "nombre": request.form['nombre'],
        "gmail": request.form['gmail'],
        "password": request.form['password']
    } #no tiene el updated_at o el created_at por que el formulario no lo pide y el id tampoco
    Usuario.save(datos)
    return redirect("/usuarios")

@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    datos = {
        "id": id}
    usuario = Usuario.get_one(datos)
    favoritas = Cancion.get_favoritas_de(datos) #este get llama las canciones favoritas del usuario
    canciones = Cancion.get_all()
#el get one es para traer un solo usuario, el get_all es para traer todos los usuarios, osea get one llama a tu mamá y el get_all a toda tu familia
    return render_template("mostrar_usuario.html", usuario = usuario,
                            favoritas = favoritas,
                            canciones = canciones)

@app.route("/guardar_favorito", methods=["POST"])
def guardar_favorito():
    datos = {
        "usuario_id": request.form['usuario_id'],
        "cancion_id": request.form['cancion_id']
    }
    Favorito.save(datos)
    return redirect(f"/usuarios/{request.form['usuario_id']}")