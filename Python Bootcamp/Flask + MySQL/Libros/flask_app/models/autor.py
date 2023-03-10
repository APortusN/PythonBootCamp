from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import libro

class Autor:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.libros_favoritos = []


    @classmethod
    def get_todos(cls):
        query = "SELECT * FROM autores;"
        autores = []
        results = connectToMySQL('esquema_libros').query_db(query)
        for row in results:
            autores.append(cls(row))
        return autores

    @classmethod
    def save(cls,data):
        query = "INSERT INTO autores (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('esquema_libros').query_db(query,data)

    @classmethod
    def autores_no_favoritos(cls,data):
        query = "SELECT * FROM autores WHERE autores.id NOT IN ( SELECT autor_id FROM favoritos WHERE libro_id = %(id)s );"
        autores = []
        results = connectToMySQL('esquema_libros').query_db(query,data)
        for row in results:
            autores.append(cls(row))
        return autores

    @classmethod
    def agregar_favorito(cls,data):
        query = "INSERT INTO favoritos (autor_id,libro_id) VALUES (%(autor_id)s,%(libro_id)s);"
        return connectToMySQL('esquema_libros').query_db(query,data);


    @classmethod
    def get_por_id(cls,data):
        query = "SELECT * FROM autores LEFT JOIN favoritos ON autores.id = favoritos.autor_id LEFT JOIN libros ON libros.id = favoritos.libro_id WHERE autores.id = %(id)s;"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        autor = cls(results[0])
        for row in results:
            if row['libros.id'] == None:
                break
            data = {
                "id": row['libros.id'],
                "titulo": row['titulo'],
                "num_de_pag": row['num_de_pag'],
                "created_at": row['libros.created_at'],
                "updated_at": row['libros.updated_at']
            }
            autor.libros_favoritos.append(libro.Libro(data))
        return autor