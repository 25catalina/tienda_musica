from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, email, password, created_at, updated_at) VALUES (%(nombre)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('esquema_usuarios').query_db(query, data)

