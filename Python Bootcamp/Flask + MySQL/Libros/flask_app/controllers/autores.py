from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.autor import Autor
from flask_app.models.libro import Libro


@app.route('/')
def index():
    return redirect('/autores')

@app.route('/autores')
def autores():
    return render_template('autores.html',todos_autores=Autor.get_todos())

@app.route('/crear/autor',methods=['POST'])
def crear_autor():
    data = {
        "nombre": request.form['nombre']
    }
    autor_id = Autor.save(data)
    return redirect('/autores')

@app.route('/autor/<int:id>')
def ver_autor(id):
    data = {
        "id": id
    }
    return render_template('ver_autor.html', autor = Autor.get_por_id(data), libros_no_favoritos = Libro.libros_no_favoritos(data))

@app.route('/librofavorito',methods=['POST'])
def libro_favorito():
    data = {
        'autor_id': request.form['autor_id'],
        'libro_id': request.form['libro_id']
    }
    Autor.agregar_favorito(data)
    return redirect(f"/autor/{request.form['autor_id']}")