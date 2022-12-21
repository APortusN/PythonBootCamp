from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_app.models.mensaje import Mensaje

@app.route('/enviar/mensaje',methods=['POST'])
def enviar_mensaje():
    if 'usuario_id' not in session:
        return redirect('/')

    data = {
        "emisor_id":  request.form['emisor_id'],
        "receptor_id" : request.form['receptor_id'],
        "contenido": request.form['contenido']
    }
    Mensaje.save(data)
    return redirect('/tablero')

@app.route('/eliminar/mensaje/<int:id>')
def eliminar_mensaje(id):
    data = {
        "id": id
    }
    Mensaje.destroy(data)
    return redirect('/tablero')