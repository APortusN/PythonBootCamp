from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_app.models import usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro',methods=['POST'])
def registro():
    if not Usuario.validador_registro(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])
    print(pw_hash)
    data ={ 
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "fecha_nacimiento":request.form['fecha_nacimiento'],
        "email": request.form['email'],
        "contraseña": pw_hash
    }
    usuario_id = Usuario.save(data)
    session['usuario_id'] = usuario_id

    return redirect('/tablero')

@app.route('/iniciosesion',methods=['POST'])
def inicio_sesion():
    usuario = Usuario.get_por_email(request.form)

    if not usuario:
        flash("Email invalido","iniciosesion")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['contraseña']):
        flash("Contraseña invalida", "iniciosesion")
        return redirect('/')
    session['usuario_id'] = usuario.id
    return redirect('/tablero')

@app.route('/tablero')
def dashboard():
    if 'usuario_id' not in session:                 #para evitar entrar a otras rutas no logeado (agregar a todas rutas donde se redireccionan platillas)
        return redirect('/cierresesion')
    data ={
        'id': session['usuario_id']
    }
    return render_template("tablero.html", usuario=Usuario.get_por_id(data))

@app.route('/cierresesion')
def cierre_sesion():
    session.clear()
    return redirect('/')