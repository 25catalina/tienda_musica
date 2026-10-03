from flask_app.config.mysqlconnection import connectToMySQL

class Cancion:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        results = connectToMySQL('esquema_canciones').query_db(query)
        canciones = []
        for cancion in results:
            canciones.append(cls(cancion))
        return canciones

    @classmethod
    def save(cls, data):
        query = "INSERT INTO canciones (titulo, artista, created_at, updated_at) VALUES (%(titulo)s, %(artista)s, NOW(), NOW());"
        return connectToMySQL('esquema_canciones').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        return cls(results[0]) if results else None
    
    @classmethod
    def get_favoritas_de(cls, data):
        query = """SELECT canciones.* FROM canciones JOIN favoritos ON favoritos.cancion_id = canciones.id
               WHERE favoritos.usuario_id = %(id)s;"""
        results = connectToMySQL('esquema_canciones').query_db(query, data)
        favoritas = []
        for cancion in results:
            favoritas.append(cls(cancion))
        return favoritas