from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    # using a class variable to hold my database name
    db = "validacion_correo"
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updatd_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query,email)            #duda Email.db ()
        if len(results) >= 1:                                           #duda pq >= (lee un arreglo)
            flash("¡El correo electrónico ya fue registrado!")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("¡El correo electrónico ingresado no es válido!")
            is_valid=False
        if EMAIL_REGEX.match(email['email']):
            flash("¡El correo electrónico ingresado es válido!")
            is_valid=True
        return is_valid