from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import usuarios
from flask_app.controllers import canciones


if __name__=="__main__": #Ejecutamos la aplicación

   app.run(debug=True)