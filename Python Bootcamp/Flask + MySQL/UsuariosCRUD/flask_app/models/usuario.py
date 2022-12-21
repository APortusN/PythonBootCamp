# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
# import re
# el módulo regex
# crea un objeto de expresión regular que usaremos más adelante
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo_electronico = data['correo_electronico']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios
    # método de clase para guardar a nuestro amigo en la base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , apellido , correo_electronico , created_at, updated_at ) VALUES ( %(fnombre)s , %(fapellido)s , %(fcorreoe)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM usuarios WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0]) #debe coincidir con el for
    
    @classmethod
    def update(cls,data):
        query = "UPDATE usuarios SET nombre=%(fnombre)s,apellido=%(fapellido)s,correo_electronico=%(fcorreoe)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    
    # @staticmethod
    # def validate_user( user ):
    #     is_valid = True
    #     # prueba si un campo coincide con el patrón
    #     if not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     return is_valid