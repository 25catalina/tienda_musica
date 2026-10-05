from flask_app import app #Importamos la app de la carpeta flask_app
from flask_app.controllers import usuarios
from flask_app.controllers import canciones

# si vas a crear un entorno virtual, debe tener esto;
# pymysql = "*"
# flask = "*"
# flask-bcrypt = "*"
# flask-mysqldb = "*"
# el comando para crear el entorno virtual es:pipenv install flask-bcrypt pipenv install flask-mysqldb 

if __name__=="__main__": #Ejecutamos la aplicación

   app.run(debug=True)