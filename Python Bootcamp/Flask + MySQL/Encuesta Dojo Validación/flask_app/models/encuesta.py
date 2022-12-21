from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Encuesta:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.lenguaje = data['lenguaje']
        self.comentarios = data['comentarios']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into encuestas (nombre,ubicacion,lenguaje,comentarios) VALUES (%(nombre)s,%(ubicacion)s,%(lenguaje)s,%(comentarios)s);"
        return connectToMySQL('esquema_encuesta_dojo').query_db(query,data)

    @classmethod
    def get_ultima_encuesta(cls):
        query = "SELECT * FROM encuestas ORDER BY encuestas.id DESC LIMIT 1;"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        return Encuesta(results[0])

    @staticmethod
    def validar_encuesta(encuesta):
        is_valid = True
        if len(encuesta['nombre']) < 4:
            is_valid = False
            flash("Su nombre debe tener al menos 4 caracteres.")
        if len(encuesta['ubicacion']) < 1:
            is_valid = False
            flash("Debe ingresar una ubicación.")
        if len(encuesta['lenguaje']) < 1:
            is_valid = False
            flash("Debe elegir un lenguaje favorito.")
        if len(encuesta['comentarios']) < 6:
            is_valid = False
            flash("Los comentarios deben tener al menos 6 caracteres.")
        return is_valid