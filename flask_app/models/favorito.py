from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import favoritos

class Favorito:
    def __init__(self, data):
        self.id = data['id']
        self.usuario_id = data['usuario_id']
        self.cancion_id = data['cancion_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM favoritos;"
        results = connectToMySQL('esquema_canciones').query_db(query)
        favoritos = []
        for favorito in results:
            favoritos.append(cls(favorito))
        return favoritos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO favoritos (usuario_id, cancion_id) VALUES (%(usuario_id)s, %(cancion_id)s);"
        return connectToMySQL('esquema_canciones').query_db(query, data)