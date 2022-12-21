from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
CONTRASE_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])')
from flask import flash

class Usuario:
    db = "inicio_sesion_registro"
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.fecha_nacimiento = data['fecha_nacimiento']
        self.email = data['email']
        self.contraseña = data['contraseña']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, email, contraseña) VALUES(%(nombre)s,%(apellido)s, %(fecha_nacimiento)s, %(email)s,%(contraseña)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_todos(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db).query_db(query)
        usuarios= []
        for row in results:
            usuarios.append( cls(row))
        return usuarios

    @classmethod
    def get_por_email(cls,data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_por_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validador_registro(usuario):
        is_valid = True
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(Usuario.db).query_db(query,usuario)
        if len(results) >= 1:
            flash("El email ya ha sido registrado","registro")
            is_valid=False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Email invalido","registro")
            is_valid=False
        if len(usuario['nombre']) < 2:
            flash("Nombre debe tener al menos 2 caracteres","registro")
            is_valid= False
        if len(usuario['apellido']) < 2:
            flash("Apellido debe tener al menos 2 caracteres","registro")
            is_valid= False
        if usuario['fecha_nacimiento'] == "":
            flash("Ingrese fecha nacimiento","registro")
            is_valid = False
        if len(usuario['contraseña']) < 8:
            flash("Contraseña debe tener al menos 8 caracteres","registro")
            is_valid= False
        if not CONTRASE_REGEX.match(usuario['contraseña']):
            flash("Email debe contener al menos un dígito y al menos una mayúscula","registro")
            is_valid=False
        if usuario['contraseña'] != usuario['confirmar_contraseña']:
            flash("Las contraseñas no coinciden","registro")
            is_valid = False
        return is_valid