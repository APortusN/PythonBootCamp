from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []    # aqui "vive" el metodo de clase get_dojo_with_ninjas lista de instancias de ninjas u objetos de ninja

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas2').query_db(query)
        dojos = []
        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(fnombred)s);"
        result = connectToMySQL('esquema_dojos_y_ninjas2').query_db(query,data)
        return result

    @classmethod
    def get_dojo_with_ninjas(cls, data):    # obtener un dojo con todos los ninjas asociados a el
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas2').query_db(query,data)
        # los resultados serán una lista de objetos 
        dojo = cls(results[0])
        for row in results:
            # ahora parseamos los datos de ninja para crear instancias de ninja y agregarlas a nuestra lista
            ninja_data = {
                'id': row['ninjas.id'],  # cuando hay nombres de columnas comunes entre dos tablas 
                'first_name': row['first_name'],    # se antepone el nombre de la llave
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data)) # ninja.Ninja se instanacia  y se agrega a la lista de dojos
        return dojo