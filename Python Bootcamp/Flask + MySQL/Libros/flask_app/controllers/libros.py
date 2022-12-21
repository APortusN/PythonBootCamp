from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.autor import Autor
from flask_app.models.libro import Libro
from flask_app.models import libro


@app.route('/libros')
def libros():
    return render_template('libros.html',todos_libros=Libro.get_todos())

@app.route('/crear/libro',methods=['POST'])
def crear_libro():
    data = {
        "titulo":request.form['titulo'],
        "num_de_pag": request.form['num_de_pag']
    }
    libro_id = Libro.save(data)
    return redirect('/libros')

@app.route('/libro/<int:id>')
def ver_libro(id):
    data = {
        "id":id
    }
    return render_template('ver_libro.html',libro=Libro.get_por_id(data),autores_no_favoritos=Autor.autores_no_favoritos(data))

@app.route('/autorfavorito',methods=['POST'])
def autor_favorito():
    data = {
        'autor_id': request.form['autor_id'],
        'libro_id': request.form['libro_id']
    }
    Autor.agregar_favorito(data)
    return redirect(f"/libro/{request.form['libro_id']}")