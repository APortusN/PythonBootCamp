from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Mensaje:
    db = 'muro_privado'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.contenido = db_data['contenido']
        self.emisor_id = db_data['emisor_id']
        self.emisor = db_data['emisor']
        self.receptor_id = db_data['receptor_id']
        self.receptor = db_data['receptor']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f"{delta.days} días atrás"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} horas atrás"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutos atrás"
        else:
            return f"{math.floor(delta.total_seconds())} segundos atrás"

    @classmethod
    def get_usuario_mensajes_recividos(cls,data):
        query = "SELECT usuarios.nombre as emisor, usuarios2.nombre as receptor, mensajes.* FROM usuarios LEFT JOIN mensajes ON usuarios.id = mensajes.emisor_id LEFT JOIN usuarios as usuarios2 ON usuarios2.id = mensajes.receptor_id WHERE usuarios2.id =  %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        if results == False:
            return None
        mensajes_recibidos = []
        for row in results:
            mensajes_recibidos.append( cls(row) )
        return mensajes_recibidos

    @classmethod
    def get_mensajes_enviados(cls, data):
        query = "SELECT usuarios.nombre as emisor, usuarios2.nombre as receptor, mensajes.* FROM usuarios LEFT JOIN mensajes ON usuarios.id = mensajes.emisor_id LEFT JOIN usuarios as usuarios2 ON usuarios2.id = mensajes.receptor_id WHERE emisor_id =  %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results,"###################################")
        if results == False:
            return None
        mensajes_enviados = []
        for row in results:
            mensajes_enviados.append( row )
        return mensajes_enviados

    @classmethod
    def save(cls,data):
        query = "INSERT INTO mensajes (contenido,emisor_id,receptor_id) VALUES (%(contenido)s,%(emisor_id)s,%(receptor_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM mensajes WHERE mensajes.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)