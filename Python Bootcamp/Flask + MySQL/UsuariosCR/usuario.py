# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
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