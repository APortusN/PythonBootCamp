from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save (cls, data):
        query = "INSERT INTO  ninjas (first_name, last_name, age, dojo_id) VALUES (%(fnombre)s, %(fapellido)s, %(fedad)s, %(dojo_id)s);"
        return connectToMySQL('esquema_dojos_y_ninjas2').query_db(query, data)
    
    @classmethod
    def get_un_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id_ninja)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas2').query_db(query, data)
        return results[0]