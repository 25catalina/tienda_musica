from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando
from flask_app.models.usuario import Usuario

@app.route("/")
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios", methods=["GET"])
def registro():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/guardar', methods=["POST"])
def guardar():
    datos = {
        "nombre": request.form['nombre'],
        "gmail": request.form['gmail'],
        "password": request.form['password']
    }
    Usuario.save(datos)
    return redirect("/usuarios")

@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    datos = {
        "id": id}
    usuario = Usuario.get_one(datos)
    return render_template("mostrar_usuario.html", usuario = usuario)