from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.gmail = data['gmail']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('esquema_canciones').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, gmail, password, created_at, updated_at) VALUES (%(nombre)s, %(gmail)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('esquema_canciones').query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def get_fans_de(cls, data):
        query = """SELECT usuarios.* FROM usuarios JOIN favoritos ON favoritos.usuario_id = usuarios.id WHERE favoritos.cancion_id = %(id)s;"""
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios